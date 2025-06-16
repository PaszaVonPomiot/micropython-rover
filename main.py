import asyncio

from core.clock import Clock
from core.factories import sd_factory
import uos
from core.factories import ambient_sound_sensor_factory, ambient_light_sensor_factory
from core.logger import (
    LoggerCSV,
)

from core.mic import AmbientSoundSensor
from lib.bh1750 import BH1750Mode
from lib.bh1750.bh1750 import BH1750


async def ambient_sound_loop(
    *, clock: Clock, logger: LoggerCSV, sensor: AmbientSoundSensor
) -> None:
    while True:
        logger.write_record_with_buffer(f"{clock.now()} {sensor.get_sound_level()}")
        await asyncio.sleep(10)


async def ambient_light_loop(
    *, clock: Clock, logger: LoggerCSV, sensor: BH1750
) -> None:
    while True:
        luminance = sensor.luminance(
            mode=BH1750Mode.ONCE_HIRES_2
        )  # TODO save mode during init (in factory)
        logger.write_record_with_buffer(f"{clock.now()} {luminance:.2f}")
        await asyncio.sleep(10)


async def main() -> None:
    clock = Clock()
    # print(clock._ext_rtc.get_date_time())
    # print(clock.now())
    sd = sd_factory()
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
    print(uos.listdir("/sd"))
    sensor_sound = ambient_sound_sensor_factory()
    ambient_sound_logger = LoggerCSV(
        file_name="ambient_sound.csv", csv_headers=["date", "value"], buffer_size=3
    )
    ambient_light_sensor = ambient_light_sensor_factory()
    ambient_light_logger = LoggerCSV(
        file_name="ambient_light.csv", csv_headers=["date", "value"], buffer_size=3
    )

    await asyncio.gather(
        ambient_sound_loop(
            clock=clock, logger=ambient_sound_logger, sensor=sensor_sound
        ),
        ambient_light_loop(
            clock=clock, logger=ambient_light_logger, sensor=ambient_light_sensor
        ),
    )

    # sensor_logger.write_record_with_buffer("record buffered")
    # sensor_logger.write_record_with_buffer("record buffered")
    # sensor_logger.write_record_with_buffer("record buffered and buffer written to file")
    # sensor_logger.write_record("record written to file directly")


if __name__ == "__main__":
    asyncio.run(main())
