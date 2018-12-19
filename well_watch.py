import utime
from machine import Pin, RTC, Timer
import network
from relays import Relay
from pressure_level import PressureLevel
from flow_sensor import FlowSensor


def setup_network():
    wlan = network.WLAN(network.STA_IF) # create station interface
    wlan.active(True)                   # activate the interface
    wlan.scan()                         # scan for access points
    wlan.isconnected()                  # check if the station is connected to an AP
    wlan.connect('viennabackup', 'deadface01')  # connect to an AP
    wlan.config('mac')                  # get the interface's MAC adddress
    wlan.ifconfig()                     # get the interface's IP/netmask/gw/DNS addresses


def main():
    setup_network()

    inflow = FlowSensor(12, 0.24)
    outflow = FlowSensor(39, 0.25)
    well_relay = Relay(33)
    misc_relay = Relay(32)
    tank_level = PressureLevel(3)

    led = Pin(2, Pin.OUT)
    enabled = False
    while True:
        if enabled:
            led.off()
        else:
            led.on()
        utime.sleep_ms(1000)
        enabled = not enabled


if __name__ == '__main__':
    main()
