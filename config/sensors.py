"""Sensor configurations."""


class AmbientSoundSensorConfig:
    """
    Configuration for the ambient sound sensor.

    Attributes:
        GPIO_ADC (int): ADC GPIO pin. Options:
            - GP26 -> A0
            - GP27 -> A1
            - GP28 -> A2
            - GP29 -> A3 (only for VSYS)
        OUTPUT_RESOLUTION_BITS (int): ADC resolution in bits.
        RAW_INPUT_MIN (int): Minimum raw input value.
        RAW_INPUT_MAX (int): Maximum raw input value.
    """

    GPIO_ADC: int = 26
    OUTPUT_RESOLUTION_BITS: int = 12
    RAW_INPUT_MIN: int = 26000
    RAW_INPUT_MAX: int = 58430


class AmbientLightSensorConfig:
    """
    Configuration for the ambient light sensor.

    Attributes:
        I2C_CONTROLLER (int): I2C controller id
        GPIO_SDA (int): I2C pin for SDA.
        GPIO_SCL (int): I2C pin for SCL.
    Ensure that SDA and SCL pins belong to the same I2C controller.
    """

    I2C_CONTROLLER: int = 0
    GPIO_SDA: int = 8
    GPIO_SCL: int = 9
