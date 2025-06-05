"""Real Time Clock"""

from machine import RTC
from core.factories import ext_rtc_factory


class Clock:
    """
    Clock is composed of internal (on-board) and external Real Time Clocks.
    Use it to sync internal RTC from external RTC and to produce timestamp.
    """

    def __init__(self) -> None:
        self._int_rtc = RTC()
        self._ext_rtc = ext_rtc_factory()

    def sync_rtc(self) -> None:
        """Sync internal RTC from external RTC"""
        ext_date_time = self._ext_rtc.get_date_time()
        ext_date_time.append(0)  # for subseconds
        self._int_rtc.datetime(tuple(ext_date_time))  # sync

    def now(self) -> str:
        """Return the current date and time in the format 'YYYY-MM-DD HH:MM:SS'."""
        dt: tuple[int, ...] = self._int_rtc.datetime()
        return (
            f"{dt[0]:04d}-{dt[1]:02d}-{dt[2]:02d} {dt[4]:02d}:{dt[5]:02d}:{dt[6]:02d}"
        )
