"""Storage configurations."""


class RTCConfig:
    GPIO_CLK: int = 0
    GPIO_DAT: int = 1
    GPIO_RST: int = 2


class SDConfig:
    SPI_CONTROLLER: int = 1
    GPIO_SCK: int = 10
    GPIO_MOSI: int = 11
    GPIO_MISO: int = 12
    GPIO_CS: int = 13
    MOUNT_POINT: str = "sd"
