from core.factories import ext_rtc_factory

rtc = ext_rtc_factory()
rtc.set_date_time(
    [
        2025,
        6,
        16,
        1,  # weekday
        1,
        57,
        50,
    ]
)
