from __future__ import annotations

import os
from datetime import datetime, timezone, timedelta
from enum import Enum
from fastapi import HTTPException


class Tier(str, Enum):
    FREE = "free"
    PILOT = "pilot"
    ENTERPRISE = "enterprise"


_TIER = Tier(os.getenv("COGNOS_TIER", "enterprise").lower())

PILOT_DAYS = 30


def get_tier() -> Tier:
    return _TIER


# ---------------------------------------------------------------------------
# Free tier limits
# ---------------------------------------------------------------------------

PILOT_LIMITS = {
    "max_tenants": 1,
    "rate_limit": "10000/day",
    "webhook_max_endpoints": 3,
    "webhook_max_events_per_day": 1000,
    "audit_pdf": True,
    "compliance_report_json": True,
    "compliance_report_pdf": True,
    "multi_tenant": False,
    "fallback_provider": True,
    "session_memory": False,
    "token_compressor": False,
    "rbac_roles": {"admin", "operator", "auditor"},
    "custom_rate_limit": False,
}

FREE_LIMITS = {
    "max_tenants": 1,
    "rate_limit": "100/day",
    "webhook_max_endpoints": 1,
    "webhook_max_events_per_day": 100,
    "audit_pdf": False,
    "compliance_report_json": True,
    "compliance_report_pdf": False,
    "multi_tenant": False,
    "fallback_provider": False,
    "session_memory": False,
    "token_compressor": False,
    "rbac_roles": {"admin", "operator"},   # auditor/viewer locked
    "custom_rate_limit": False,
}


def enforce(feature: str) -> None:
    """Raise 402 if feature is locked in current tier."""
    if _TIER == Tier.ENTERPRISE:
        return
    limits = PILOT_LIMITS if _TIER == Tier.PILOT else FREE_LIMITS
    locked = not limits.get(feature, True)
    if locked:
        raise HTTPException(
            status_code=402,
            detail=f"Feature '{feature}' requires TrustPlane SaaS (€999/month). "
                   f"Contact bjorn@base76research.com to upgrade.",
        )


def enforce_pilot_expiry(pilot_started_at: datetime | None) -> None:
    """Raise 402 if pilot period has expired."""
    if _TIER != Tier.PILOT or pilot_started_at is None:
        return
    expires = pilot_started_at + timedelta(days=PILOT_DAYS)
    if datetime.now(timezone.utc) > expires:
        raise HTTPException(
            status_code=402,
            detail=(
                f"Your 30-day TrustPlane pilot expired on "
                f"{expires.strftime('%Y-%m-%d')}. "
                f"Continue with TrustPlane SaaS at €999/month — "
                f"contact bjorn@base76research.com."
            ),
        )


def enforce_tenant_count(current_count: int) -> None:
    if _TIER == Tier.ENTERPRISE:
        return
    limit = PILOT_LIMITS["max_tenants"] if _TIER == Tier.PILOT else FREE_LIMITS["max_tenants"]
    if current_count >= limit:
        raise HTTPException(
            status_code=402,
            detail="Pilot tier is limited to 1 tenant. Contact bjorn@base76research.com to upgrade.",
        )


def get_effective_rate_limit(configured: str) -> str:
    if _TIER == Tier.FREE:
        return FREE_LIMITS["rate_limit"]
    if _TIER == Tier.PILOT:
        return PILOT_LIMITS["rate_limit"]
    return configured


def pilot_expires_at(started_at: datetime) -> datetime:
    return started_at + timedelta(days=PILOT_DAYS)


def tier_info() -> dict:
    limits = (
        FREE_LIMITS if _TIER == Tier.FREE
        else PILOT_LIMITS if _TIER == Tier.PILOT
        else "unlimited"
    )
    return {
        "tier": _TIER.value,
        "limits": limits,
        "pilot_days": PILOT_DAYS if _TIER == Tier.PILOT else None,
        "upgrade_url": "mailto:bjorn@base76research.com" if _TIER != Tier.ENTERPRISE else None,
    }
