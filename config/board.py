"""Board configurations."""

from micropython import const


class PicoConfig:
    """Pico specific configuration."""

    MCU_FREQUENCY: int = const(48_000_000)  # 48 MHz
    STATIC_RTC_DATETIME: tuple[int, ...] = (2025, 5, 3, 4, 12, 0, 0, 0)
