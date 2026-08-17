"""Fixed first-stage BTC testing policy."""

from datetime import date


BTC_PAIR = "BTC/USDT"
ALLOWED_TIMEFRAMES = {
    "scalping": ("5m", "15m"),
    "day_trading": ("1h", "4h", "1d"),
}


def candidate_timeframes(suggested_timeframe: str) -> tuple[str, ...]:
    """Return the fixed comparison set for a strategy's trading style."""
    if suggested_timeframe in ALLOWED_TIMEFRAMES["scalping"]:
        return ALLOWED_TIMEFRAMES["scalping"]
    return ALLOWED_TIMEFRAMES["day_trading"]


def three_year_timerange(today: date | None = None) -> str:
    today = today or date.today()
    try:
        start = today.replace(year=today.year - 3)
    except ValueError:  # February 29
        start = today.replace(year=today.year - 3, day=28)
    return f"{start:%Y%m%d}-{today:%Y%m%d}"


def public_policy() -> dict[str, object]:
    return {
        "pair": BTC_PAIR,
        "timerange": three_year_timerange(),
        "scalping_timeframes": list(ALLOWED_TIMEFRAMES["scalping"]),
        "day_trading_timeframes": list(ALLOWED_TIMEFRAMES["day_trading"]),
        "metrics": ["PF", "CAGR", "Max DD", "Trades/day"],
    }
