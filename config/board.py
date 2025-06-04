"""Board configuration."""

from micropython import const


class Pico:
    """Pico specific configuration."""

    MCU_FREQUENCY = const(48_000_000)  # 48 MHz
    STATIC_RTC_DATETIME = (2025, 5, 3, 4, 12, 0, 0, 0)  # date after reset
