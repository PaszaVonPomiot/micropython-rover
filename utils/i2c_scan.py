from machine import Pin, I2C


class I2CScanner:
    """Scans for I2C devices on specified pins."""

    def __init__(self, *, scl_pin: int = 9, sda_pin: int = 8) -> None:
        self.scl_pin = scl_pin
        self.sda_pin = sda_pin

    def scan(self) -> list[int]:
        """Scans for I2C devices and returns their addresses."""
        i2c = I2C(scl=Pin(self.scl_pin), sda=Pin(self.sda_pin))
        try:
            devices = i2c.scan()
        except Exception as exc:
            print(f"Error scanning I2C devices: {exc}")
            return []
        if devices:
            print(f"I2C devices found: {[hex(device) for device in devices]}")
        else:
            print("No I2C devices found.")
        return devices


def main() -> None:
    """Runs the I2C scan with specified pins."""
    scanner = I2CScanner(scl_pin=9, sda_pin=8)
    scanner.scan()


if __name__ == "__main__":
    main()
