import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import Split, SplitType, SplitSide
try:
    from klor_config import klor_variant, klor_rgb
except ImportError:
    pass

### CHANGE CONFIG HERE
klor_oled = False                # True
klor_speaker = False            # False

keyboard = KMKKeyboard(klor_oled, klor_speaker)

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())


# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True

# Split code starts here ---
split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=keyboard.rx,  # The primary data pin to talk to the secondary device with
    data_pin2=keyboard.tx,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
keyboard.modules.append(split)
# Split code ends here ---


# RGB:
if klor_rgb == 'none':
    pass
# basic rgb
elif klor_rgb == 'basic_rgb' and not klor_variant == 'undefined':
    from klor_basic_rgb import basic_rgb
    if klor_variant == 'polydactyl':
        basic_rgb(keyboard, pixels=21)
    elif klor_variant == 'konrad':
        basic_rgb(keyboard, pixels=20)
    elif klor_variant == 'yubitsume':
        basic_rgb(keyboard, pixels=19)
    elif klor_variant == 'saegewerk':
        basic_rgb(keyboard, pixels=18)
# peg rgb
elif klor_rgb == 'peg_rgb' and not klor_variant == 'undefined':
    if klor_variant == 'polydactyl':
        from klor_peg_rgb import peg_rgb_polydactyl
        peg_rgb_polydactyl(keyboard)
    elif klor_variant == 'konrad':
        from klor_peg_rgb import peg_rgb_konrad
        peg_rgb_konrad(keyboard)
    elif klor_variant == 'yubitsume':
        from klor_peg_rgb import peg_rgb_yubitsume
        peg_rgb_yubitsume(keyboard)
    elif klor_variant == 'saegewerk':
        from klor_peg_rgb import peg_rgb_saegewerk
        peg_rgb_saegewerk(keyboard)

elif klor_rgb == 'basic_rgb' or 'peg_rgb' and klor_variant == 'undefined':
    print:("Make sure the define your KLOR variant in the 'klor_variant' variable.")


# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS
RAISE = KC.MO(1)

# Keymap
keyboard.keymap = [
    [
       #BASE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
        KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
        KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MUTE,   KC.MPLY,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                          KC.N1,  KC.SPC,   KC.N3,   KC.N4,                       KC.N4,   KC.N3,   RAISE,   KC.N1,

        # Encoders
        KC.AUDIO_VOL_UP,     #Left side counterclockwise
        KC.AUDIO_VOL_DOWN,   #Left side clockwise
        KC.MEDIA_PREV_TRACK, #Right side counterclockwise
        KC.MEDIA_NEXT_TRACK, #Right side clockwise
    ],
    [
       #RAISE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                 KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                       KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,         \
        KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
        KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MUTE,   KC.MPLY,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                          KC.N1, _______,   KC.N3,   KC.N4,                       KC.N4,   KC.N3, xxxxxxx,   KC.N1,

        # Encoders
        KC.AUDIO_VOL_UP,     #Left side counterclockwise
        KC.AUDIO_VOL_DOWN,   #Left side clockwise
        KC.MEDIA_PREV_TRACK, #Right side counterclockwise
        KC.MEDIA_NEXT_TRACK, #Right side clockwise
    ],
]


if __name__ == '__main__':
    keyboard.go()

