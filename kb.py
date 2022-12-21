import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner(s)
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins = self.col_pins,
                row_pins = self.row_pins,
            ),
            RotaryioEncoder(
                pin_a=self.encoder_a,
                pin_b=self.encoder_b,
            )
        ]
    col_pins = (board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D21)
    row_pins = (board.D5, board.D6, board.D7, board.D8)
    diode_orientation = DiodeOrientation.COL2ROW
    encoder_a = board.A3
    encoder_b = board.A2
    # NOQA
    # flake8: noqa
    coord_mapping = [
            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
       12, 13, 14, 15, 16, 17, 23, 49, 43, 42, 41, 40, 39, 38,
               19, 20, 21, 22,         48, 47, 46, 45,                
                       24, 25,         51, 50,
    ]

#2)
#            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
#        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
#       12, 13, 14, 15, 16, 17,         43, 42, 41, 40, 39, 38,
#               19, 20, 21, 22, 23, 49, 48, 47, 46, 45,                
#                       24, 25,         51, 50,

#1)
#            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
#        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
#       12, 13, 14, 15, 16, 17,         43, 42, 41, 40, 39, 38,
#           19, 20, 21, 22, 23,         49, 48, 47, 46, 45,                
#                       24, 25,         51, 50,





