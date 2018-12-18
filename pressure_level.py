from machine import ADC, Pin


class PressureLevel(ADC):
    def __init__(self, pin: int):
        super().__init__(Pin(pin))
        self.atten(self.ATTN_11DB)

    @property
    def tank_level(self) -> float:
        return self.read()


