import time

import board
import random
import neopixel
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation import helper
from adafruit_led_animation.color import RED, GREEN, BLUE, PURPLE, AMBER, JADE

# Define fixed parameters
BRIGHTNESS = 0.8
BOARD_PIN = board.GP0
NUM_PIXELS = 50

# Create pixel object
pixels = neopixel.NeoPixel(
    BOARD_PIN,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    pixel_order=neopixel.RGB,
    auto_write=False,
)

# pixelmaps
pixel_wing_vertical = helper.PixelMap.vertical_lines(
    pixels, 8, 6, helper.horizontal_strip_gridmap(6, alternating=False)
)
pixel_wing_horizontal = helper.PixelMap.horizontal_lines(
    pixels, 8, 6, helper.horizontal_strip_gridmap(8, alternating=False)
)

# Setup color
def getRandomColor():
    return random.choice([RED, GREEN, BLUE, PURPLE, AMBER, JADE])

# Setup animations
comet = Comet(pixels, speed=0.02, tail_length=48, bounce=True, color=getRandomColor())
chase = Chase(pixels, speed=0.1, color=getRandomColor())
rainbow_comet = RainbowComet(pixels, 0.02, tail_length=40, bounce=True)
rainbow_chase = RainbowChase(pixels, 0.1)
rainbow_sparkle = RainbowSparkle(pixels, speed=0.1, num_sparkles=15)

comet_v = Comet(pixel_wing_vertical, speed=0.1, color=getRandomColor(), tail_length=8, bounce=True)
comet_h = Comet(pixel_wing_horizontal, speed=0.1, color=getRandomColor(), tail_length=6, bounce=True)

rainbow_chase_v = RainbowChase(
    pixel_wing_vertical, speed=0.1, size=3, spacing=2, step=8
)

rainbow_chase_h = RainbowChase(
    pixel_wing_horizontal, speed=0.1, size=6, spacing=2, step=8
)

rainbow_comet_v = RainbowComet(
    pixel_wing_vertical, speed=0.1, tail_length=7, bounce=True
)

# Define sequence of animations
animations = AnimationSequence(
    #comet,
    rainbow_comet,
    #chase,
    rainbow_chase,
    rainbow_sparkle,
    #comet_v,
    #comet_h,
    rainbow_chase_v,
    rainbow_chase_h,
    #rainbow_comet_v,
    advance_interval=20,
    # random_order=True,  # activate for random order
    auto_clear=True       # Clear the pixels between animations
)

while True:
    animations.animate()

