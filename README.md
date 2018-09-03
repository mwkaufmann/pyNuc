# pyNuc
let's you control the LEDs from INTEL NUCs (linux only)

**WARNING: THIS IS WORK IN PROGRESS**

It does this by providing a simple wrapper for this dynamic linux library: https://github.com/nomego/intel_nuc_led/blob/master/README.md


## Installation
Please install the following library: https://github.com/nomego/intel_nuc_led/blob/master/README.md

## Usage
Usage is quite simple:

    from pyNuc import SkullLED, EyesLED, BlinkMode
    
    skull_led = SkullLED()
    eyes_led = EyesLED()

    # set skull to solid blue
    skull_led.set_brightness(100)
    skull_led.set_color(0,0,255)
    skull_led.set_blink_mode(BlinkMode.SOLID)

    # set eyes to strobing in red
    eyes_led.set_brightness(100)
    skull_led.set_color(255,0,0)
    skull_led.set_blink_rate(1) # fastest
    skull_led.set_blink_mode(BlinkMode.STROBING)

