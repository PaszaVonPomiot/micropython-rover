import machine
from config.board import PicoConfig

from core.factories import buzzer_factory
from core.clock import Clock


machine.freq(PicoConfig.MCU_FREQUENCY)
Clock().sync_rtc()
buzzer_factory().dot(2)
