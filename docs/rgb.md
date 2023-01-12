## RGB

>tl;dr: add library to your keyboard, set `klor_rgb = 'basic_rgb' OR 'peg_rgb'`, customize your RGB code and add rgb keycodes to your keymap to control your lighting.
## 1) Add the necessary library: 
In order to use RGB you have to install one library into your keyboards `lib` folder:

You can find the necessary libraries included in the `klor_kmk_firmware.zip` release.\
**or**\
You can download them yourself from here: [adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/)

1) Copy the **file** called `neopixel.mpy` out of your `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD/lib/` folder
2) Paste the file into the `lib` folder on your microcontroller
3) Repeat for your other keyboard half

<p>
  <img alt="OLED lib folder" src="images/rgb_lib.png">
</p>

## 2) Chose your RGB mode:

Afterwards you have to change the variable `klor_rgb` from `none` to either `basic_rgb` **or** `peg_rgb` in your `main.py` file and also set `klor_variant` to your own [KLOR variant](https://github.com/GEIGEIGEIST/klor#layouts):


```python
klor_variant = 'saegewerk' #<- Change this to your own KLOR variant: 'polydactyl', 'konrad', 'yubitsume', 'saegewerk'
klor_rgb     = 'none'      #<- Change this to `basic_rgb` OR `peg_rgb`
klor_oled    = False
klor_speaker = False
```
## 3) "Basic" RGB vs PEG RGB:

If you need to address LEDs individually (so change specific LEDs to a different color) use [`peg_rgb`](http://kmkfw.io/docs/peg_rgb_matrix/) in any other case use the more powerful [`basic_rgb`](http://kmkfw.io/docs/rgb/) implementation.\
*I would recommend going with `basic_rgb`!*

## 4.1) Customize "Basic" RGB:

*You can find the code in your `kb.py` file starting on `line 113`*

```python
rgb = RGB(pixel_pin=self.rgb_pixel_pin, num_pixels=pixels, val_limit=50, hue_default=0, sat_default=100, val_default=20,)
```

Consider changing `hue_default=0-255`, `sat_default=0-255` or `val_default=0-255`.\
Read more about this here: http://kmkfw.io/docs/rgb/#configuration

## 4.2) Customize PEG RGB:

*You can find the code in your `kb.py` file starting on `line 19`*

```python
rgb_data = [
                  [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                            
    [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                            
    [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],                            
                                                            [85, 0, 255], [85, 0, 255], [85, 0, 255], [85, 0, 255],
]
(only showing half of 'rgb_data' for reasons of space)
```
Each `[R, G, B]` square bracket matches a KLOR key as seen in `led_positions` in `line 11`.\
Keep in mind that some KLOR variants have less columnar staggered / thumb keys.\
Adjust `[R, G, B]` with a value between `[0-255, 0-255, 0-255]`.

> **Warning**
> Use RGB Codes e.g.: `[255,55,55]` and **NOT** Color Classes e.g.: `Color.RED`

 ## 5) Add RGB keycodes to your keymap:

 Add some keycodes to your keymap in order to control your RGB lighting e.g.: turn it on or off via `KC.RGB_TOG`

 For `basic_rgb` use [these keycodes](http://kmkfw.io/docs/rgb#keycodes).

 For `peg_rgb` use [these keycodes](http://kmkfw.io/docs/peg_rgb_matrix/#keycodes) (yes, there are only three).