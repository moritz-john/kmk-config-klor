import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
layers_ext = Layers()
encoder_handler = EncoderHandler()
media = MediaKeys()

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.TX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.col_pins = (board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D21)
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler.pins = ((board.A3, board.A2, None, False),)

keyboard.modules = [split, layers_ext, encoder_handler]
keyboard.extensions = [media]


# Is coord_mapping even needed? Keyboard works fine without this part.
coord_mapping = [
     1,  2,  3,  4,  5,          29, 28, 27, 26, 25,
     7,  8,  9, 10, 11,          35, 34, 33, 32, 31,
    13, 14, 15, 16, 17,          41, 40, 39, 38, 37,
            19, 20, 21, 23,  47, 45, 44, 43,
]


# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS
RAISE = KC.MO(1)

# Keymap
keyboard.keymap = [
    [  #Base
        xxxxxxx,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P, xxxxxxx,\
        xxxxxxx,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, xxxxxxx,\
        xxxxxxx,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,        KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, xxxxxxx,\
        xxxxxxx,   KC.N1,   RAISE,   KC.N3, xxxxxxx, KC.MUTE,     KC.RPRN, xxxxxxx,   KC.N6,   RAISE,   KC.N4, xxxxxxx,
       #         THUMBL1, THUBML2, THUMBL3,           ENCODL,      ENCODR,          THUMBR3, THUMBR2, THUMBR1,
       #                                    THUMBL4,                       THUMBR4,                                      --> Those are probably used on Polydactyl and Yubitsume
    ],
    [  #RAISE
        xxxxxxx,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,       KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, xxxxxxx,\
        xxxxxxx,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, xxxxxxx,\
        xxxxxxx,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,        KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, xxxxxxx,\
        xxxxxxx,   KC.N3, _______,   KC.N1, xxxxxxx, KC.MUTE,     KC.RPRN, xxxxxxx,   KC.N4, _______,   KC.N6, xxxxxxx,
    ]
]


# Encoder "keymap"
encoder_handler.map = [ ((KC.VOLU, KC.VOLD),),  # Encoder function on Base layer
                        ((KC.UP, KC.DOWN),),  # Encoder function on Raise layer
                        ]


if __name__ == '__main__':
    keyboard.go()

