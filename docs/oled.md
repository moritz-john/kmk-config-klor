# OLED

>tl;dr: add libraries to your keyboard, set `klor_oled = True` and customize your OLED text
## 1) Add the necessary libraries: 
In order to use OLEDs you have to install two libraries into your keyboards `lib` folder:

You can find the necessary libraries included in the `klor_kmk_firmware.zip` release.\
**or**\
You can download them yourself from here: [adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)

1) Copy the **folder** called `adafruit_display_text` and the **file** called `adafruit_displayio_ssd1306.mpy` out of your `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD/lib/` folder
2) Paste both file & folder into the `lib` folder on your microcontroller
3) Repeat for your other keyboard half

<p>
  <img alt="OLED lib folder" src="images/oled_lib.png">
</p>

## 2) Activate the OLED code:
Afterwards you have to change the variable `klor_oled` from `False` to `True` in your [`main.py`](../main.py) file:

```python
klor_variant = 'saegewerk'
klor_rgb     = 'none'
klor_oled    = False       #<- Change this to True
klor_speaker = False
```

## 3) Customize your OLED text:
When you add more layers to your keymap - also add them to this part your OLED code e.g.:

*You can find the code in your [`kb.py`](../kb.py) file starting on `line 76`*
```python
corner_one={0:OledReactionType.STATIC,1:["Layer"]},
corner_two={0:OledReactionType.LAYER,1:["0","1","2",]},
corner_three={0:OledReactionType.LAYER,1:["BASE","RAISE","TESTLAYER",]},
corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","tested",]}
```

