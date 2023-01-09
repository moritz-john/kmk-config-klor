led_display_polydactyl = [
                          [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                                    [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255],   [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_konrad =[
                          [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                                    [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_yubitsume =[
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                                              [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                      [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255],   [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]

led_display_saegewerkt =[
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                                [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
                                                      [85, 0, 255], [85, 0, 255], [85, 0, 255],    [85, 0, 255], [85, 0, 255], [85, 0, 255],
        ]


def peg_rgb_polydactyl(keyboard):
    from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
    rgb_ext = Rgb_matrix(
        ledDisplay=led_display_polydactyl,
        split=True,
        rightSide=False,
        disable_auto_write=True,
    )
    keyboard.extensions.append(rgb_ext)

def peg_rgb_konrad(keyboard):
    from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
    rgb_ext = Rgb_matrix(
        ledDisplay=led_display_konrad,
        split=True,
        rightSide=False,
        disable_auto_write=True,
    )
    keyboard.extensions.append(rgb_ext)

def peg_rgb_yubitsume(keyboard):
    from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
    rgb_ext = Rgb_matrix(
        ledDisplay=led_display_yubitsume,
        split=True,
        rightSide=False,
        disable_auto_write=True,
    )
    keyboard.extensions.append(rgb_ext)

def peg_rgb_saegewerk(keyboard):
    from kmk.extensions.peg_rgb_matrix import Rgb_matrix,Rgb_matrix_data,Color
    rgb_ext = Rgb_matrix(
        ledDisplay=led_display_saegewerkt,
        split=True,
        rightSide=False,
        disable_auto_write=True,
    )
    keyboard.extensions.append(rgb_ext)

klor_brightness_limit = 0.3
