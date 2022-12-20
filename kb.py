import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D21)
    row_pins = (board.D5, board.D6, board.D7, board.D8)
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_pin_0 = board.A2
    encoder_pin_1 = board.A3
    # NOQA
    # flake8: noqa
    coord_mapping = [
            1,  2,  3,  4,  5,         29, 28, 27, 26, 25,
        6,  7,  8,  9, 10, 11,         35, 34, 33, 32, 31, 30,
       12, 13, 14, 15, 16, 17, 23, 47, 41, 40, 39, 38, 37, 36,
               19, 20, 21, 22,         46, 45, 44, 43,
    ]






