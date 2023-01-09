import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins # Change this according to your microcontroller: https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder

try:
    from klor_config import klor_rgb, klor_variant
except ImportError:
    pass

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins = self.col_pins,
                row_pins = self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=DiodeOrientation.COL2ROW,
                interval=0.02,  # Debounce time in floating point seconds
                max_events=64
            ),
            RotaryioEncoder(
                pin_a=self.encoder_a,
                pin_b=self.encoder_b,
                # optional
                divisor=2,
            )
        ]
    col_pins = (pins[17], pins[16], pins[15], pins[14], pins[13], pins[12],)
    row_pins = (pins[7], pins[8], pins[9], pins[10],)
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_a = pins[19]
    encoder_b = pins[18]
    SCL = pins[5]
    SDA = pins[4]
    rx = pins[6]
    tx = pins[1]
    buzzer_pin = pins[11]
    rgb_pixel_pin = pins[0]
    if klor_rgb == 'none':
        pass
    elif klor_rgb == 'peg_rgb' and not klor_variant == 'undefined':
        from klor_peg_rgb import klor_brightness_limit
        brightness_limit = klor_brightness_limit
        if klor_variant == 'polydactyl':
            from klor_peg_rgb import led_pos_polydactyl
            led_key_pos = led_pos_polydactyl
            num_pixels = len(led_pos_polydactyl)
        elif klor_variant == 'konrad':
            from klor_peg_rgb import led_pos_konrad
            led_key_pos = led_pos_konrad
            num_pixels = len(led_pos_konrad)
        elif klor_variant == 'yubitsume':
            from klor_peg_rgb import led_pos_yubitsume
            led_key_pos = led_pos_yubitsume
            num_pixels = len(led_pos_yubitsume)
        elif klor_variant == 'saegewerk':
            from klor_peg_rgb import led_pos_saegewerk
            led_key_pos = led_pos_saegewerk
            num_pixels = len(led_pos_saegewerk)
    # NOQA
    # flake8: noqa
    coord_mapping = [
            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
       12, 13, 14, 15, 16, 17, 23, 49, 43, 42, 41, 40, 39, 38,
               19, 20, 21, 22,         48, 47, 46, 45,                
                       24, 25,         51, 50,
    ]




