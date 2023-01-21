---
title: Home
description: Start using the KMK Klor firmware
hide:
# Hide navigation bar on left side
  - navigation
---

![KLOR_KMK_LOGO](./images/klor_kmk.svg){ width="400"}

## Installation

Follow these steps:  
1. [Install CircuitPython, rename microcontroller, install KMK](./installation.md)  
2. [Copy `kb.py`, `main.py` & `lib` to your KLOR](./installation.md)

!!! info
    `main.py` & `kb.py` only represent a basic framework.  
    Adjust the keymap to your liking and enable RGB & OLED support if you want.

## Microcontroller support
[`kb.py`](https://github.com/moritz-john/kmk-config-klor/blob/master/kb.py) is designed to work with the **SparkFun Pro Micro RP2040** but you can update this line in `kb.py` to [any supported microcontroller:](https://github.com/KMKfw/kmk_firmware/tree/master/kmk/quickpin/pro_micro)

```python
from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
```

## Optional

### [OLED Setup](./oled.md)
### [RGB Setup](./rgb.md)

### [Hide device storage by default](./hide_device_storage.md)


