from pyNuc import SkullLED, EyesLED, BlinkMode
import time

skull_led = SkullLED()
eyes_led = EyesLED()

print("Blue skull with strobing red eyes!")

# set skull to solid blue
skull_led.set_brightness(100)
skull_led.set_color(0, 0, 255)
skull_led.set_blink_mode(BlinkMode.SOLID)

# set eyes to strobing in red
eyes_led.set_brightness(100)
eyes_led.set_color(255, 0, 0)
eyes_led.set_blink_rate(5)  # fastest
eyes_led.set_blink_mode(BlinkMode.STROBING)

time.sleep(10)

print("yellow skull with breathing green eyes!")

skull_led.set_brightness(100)
skull_led.set_color(255,255,0)
skull_led.set_blink_mode(BlinkMode.SOLID)

eyes_led.set_brightness(100)
eyes_led.set_color( 0, 255, 0)
eyes_led.set_blink_rate(5) 
eyes_led.set_blink_mode(BlinkMode.BREATHING)

time.sleep(10)

print("white skull with flashing magenta eyes!")

skull_led.set_brightness(100)
skull_led.set_color(255,255,255)
skull_led.set_blink_mode(BlinkMode.SOLID)

eyes_led.set_brightness(100)
eyes_led.set_color( 255, 0, 255)
eyes_led.set_blink_rate(10) 
eyes_led.set_blink_mode(BlinkMode.PULSING)
