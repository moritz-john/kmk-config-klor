<p align="center">
  <img alt="KLOR KMK logo" width="500" src="docs/images/klor_kmk.svg">
</p>


# KLOR Keyboard
> KLOR is 36-42 keys column-staggered split keyboard. It supports encoders, OLED displays, the SplitKB tenting puck and four different layouts, through break off parts.

Hardware Availability: [PCB & Case Source](https://github.com/GEIGEIGEIST/klor)

`main.py` & `kb.py` only represents a basic framework.\
Adjust the keymap to your liking and enable RGB & OLED support if needed.
### Installation:
[Install CircuitPython, rename microcontroller, install KMK](docs/installation.md) + `kb.py` & `main.py` (+ `lib` if you plan to use OLEDs or RGB)


### Microcontroller support:
`kb.py` is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `kb.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```python
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```

### OLED support:
[Additional steps in order for the OLEDs to work.](docs/oled.md)

### RGB support:
[Additional steps in order for RGB to work.](docs/rgb.md)

### Hide device storage by default
If you want to hide your keyboard from showing up as a USB storage [follow these steps](docs/hide_device_storage.md).

___
### Modules/extensions implemented:
- [Split](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md)
- [Layers](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/layers.md)
- [Media Keys](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/media_keys.md)
- [OLED](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/peg_oled_display.md) *disabled by default*
- [RGB](http://kmkfw.io/docs/rgb) *disabled by default*
- [Encoders](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md#rotary-encoder-scanners) *working on both halfes via Rotary Encoder Scanners!*
- Buzzer / Speaker (via custom code)

### Not implemented:
- Haptic feedback
- Pixart Paw3204 trackball


### Prior art / thanks to:

The people behind the [Lunakey Pico](https://github.com/KMKfw/kmk_firmware/blob/master/boards/lunakey_pico/README.md), [Lulu](https://github.com/KMKfw/kmk_firmware/tree/master/boards/boardsource/Lulu), [w3by2](https://github.com/wlard/keyboards/tree/main/w3by2%20-%20pico) and [Sofle V2](https://github.com/KMKfw/kmk_firmware/tree/master/boards/sofle/sofleV2) KMK firmware, regicidal plutophage, @janjan and @manna-harbour.
