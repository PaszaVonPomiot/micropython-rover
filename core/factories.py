from machine import Pin, SPI, RTC
from config.sensors import MicConfig
from config.actuators import BuzzerConfig
from config.storage import RTCConfig, SDConfig
from core.buzzer import Buzzer
from core.mic import Mic
from lib.ds1302 import DS1302
from lib.sdcard import SDCard


def buzzer_factory() -> Buzzer:
    return Buzzer(
        pin=Pin(BuzzerConfig.GPIO_PLUS, mode=Pin.OUT, value=0),
        dot_ms=BuzzerConfig.DOT_MS,
        dash_ms=BuzzerConfig.DASH_MS,
        pause_ms=BuzzerConfig.PAUSE_MS,
    )


def mic_factory() -> Mic:
    return Mic(
        adc_pin=Pin(MicConfig.GPIO_ADC),
        output_resolution_bits=MicConfig.OUTPUT_RESOLUTION_BITS,
        raw_input_min=MicConfig.RAW_INPUT_MIN,
        raw_input_max=MicConfig.RAW_INPUT_MAX,
    )


def ext_rtc_factory() -> DS1302:
    return DS1302(
        clk=Pin(RTCConfig.GPIO_CLK),
        dat=Pin(RTCConfig.GPIO_DAT),
        rst=Pin(RTCConfig.GPIO_RST),
    )


def sd_factory() -> SDCard:
    spi = SPI(
        SDConfig.SPI_CONTROLLER,
        sck=SDConfig.GPIO_SCK,
        mosi=SDConfig.GPIO_MOSI,
        miso=SDConfig.GPIO_MISO,
    )
    return SDCard(spi=spi, cs=Pin(SDConfig.GPIO_CS, mode=Pin.OUT))
