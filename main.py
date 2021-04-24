import time

from random import randrange
from typing import List
from openrgb import OpenRGBClient
from openrgb.utils import DeviceType

from colors import *

# need to provide
LED_SIZE = 24

client = OpenRGBClient()

client.clear()  # Turns everything off

motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
motherboard.zones[1].resize(LED_SIZE)

keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0].zones[0]
KEYBOARD_SIZE = len(keyboard.colors)


class Effects(object):

    @staticmethod
    def rainbow():
        motherboard.set_mode('Rainbow')

    @staticmethod
    def spectrum():
        motherboard.set_mode('Spectrum Cycle')

    @staticmethod
    def fire():
        motherboard.set_mode('Direct')
        while True:

            motherboard.zones[1].set_colors([RGBColor(255, randrange(0, 40), 0) for _ in range(24)])
            keyboard.set_colors([RGBColor(255, randrange(0, 80), 0) for _ in range(KEYBOARD_SIZE)])

            time.sleep(0.1)

    @classmethod
    def red_snake(cls):
        motherboard.set_mode('Direct')
        template = [red, red, blue, blue, blue, red]*4
        cls.circular(template)

    @staticmethod
    def circular(template: List[RGBColor]):
        while True:
            motherboard.zones[1].set_colors(template)
            template = template[-1:] + template[:-1]
            time.sleep(0.1)


if __name__ == "__main__":
    keyboard.set_color(off)
    Effects.red_snake()
