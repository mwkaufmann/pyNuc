import os
from enum import IntEnum
import six

INSTALL_URL = "https://github.com/nomego/intel_nuc_led"
NUC_PATH = "/proc/acpi/nuc_led"


def check_installation():
    """ checks if the INTEL_NUC_LEDs are available """
    if not os.path.isfile(NUC_PATH):
        print("cannot find INTEL NUC LEDs in this system!")
        print(
            "please install the INTEL_NUC_LED kernel module to make them available.\r\nFor instructions visit: " + INSTALL_URL)
        raise SystemExit()


def warn_user():
    while True:
        warning = "WARNING, this library has not been tested and might not work!\r\nType: 'ok' to continue: "
        result = six.input(warning)
        if result.lower() == "ok":
            break


class NotInstalledError(Exception):
    pass


class LEDType(IntEnum):
    POWER = 0
    RING = 1
    SKULL = 2
    EYES = 3


class Operation(IntEnum):
    SET_BRIGHTNESS = 0
    SET_BLINK_MODE = 1
    SET_BLINK_RATE = 2
    SET_RED = 3
    SET_GREEN = 4
    SET_BLUE = 5


class Color(IntEnum):
    RED = 3
    GREEN = 4
    BLUE = 5


class BlinkMode(IntEnum):
    SOLID = 0
    BREATHING = 1
    PULSING = 2
    STROBING = 3


class NUCLed(object):

    def __init__(self):
        self.mode = 4  # software mode
        self.set_software_control()

    def set_color(self, r, g, b):
        assert (0 <= r <= 255)
        assert (0 <= g <= 255)
        assert (0 <= b <= 255)
        cmds = [
            "set_indicator_value,{},{},3,{}".format(self.led_id, self.mode, r),
            "set_indicator_value,{},{},4,{}".format(self.led_id, self.mode, g),
            "set_indicator_value,{},{},5,{}".format(self.led_id, self.mode, b),
        ]
        for cmd in cmds:
            self.update_settings(cmd)

    def set_brightness(self, brightness):
        assert (0 <= brightness <= 100)
        cmd = "set_indicator_value,{},{},{},{}".format(self.led_id, self.mode, Operation.SET_BRIGHTNESS, brightness)
        self.update_settings(cmd)

    def set_blink_mode(self, blink_mode):
        assert (0 <= blink_mode <= 3)
        cmd = "set_indicator_value,{},{},{},{}".format(self.led_id, self.mode, Operation.SET_BLINK_MODE, blink_mode)
        self.update_settings(cmd)

    def set_blink_rate(self, rate):
        assert (0 <= rate <= 10)
        cmd = "set_indicator_value,{},{},{},{}".format(self.led_id, self.mode, Operation.SET_BLINK_RATE, rate)
        self.update_settings(cmd)

    def set_software_control(self):
        cmd = "set_indicator,{},{}".format(self.led_id, self.mode)
        self.update_settings(cmd)

    def update_settings(self, settings):
        with open(NUC_PATH, "w") as nuc:
            nuc.write(settings)


class PowerLED(NUCLed):
    def __init__(self):
        self.led_id = LEDType.POWER
        super(PowerLED, self).__init__()


class RingLED(NUCLed):
    def __init__(self):
        self.led_id = LEDType.RING
        super(RingLED, self).__init__()


class SkullLED(NUCLed):
    def __init__(self):
        self.led_id = LEDType.SKULL
        super(SkullLED, self).__init__()


class EyesLED(NUCLed):
    def __init__(self):
        self.led_id = LEDType.EYES
        super(EyesLED, self).__init__()


check_installation()
# warn_user()
