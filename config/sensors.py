from machine import Pin


class MicGPIO:
    """
    GP26 -> A0
    GP27 -> A1
    GP28 -> A2
    GP29 -> A3, only for VSYS
    """

    ADC: int = 26


class MicPin:
    ADC: Pin = Pin(MicGPIO.ADC)


class MicConfig:
    OUTPUT_RESOLUTION_BITS: int = 12
    RAW_INPUT_MIN: int = 26000
    RAW_INPUT_MAX: int = 58430
