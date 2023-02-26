---
title: Setup RGB
description: How to setup RGB on your KLOR
hide:
# Hide navigation bar on left side
  - navigation
---

!!! tip "tl;dr"
    Add library to your keyboard drive, set `:::py klor_rgb = "basic_rgb"` **or** `:::py "peg_rgb"`, customize your RGB code and add RGB keycodes to your keymap to control your lighting.
## Add the necessary library
In order to use RGB you have to install one library into your keyboard's `'lib'` folder:

=== "Github Releases"
    You can find the necessary library included in the [`klor_kmk_firmware.zip` release](https://github.com/moritz-john/kmk-config-klor/releases)

    1. Copy the **file** called `'neopixel.mpy'` out of `'klor_kmk_firmware/lib'`  
    2. Paste the file into the `'lib'` folder on your microcontroller  
    3. Repeat for your other keyboard half  

=== "Locate & exctract files yourself" 
    Download: [adafruit-circuitpython-bundle-8.x-mpy-YYYYMMDD.zip](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)

    1. Copy the **file** called `'neopixel.mpy'` out of `'adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD/lib/'`  
    2. Paste the file into the `'lib'` folder on your microcontroller  
    3. Repeat for your other keyboard half  

![Image title](images/rgb_lib.png){ width="700"}

## Chose your RGB mode
Afterwards you have to change the variable `klor_rgb` from `"none"` to either `"basic_rgb"` **or** `"peg_rgb"` in your [`main.py`](https://github.com/moritz-john/kmk-config-klor/blob/master/firmware/main.py) file and also set `klor_variant` to your own [KLOR variant](https://github.com/GEIGEIGEIST/klor#layouts):

```python
klor_variant = "saegewerk" #<- Change this to your own KLOR variant: "polydactyl", "konrad", "yubitsume", "saegewerk"
klor_rgb = "none"  #<- Change this to "basic_rgb" OR "peg_rgb"
klor_oled = False
klor_speaker = False
```
### Basic RGB vs PEG RGB
If you need to address LEDs individually (so change specific LEDs to a different color) use [`peg_rgb`](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/peg_rgb_matrix.md) in any other case use the more powerful [`basic_rgb`](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md) implementation.  
*I would recommend going with `basic_rgb`.*

## Customize your RGB experience
### Basic RGB

*You can find the code in your [`kb.py`](https://github.com/moritz-john/kmk-config-klor/blob/master/firmware/kb.py) file:*

```py title="kb.py"
--8<-- 'firmware/kb.py:rgb'
```

Consider changing `hue_default`, `sat_default` or `val_default`. Use a value in the range `0-255`.  
Read more about the possible configuration options [HERE](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md#configuration).

You can also change the colors and much more at runtime via [RGB keycodes](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md#keycodes).

### PEG RGB

*You can find the code in your [`kb.py`](https://github.com/moritz-john/kmk-config-klor/blob/master/firmware/kb.py) file:*

```py title="kb.py"
--8<-- 'firmware/kb.py:rgbdata'
```

Each `[R, G, B]` list matches a KLOR key as seen in `led_positions`. Keep in mind that some KLOR variants have less keys.  
Adjust `[R, G, B]` with a value between `[0-255, 0-255, 0-255]`.

___

Instead of using **RGB codes**, such as `[255,55,55]`, one can use **Color classes** like `Color.RED` or `Color.GREEN`.  
Uncomment `:::py from kmk.extensions.peg_rgb_matrix import Color` in `kb.py` (by removing the `#` infront of it) to activate this feature.  
[HERE](https://github.com/KMKfw/kmk_firmware/blob/master/kmk/extensions/peg_rgb_matrix.py#L10) is a list of predefined color names.

It is possible to mix and match RGB codes with Color classes e.g.:

```py title="Example: RGB codes mixed with Color classes"
rgb_data = [
    Color.BLUE, [0, 255, 128], Color.RED, #[...]
]
```

You **can't** adjust colors at runtime with `peg_rgb` via keycodes.

## Add RGB keycodes to your keymap
Add some keycodes to your keymap in order to control your RGB lighting e.g.: turn it on or off via ++rgbtog++

=== "Basic RGB"
    Use [these keycodes](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/rgb.md#keycodes).

=== "PEG RGB"
    Use [these keycodes](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/peg_rgb_matrix.md#keycodes) (yes, there are only three).