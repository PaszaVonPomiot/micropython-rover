import machine
from config.board import Pico
from core.buzzer import Buzzer
from config.actuators import BuzzerPin
from core.rtc import sync_rtc

machine.freq(Pico.MCU_FREQUENCY)

sync_rtc()

buzzer = Buzzer(pin=BuzzerPin.PLUS)
buzzer.dot(2)
