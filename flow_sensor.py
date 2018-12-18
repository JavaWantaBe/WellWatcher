from machine import Pin
import time


class FlowSensor(Pin):
    def __init__(self, pin: int, rate: float):
        super().__init__(id=pin, mode=self.IN)
        self.irq(trigger=self.IRQ_RISING, handler=self._register_flow)
        self.__rate = rate
        self.__flow_total = 0
        self.__flow_per_min = 0

    def _register_flow(self, p):
        self.__flow_total += 1

    @property
    def flow_rate(self) -> float:
        return self.__rate

    @property
    def flow_total(self) -> float:
        return self.__flow_total

    @property
    def flow_per_minute(self) -> float:
        return self.__flow_per_min



