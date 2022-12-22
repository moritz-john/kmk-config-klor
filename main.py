import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys 
from kmk.modules.split import Split, SplitType
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()
layers_ext = Layers()
media = MediaKeys()

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.TX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.modules = [split, layers_ext,]
keyboard.extensions = [media,]


# Comment this block out if you are not using OLEDs
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["Layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER,1:["BASE","LOWER","RAISE","ADJUST"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
        ),
        toDisplay=OledDisplayMode.TXT,
        flip=True,
)
keyboard.extensions.append(oled_ext) 


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
    ],
    [  
       #RAISE       |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                         KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,         \
               KC.N1,    KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.N2,  \
               KC.N2,    KC.Z,    KC.X,    KC.C,    KC.V,    KC.B, KC.MPRV,   KC.MNXT,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.N3,  \
                                 KC.N1, _______,   KC.N3,   KC.N4,                       KC.N4,   KC.N3, _______,   KC.N1,  
    ],
]


if __name__ == '__main__':
    keyboard.go()

