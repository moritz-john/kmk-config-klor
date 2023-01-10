import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins # Change this according to your microcontroller: https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder

####
# LED positions used for PEG RGB (per key RGB)
# do not change!
led_pos_polydactyl = [
        18, 13, 12,  6,  5,                  26, 27, 33, 34, 39,
    19, 17, 14, 11,  7,  4,                  25, 28, 32, 35, 38, 40,
    20, 16, 15, 10,  8,  3,                  24, 29, 31, 36, 37, 41,
                     9,  2, 1, 0,    21, 22, 23, 30,
]

led_pos_konrad = [
        17, 12, 11,  5,  4,                  23, 24, 30, 31, 36,
    18, 16, 13, 10,  6,  3,                  22, 25, 29, 32, 35, 37,
    19, 15, 14,  9,  7,  2,                  21, 26, 28, 33, 34, 38,
                     8,  1, 0,           19, 20, 27,
]

led_pos_yubitsume = [
        18, 13, 12,  6,  5,                  24, 25, 31, 32, 37,
        17, 14, 11,  7,  4,                  23, 26, 30, 33, 36,
        16, 15, 10,  8,  3,                  22, 27, 29, 34, 35,
                     9,  2, 1, 0,    19, 20, 21, 28,
]

led_pos_saegewerk = [
        17, 12, 11,  5,  4,                  22, 23, 29, 30, 35,
        16, 13, 10,  6,  3,                  21, 24, 28, 31, 34,
        15, 14,  9,  7,  2,                  20, 25, 27, 32, 33,
                     8,  1, 0,           18, 19, 26,
]

# LED colors for PEG (per key RGB)
# change color here for your specifig KLOR variant

led_display_polydactyl = [
                          [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                                    [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255],   [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_konrad =[
                          [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                                    [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_yubitsume =[
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                      [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255],   [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_saegewerk =[
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                      [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

# def basic_rgb(keyboard, pixels):
#     from kmk.extensions.RGB import RGB

#     rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=pixels, val_limit=50, hue_default=0, sat_default=100, val_default=100,)

#     keyboard.extensions.append(rgb)


# def peg_rgb(keyboard, led_display):
#     from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color

#     rgb_ext = Rgb_matrix(
#         ledDisplay=led_display,
#         split=True,
#         rightSide=False,
#         disable_auto_write=True,
#     )

#     keyboard.extensions.append(rgb_ext)


class KMKKeyboard(_KMKKeyboard):
    def __init__(self, klor_rgb, klor_variant, klor_oled, klor_speaker):
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

        self.setup_oled(klor_oled)
        self.setup_speaker(klor_speaker)
        self.setup_rgb(klor_rgb, klor_variant)

    def setup_oled(self, klor_oled):
        if klor_oled == True:
            from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

            oled_ext = Oled(
                OledData(
                    corner_one={0:OledReactionType.STATIC,1:["Layer"]},
                    corner_two={0:OledReactionType.LAYER,1:["0","1",]},
                    corner_three={0:OledReactionType.LAYER,1:["BASE","RAISE",]},
                    corner_four={0:OledReactionType.LAYER,1:["qwerty","nums",]}
                    ),
                    toDisplay=OledDisplayMode.TXT,
                    flip=True,
            )

            self.extensions.append(oled_ext)


    def setup_speaker(self, klor_speaker):
        if klor_speaker == True:
            import digitalio
            import pwmio
            import time
            from storage import getmount

            drive_name = str(getmount('/').label)

            # Play a startup beep on the left keyboard side:
            if drive_name.endswith('L'):
                buzzer = pwmio.PWMOut(self.buzzer_pin, variable_frequency=True)
                OFF = 0
                ON = 2**15
                buzzer.duty_cycle = ON
                buzzer.frequency = 2000
                time.sleep(0.2)
                buzzer.frequency = 1000
                time.sleep(0.2)
                buzzer.duty_cycle = OFF

    def basic_rgb(self, pixels):
        from kmk.extensions.RGB import RGB

        rgb = RGB(pixel_pin=self.rgb_pixel_pin, num_pixels=pixels, val_limit=50, hue_default=0, sat_default=100, val_default=100,)

        self.extensions.append(rgb)


    def peg_rgb(self, led_display):
        from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color

        rgb_ext = Rgb_matrix(
            ledDisplay=led_display,
            split=True,
            rightSide=False,
            disable_auto_write=True,
        )

        self.extensions.append(rgb_ext)

    def setup_rgb(self, klor_rgb, klor_variant):
        if klor_rgb == 'peg_rgb':
            self.brightness_limit = 0.3

            if klor_variant == 'polydactyl':
                self.led_key_pos = led_pos_polydactyl
                self.num_pixels = len(led_pos_polydactyl)
                self.peg_rgb(led_display_polydactyl)

            if klor_variant == 'konrad':
                self.led_key_pos = led_pos_konrad
                self.num_pixels = len(led_pos_konrad)
                self.peg_rgb(led_display_konrad)

            if klor_variant == 'yubitsume':
                self.led_key_pos = led_pos_yubitsume
                self.num_pixels = len(led_pos_yubitsume)
                self.peg_rgb(led_display_yubitsume)

            if klor_variant == 'saegewerk':
                self.led_key_pos = led_pos_saegewerk
                self.num_pixels = len(led_pos_saegewerk)
                self.peg_rgb(led_display_saegewerk)

        if klor_rgb == 'basic_rgb':

            if klor_variant == 'polydactyl':
                self.basic_rgb(pixels=21)

            if klor_variant == 'konrad':
                self.basic_rgb(pixels=20)

            if klor_variant == 'yubitsume':
                self.basic_rgb(pixels=19)

            if klor_variant == 'saegewerk':
                self.basic_rgb(pixels=18)

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


    # NOQA
    # flake8: noqa
    coord_mapping = [
            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
       12, 13, 14, 15, 16, 17, 23, 49, 43, 42, 41, 40, 39, 38,
               19, 20, 21, 22,         48, 47, 46, 45,
                       24, 25,         51, 50,
    ]
