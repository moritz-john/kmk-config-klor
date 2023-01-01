## Basic RGB

### 1) Add the necessary library: 
In order to use RGB you have to:

1) Download the [adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD.zip](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/) file
2) Extract it
3) Copy the **file** called `neopixel.mpy` out of your extracted `adafruit-circuitpython-bundle-7.x-mpy-YYYYMMDD/lib/` folder
4) Paste the file `neopixel.mpy` into the `lib` folder on your microcontroller

<p>
  <img alt="OLED lib folder" src="images/rgb_lib.png">
</p>

### 2) Uncomment the RGB code:
Afterwards you have to uncomment the RGB code in your `main.py` file:\
(Remove the `#` as shown below)

```
# Basic RGB code starts here --
from kmk.extensions.RGB import RGB
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
keyboard.extensions.append(rgb)
# Basic RGB code ends here --
```

Consider moving the line: `from kmk.extensions.RGB import RGB` 
to the top of your `main.py file` containing the rest of your `from [...] import [...]` code block.

### 3) Customize the RGB code:

Go into your `kb.py` file and change the line41: `rgb_num_pixels = 21` to match the amount of LEDs per keyboard half.

 e.g. POLYDACTYL -> 21, SAEGEWERK -> 18

 ### 4) Add RGB keycodes to your keymap:

 [Add some keycodes to your keymap](http://kmkfw.io/docs/rgb#keycodes) in order to control your RGB lighting e.g.: turn it on or off via `KC.RGB_TOG`