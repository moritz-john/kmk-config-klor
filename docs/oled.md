# OLED

>tl;dr: add libraries to your keyboard, set `klor_oled = True` and customize your OLED text
## 1) Add the necessary libraries
In order to use OLEDs you have to install two libraries into your keyboard's `'lib'` folder:

You can find the necessary libraries included in the `klor_kmk_firmware.zip` release.\
**or**\
You can download them yourself from here: [adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)

1) Copy the **folder** called `adafruit_display_text` and the **file** called `adafruit_displayio_ssd1306.mpy` out of your `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD/lib/` folder
2) Paste both file & folder into the `'lib'` folder on your microcontroller
3) Repeat for your other keyboard half

<p>
  <img alt="OLED lib folder" src="images/oled_lib.png">
</p>

## 2) Activate the OLED code
Afterwards you have to change the variable `klor_oled` from `False` to `True` in your [`main.py`](../main.py) file:

```python
klor_variant = "saegewerk"
klor_rgb = "none"         
klor_oled = False          #<- Change this to True
klor_speaker = False      
```

## 3) Customize your OLED text
When you add more layers to your keymap, also add them to this part your OLED code e.g.:

*You can find the code in your [`kb.py`](../kb.py#L102) file.
```python
            oled_ext = Oled(
                OledData(
                    corner_one={
                        0: OledReactionType.STATIC,
                        1: ["Layer"],
                    },
                    corner_two={
                        0: OledReactionType.LAYER,
                        1: ["0", "1", "2", "3"],
                    },
                    corner_three={
                        0: OledReactionType.LAYER,
                        1: ["BASE", "RAISE", "LOWER", "TESTLAYER"],
                    },
                    corner_four={
                        0: OledReactionType.LAYER,
                        1: ["qwerty", "nums", "sym", "test"],
                    },
                ),
                toDisplay=OledDisplayMode.TXT,
                flip=True,
                # oHeight=64,
            ) 
```

## 4) Possible Tweaks

The `SSD1306 128x64 pixel OLED Displays` is not offically supported by KMK, only the `128x32 pixel` version is.

If you want to display photos on your OLED as per [this instructions](http://kmkfw.io/docs/peg_oled_display#photos) you might need to uncomment `# oHeight=64,` in the OLED code block. 

> **Note**
> Displaying photos on the OLED has not been tested and might require additonal code changes.

If you uncomment `# oHeight=64,` while displaying [text](http://kmkfw.io/docs/peg_oled_display#text) the font becomes smaller, so you can display more words, but everything is moved to the top left corner. 