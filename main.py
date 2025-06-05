from machine import SPI
from core.factories import sd_factory
import uos
from core.logger import (
    LoggerCSV,
)  # FIXME: TypeError: multiple bases have instance lay-out conflict


def main() -> None:
    sd = sd_factory()
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
    print(uos.listdir("/sd"))
    # sensor_logger = LoggerCSV(
    #     file_name="sensor.csv", csv_headers=["date", "value"], buffer_size=3
    # )
    # sensor_logger.write_record_with_buffer("record buffered")
    # sensor_logger.write_record_with_buffer("record buffered")
    # sensor_logger.write_record_with_buffer("record buffered and buffer written to file")
    # sensor_logger.write_record("record written to file directly")


if __name__ == "__main__":
    main()
