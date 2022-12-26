import board
import digitalio

import pwmio
import time

from storage import getmount

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins

keyboard = KMKKeyboard()
layers_ext = Layers()
media = MediaKeys()
name = str(getmount('/').label)


split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=keyboard.rx,  # The primary data pin to talk to the secondary device with
    data_pin2=keyboard.tx,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.modules = [split, layers_ext,]
keyboard.extensions = [media,]


# OLED code starts here ---
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3",]},
        corner_three={0:OledReactionType.LAYER,1:["BASE","LOWER","RAISE",]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted",]}
        ),
        toDisplay=OledDisplayMode.TXT,
        flip=True,
)
keyboard.extensions.append(oled_ext)
# OLED code ends here ---



if name.endswith('L'):
    buzzer = pwmio.PWMOut(keyboard.buzzer_pin, variable_frequency=True)
    OFF = 0
    ON = 2**15
    buzzer.duty_cycle = ON
    buzzer.frequency = 2000
    time.sleep(0.2)
    buzzer.frequency = 1000
    time.sleep(0.2)
    buzzer.duty_cycle = OFF


# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS
LOWER = KC.MO(1)
RAISE = KC.MO(2)

# Keymap
keyboard.keymap = [
    [
       #BASE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
        KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
        KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MUTE,   KC.MPLY,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                          KC.N1,   LOWER,   KC.N3,   KC.N4,                       KC.N4,   KC.N3,   RAISE,   KC.N1,

        # Encoders
        KC.AUDIO_VOL_UP,     #Left side counterclockwise
        KC.AUDIO_VOL_DOWN,   #Left side clockwise
        KC.MEDIA_PREV_TRACK, #Right side counterclockwise
        KC.MEDIA_NEXT_TRACK, #Right side clockwise
    ],
    [
       #LOWER       |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                         KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
               KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
               KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MPRV,   KC.MNXT,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                                 KC.N1, _______,   KC.N3,   KC.N4,                       KC.N4,   KC.N3,  KC.SPC,   KC.N1,
        # Encoders
        KC.AUDIO_VOL_UP,     #Left side counterclockwise
        KC.AUDIO_VOL_DOWN,   #Left side clockwise
        KC.MEDIA_PREV_TRACK, #Right side counterclockwise
        KC.MEDIA_NEXT_TRACK, #Right side clockwise
    ],
    [
       #RAISE       |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                         KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
               KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
               KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MPRV,   KC.MNXT,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                                 KC.N1, _______,   KC.N3,   KC.N4,                       KC.N4,   KC.N3, _______,   KC.N1,
        # Encoders
        KC.AUDIO_VOL_UP,     #Left side counterclockwise
        KC.AUDIO_VOL_DOWN,   #Left side clockwise
        KC.MEDIA_PREV_TRACK, #Right side counterclockwise
        KC.MEDIA_NEXT_TRACK, #Right side clockwise
    ],
]


if __name__ == '__main__':
    keyboard.go()

