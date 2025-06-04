"""Sound level meter"""

from config.sensors import Pin
from machine import ADC


class Mic:
    def __init__(
        self,
        adc_pin: Pin,
        output_resolution_bits: int,
        raw_input_min: int,
        raw_input_max: int,
    ) -> None:
        self.mic = ADC(adc_pin)
        self.output_resolution_bits = output_resolution_bits
        self.raw_input_min = raw_input_min
        self.raw_input_max = raw_input_max

    def _scale_to_bits(
        self, input: int, input_min: int, input_max: int, output_resolution_bits: int
    ) -> int:
        """
        ADC usually has 12-bit output resolution (0-4095) therefore 16-bit (0-65535)
        raw input data from microphone can be scaled down without data loss."""
        return int(
            (input - input_min)
            * (2**output_resolution_bits - 1)
            / (input_max - input_min)
        )

    def _get_raw_sound_level(self) -> int:
        """Return raw sound level from the microphone. This is a 16-bit value (0-65535)."""
        return self.mic.read_u16()

    def get_sound_level(self) -> int:
        """Return sound level scaled to output_resolution_bits"""
        return self._scale_to_bits(
            input=self._get_raw_sound_level(),
            input_min=self.raw_input_min,
            input_max=self.raw_input_max,
            output_resolution_bits=self.output_resolution_bits,
        )
