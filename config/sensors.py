"""Sensor configurations."""


class MicConfig:
    """
    GP26 -> A0
    GP27 -> A1
    GP28 -> A2
    GP29 -> A3, only for VSYS
    """

    GPIO_ADC: int = 26
    OUTPUT_RESOLUTION_BITS: int = 12
    RAW_INPUT_MIN: int = 26000
    RAW_INPUT_MAX: int = 58430
