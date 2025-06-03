import machine
from config.board import Pico
from core.buzzer import Buzzer
from config.actuators import BuzzerPin

machine.freq(Pico.MCU_FREQUENCY)
machine.RTC().datetime(Pico.RTC_DATETIME)  # sync internal RTC

buzzer = Buzzer(pin=BuzzerPin.PLUS)
buzzer.dot(2)
