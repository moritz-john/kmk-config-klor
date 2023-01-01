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


keyboard = KMKKeyboard()
drive_name = str(getmount('/').label)

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


# # OLED code starts here ---
# from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
# oled_ext = Oled(
#     OledData(
#         corner_one={0:OledReactionType.STATIC,1:["Layer"]},
#         corner_two={0:OledReactionType.LAYER,1:["0","1",]},
#         corner_three={0:OledReactionType.LAYER,1:["BASE","RAISE",]},
#         corner_four={0:OledReactionType.LAYER,1:["qwerty","nums",]}
#         ),
#         toDisplay=OledDisplayMode.TXT,
#         flip=True,
# )
# keyboard.extensions.append(oled_ext)
# # OLED code ends here ---


# # Basic RGB code starts here --
# from kmk.extensions.RGB import RGB
# rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
# keyboard.extensions.append(rgb)
# # Basic RGB code ends here --


# Buzzer code starts here ---
# Play a startup beep on the left keyboard side:
if drive_name.endswith('L'):
    buzzer = pwmio.PWMOut(keyboard.buzzer_pin, variable_frequency=True)
    OFF = 0
    ON = 2**15
    buzzer.duty_cycle = ON
    buzzer.frequency = 2000
    time.sleep(0.2)
    buzzer.frequency = 1000
    time.sleep(0.2)
    buzzer.duty_cycle = OFF
# Buzzer code ends here ---


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

