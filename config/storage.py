from machine import Pin


class RTCGPIO:
    CLK: int = 0
    DAT: int = 1
    RST: int = 2


class RTCPin:
    CLK: Pin = Pin(RTCGPIO.CLK)
    DAT: Pin = Pin(RTCGPIO.DAT)
    RST: Pin = Pin(RTCGPIO.RST)


class SDGPIO:
    SCK: int = 10
    MOSI: int = 11
    MISO: int = 12
    CS: int = 13


class SDPin:
    SCK: Pin = Pin(SDGPIO.SCK)
    MOSI: Pin = Pin(SDGPIO.MOSI)
    MISO: Pin = Pin(SDGPIO.MISO)
    CS: Pin = Pin(SDGPIO.CS, mode=Pin.OUT)


class SDConfig:
    MOUNT_POINT: str = "sd"
