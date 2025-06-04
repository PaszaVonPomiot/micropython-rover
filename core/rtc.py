"""Real Time Clock"""

from core.factories import int_rtc_factory, ext_rtc_factory

int_rtc = int_rtc_factory()
ext_rtc = ext_rtc_factory()


def sync_rtc() -> None:
    """Sync internal RTC from external RTC"""
    ext_date_time = ext_rtc.get_date_time()
    ext_date_time.append(0)  # for subseconds
    int_rtc.datetime(tuple(ext_date_time))  # sync
