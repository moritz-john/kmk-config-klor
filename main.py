import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import Split, SplitType, SplitSide

# fmt: off
# ↓↓↓ EDIT CONFIG HERE ↓↓↓
klor_variant = "saegewerk"  # Options: "polydactyl", "konrad", "yubitsume", "saegewerk"
klor_rgb = "none"           # Options:"basic_rgb", "peg_rgb", "none"
klor_oled = False           # Options: True, False
klor_speaker = False        # Options: True, False
# ↑↑↑ EDIT CONFIG HERE ↑↑↑
# fmt: on

keyboard = KMKKeyboard(klor_rgb, klor_variant, klor_oled, klor_speaker)

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True

# Split Code:
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


# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS
RAISE = KC.MO(1)
LOWER = KC.MO(2)

# Keymap
# fmt: off
keyboard.keymap = [
    [
       #BASE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
        KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N1,  \
        KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MUTE,   KC.MPLY,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N2,  \
                        KC.LCTL,   LOWER,  KC.SPC,   KC.N4,                       KC.N4, KC.BSPC,   RAISE,  KC.ENT,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
    [
       #RAISE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                 KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                       KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,           \
      _______,  KC.TAB, KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT,                     xxxxxxx, KC.MINS,  KC.EQL, KC.LBRC, KC.RBRC, _______,  \
      _______, KC.LCTL,  KC.GRV, KC.LGUI, KC.LALT, xxxxxxx, KC.MUTE,   KC.MPLY, xxxxxxx, xxxxxxx, xxxxxxx, KC.BSLS, KC.QUOT, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,

        # Encoders
        KC.PGUP,  #Left side clockwise
        KC.PGDN,  #Left side counterclockwise
        KC.RIGHT, #Right side clockwise
        KC.LEFT,  #Right side counterclockwise
    ],
    [
       #LOWER
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
               KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                     KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,           \
      _______,  KC.ESC, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx, KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, _______,  \
      _______, KC.CAPS, KC.TILD, xxxxxxx, xxxxxxx, xxxxxxx, KC.MUTE,   KC.MPLY, xxxxxxx, xxxxxxx, xxxxxxx, KC.PIPE,  KC.DQT, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx,  KC.ENT, xxxxxxx,  KC.DEL,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
