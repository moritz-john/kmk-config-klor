print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.handlers.sequences import simple_key_sequence

from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.col_pins = (pins[17], pins[16], pins[15], pins[14], pins[13], pins[12],)
keyboard.row_pins = (pins[7], pins[8], pins[9], pins[10],)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.rx = pins[6]
keyboard.tx = pins[1]

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=keyboard.rx,  # The primary data pin to talk to the secondary device with
    data_pin2=keyboard.tx,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)


keyboard.modules = [split]

# *2 for split keyboards, which will typically manage twice the number of keys
# of one side. Having this N too large will have no impact (maybe slower boot..)
N = len(keyboard.col_pins) * len(keyboard.row_pins) * 2

keyboard.coord_mapping = list(range(N))

layer = []

for i in range(N):
    c, r = divmod(i, 100)
    d, u = divmod(r, 10)
    layer.append(
        simple_key_sequence(
            (
                getattr(KC, 'N' + str(c)),
                getattr(KC, 'N' + str(d)),
                getattr(KC, 'N' + str(u)),
                KC.SPC,
            )
        )
    )
keyboard.keymap = [layer]

if __name__ == '__main__':
    keyboard.go()
