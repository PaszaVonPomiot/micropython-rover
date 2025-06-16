from machine import Pin, SPI, I2C
from config.sensors import AmbientSoundSensorConfig, AmbientLightSensorConfig
from config.actuators import BuzzerConfig
from config.storage import RTCConfig, SDConfig
from core.buzzer import Buzzer
from core.mic import AmbientSoundSensor
from lib.ds1302 import DS1302
from lib.sdcard import SDCard
from lib.bh1750 import BH1750


def buzzer_factory() -> Buzzer:
    return Buzzer(
        pin=Pin(BuzzerConfig.GPIO_PLUS, mode=Pin.OUT, value=0),
        dot_ms=BuzzerConfig.DOT_MS,
        dash_ms=BuzzerConfig.DASH_MS,
        pause_ms=BuzzerConfig.PAUSE_MS,
    )


def ambient_sound_sensor_factory() -> AmbientSoundSensor:
    return AmbientSoundSensor(
        adc_pin=Pin(AmbientSoundSensorConfig.GPIO_ADC),
        output_resolution_bits=AmbientSoundSensorConfig.OUTPUT_RESOLUTION_BITS,
        raw_input_min=AmbientSoundSensorConfig.RAW_INPUT_MIN,
        raw_input_max=AmbientSoundSensorConfig.RAW_INPUT_MAX,
    )


def ambient_light_sensor_factory() -> BH1750:
    return BH1750(
        i2c=I2C(
            AmbientLightSensorConfig.I2C_CONTROLLER,
            scl=Pin(AmbientLightSensorConfig.GPIO_SCL),
            sda=Pin(AmbientLightSensorConfig.GPIO_SDA),
        )
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
