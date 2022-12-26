print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.handlers.sequences import simple_key_sequence

from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.col_pins = (board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D21)
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.TX,  # Second uart pin to allow 2 way communication
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
