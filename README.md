<p align="center">
  <img alt="KLOR KMK logo" width="500" src="docs/images/klor_kmk.svg">
</p>


# KLOR Keyboard
> KLOR is 36-42 keys column-staggered split keyboard. It supports encoders, OLED displays, the SplitKB tenting puck and four different layouts, through break off parts.

Hardware Availability: [PCB & Case Source](https://github.com/GEIGEIGEIST/klor)


### Installation:
[Install CircuitPython, rename microcontroller, install KMK](docs/installation.md) + `kb.py` & `main.py`


### Microcontroller support:
`kb.py` is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `kb.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```python
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```

### OLED support:
[Additional steps in order for the OLEDs to work.](docs/oled.md)


### Modules/extensions enabled by default:
- [Split](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/split_keyboards.md)
- [Layers](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/layers.md)
- [Media Keys](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/media_keys.md)
- [OLED](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/peg_oled_display.md) *comment the code in `main.py` out if you are not using OLEDs*
- [Encoders](https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/scanners.md#rotary-encoder-scanners) *working on both halfes via Rotary Encoder Scanners!*
- Buzzer / Speaker (via custom code)


___
### Not yet implemented:

- LED support (my KLOR does not use LEDs)
- Haptic feedback
- Pixart Paw3204 trackball

