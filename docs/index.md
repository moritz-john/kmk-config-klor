---
hide:
# Hide navigation bar on left side
  - navigation
---

# KMK Firmware for KLOR Keyboard

!!! info
    `main.py` & `kb.py` only represent a basic framework.  
    Adjust the keymap to your liking and enable RGB & OLED support if needed.

<figure markdown>
  ![Image title](docs/../images/klor_kmk.svg){ width="800" }
  <figcaption></figcaption>
</figure>



## Setup
### Installation
[Install CircuitPython, rename microcontroller, install KMK](docs/installation.md) + `kb.py`, `main.py` & `lib` (if you plan on using OLEDs or RGB)

### Microcontroller support
`kb.py` is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `kb.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```python
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```
### Optional
#### OLED Support
[Additional steps required for OLED support.](docs/oled.md)

#### RGB support
[Additional steps required for RGB support.](docs/rgb.md)

#### Hide device storage by default
If you want to hide your keyboard from showing up as a USB storage [follow these steps](docs/hide_device_storage.md).

!!! warning "Reset button"
    **Single push reset button:**  
    *Reboot microcontroller* - USB drive is called "CIRCUITPY" or e.g. "KLORL"  
    **Double push reset button:**  
    *UF2 Bootloader mode* - USB drive is called "RPI-RP2"
