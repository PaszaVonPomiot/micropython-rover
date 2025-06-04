"""Real Time Clock"""

import machine
from config.storage import RTCPin
from lib.ds1302 import DS1302

int_rtc = machine.RTC()
ext_rtc = ext_rtc = DS1302(clk=RTCPin.CLK, dat=RTCPin.DAT, rst=RTCPin.RST)


def sync_rtc() -> None:
    """Sync internal RTC from external RTC"""
    ext_date_time = ext_rtc.get_date_time()
    ext_date_time.append(0)  # for subseconds
    int_rtc.datetime(tuple(ext_date_time))  # sync
