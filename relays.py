from machine import Pin
from typing import Optional
import utime


class Relay(Pin):
    def __init__(self, pin: int, delay: Optional[int]):
        super().__init__(id=pin, mode=self.OUT, value=1)
        self.__delay_time = delay if delay is not None else 0

    def cycle_on(self):
        self.value(0)

    def cycle_off(self):
        self.value(1)
