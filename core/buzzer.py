from machine import Pin
from utime import sleep_ms


class Buzzer:
    def __init__(
        self,
        pin: Pin,
        dot_ms: int = 100,
        dash_ms: int = 300,
        pause_ms: int = 100,
    ) -> None:
        self.pin = pin
        self.dot_ms = dot_ms
        self.dash_ms = dash_ms
        self.pause_ms = pause_ms

    def beep(self, beep_ms: int, pause_ms: int) -> None:
        self.pin.on()
        sleep_ms(beep_ms)
        self.pin.off()
        sleep_ms(pause_ms)

    def dot(self, count: int = 1) -> None:
        for _ in range(0, count):
            self.beep(beep_ms=self.dot_ms, pause_ms=self.pause_ms)

    def dash(self, count: int = 1) -> None:
        for _ in range(0, count):
            self.beep(beep_ms=self.dash_ms, pause_ms=self.pause_ms)
