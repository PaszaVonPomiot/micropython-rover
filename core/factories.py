from config.sensors import MicPin, MicConfig
from core.mic import Mic


def mic_factory() -> Mic:
    return Mic(
        adc_pin=MicPin.ADC,
        output_resolution_bits=MicConfig.OUTPUT_RESOLUTION_BITS,
        raw_input_min=MicConfig.RAW_INPUT_MIN,
        raw_input_max=MicConfig.RAW_INPUT_MAX,
    )
