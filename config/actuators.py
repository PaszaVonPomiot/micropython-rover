from machine import Pin


class BuzzerGPIO:
    """Active buzzer GPIO."""

    PLUS = 15


class BuzzerPin:
    """Active buzzer Pin."""

    PLUS = Pin(BuzzerGPIO.PLUS, mode=Pin.OUT, value=0)
