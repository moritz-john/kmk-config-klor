import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins # Change this according to your microcontroller: https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder


# LED colors for PEG_RGB (per key RGB)
# change the RGB [R, G, B] value for each key you want.
 

rgb = [
                                (18, [85, 0, 255]), (13, [85, 0, 255]), (12, [85, 0, 255]), (6, [85, 0, 255]), (5, [85, 0, 255]),                                                                       (26, [85, 0, 255]), (27, [85, 0, 255]), (33, [85, 0, 255]), (34, [85, 0, 255]), (39, [85, 0, 255]), 
                               
            (19, [85, 0, 255]), (17, [85, 0, 255]), (14, [85, 0, 255]), (11, [85, 0, 255]), (7, [85, 0, 255]), (4, [85, 0, 255]),                                                                       (25, [85, 0, 255]), (28, [85, 0, 255]), (32, [85, 0, 255]), (35, [85, 0, 255]), (38, [85, 0, 255]), (40, [85, 0, 255]),
                                      
            (20, [85, 0, 255]), (16, [85, 0, 255]), (15, [85, 0, 255]), (10, [85, 0, 255]), (8, [85, 0, 255]), (3, [85, 0, 255]),                                                                       (24, [85, 0, 255]), (29, [85, 0, 255]), (31, [85, 0, 255]), (36, [85, 0, 255]), (37, [85, 0, 255]), (41, [85, 0, 255]),
                               
                                                                                             (9, [255, 0, 0]), (2, [85, 100, 0]), (1, [85, 0, 250]), (0, [85, 0, 200]),             (21, [85, 0, 200]), (22, [85, 0, 255]), (23, [85, 100, 0]), (30, [255, 0, 0])     
]

# the possible cuts for the broken of keys of the different KLOR variants.
cuts = {
    "polydactyl": [],
    "konrad": [0, 21],
    "yubitsume": [19, 20, 40, 41],
    "saegewerk": [0, 19, 20, 21, 40, 41]
}

# trim down [R, G, B] contained in the rgb tupple to fit a specifig KLOR variant 
def trim_display(rgb, cut):
    return ([d for (p, d) in rgb if p not in cut])

# trim down the position part of the rgb tupple to fit the specifig KLOR variant
#  
def trim_pos(rgb, cut):
    cut_pos = [p for (p, d) in rgb if p not in cut]
    old_to_new = {old: new for new, old in enumerate(sorted(cut_pos))}
    return [old_to_new[p] for p in cut_pos]

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
            pos = trim_pos(rgb, cuts[klor_variant])
            display = trim_display(rgb, cuts[klor_variant])
            self.led_key_pos = pos
            self.num_pixels = len(pos)
            self.peg_rgb(display)

        if klor_rgb == 'basic_rgb':

            pos = trim_pos(rgb, cuts[klor_variant])
            half_pos = len(pos)/2
            self.basic_rgb(pixels=int(half_pos))

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

