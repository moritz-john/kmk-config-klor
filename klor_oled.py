def oled_code(keyboard):
    from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
    oled_ext = Oled(
        OledData(
            corner_one={0:OledReactionType.STATIC,1:["Layer"]},
            corner_two={0:OledReactionType.LAYER,1:["0","1",]},
            corner_three={0:OledReactionType.LAYER,1:["BASE","RAISE",]},
            corner_four={0:OledReactionType.LAYER,1:["qwerty","nums",]}
            ),
            toDisplay=OledDisplayMode.TXT,
            flip=True,
    )
    keyboard.extensions.append(oled_ext)
