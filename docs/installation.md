> **Note**
> **Single push reset button:**
> Reboot microcontroller - USB drive is called "CIRCUITPY" or e.g. "KLORL"

> **Note**
> **Double push reset button**: 
> UF2 Bootloader mode - USB drive is called "RPI-RP2"

> **Note**
> This firmware has been tested on **CircuitPython (stable) 7.3.3**
# Installation
## 1) Install CircuitPython
KMK is a keyboard focused layer that sits on top of CircuitPython.
[Follow these steps](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

## 2) Rename your microcontroller
Rename your microcontrollers / USB drives to "KLORL" (for the left keyboard side) and "KLORR" (for the right keyboard side) in order for KMK to figure out which side is which. 

  Follow this tutorial: ["Renaming CIRCUITPY through CircuitPython"](https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy#renaming-circuitpy-through-circuitpython-3014813)

**OR**

- take the [`utilities/rename_klor_left/boot.py`](/utilities/rename_klor_left/boot.py) file and drag it on your **left** microcontroller (currently named: "CIRCUITPY")
- take the [`utilities/rename_klor_right/boot.py`](/utilities/rename_klor_right/boot.py) file and drag it on your **right** microcontroller (currently named: "CIRCUITPY")

After a reboot the microcontroller should appear as "KLORL" and "KLORR" respectively.

## 3) Install KMK 
1) Get [a copy](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip) of KMK from the master branch 
2) Unzip the file and copy the `kmk` folder and the `boot.py` file at the root of the USB drive (override the `boot.py` file used in step 2)
3) Download the `kb.py` and `main.py` files + the `lib` folder from this repository and also copy them onto your USB drive\
You can also find those files in the `klor_kmk_firmware.zip` file from [GitHub releases](https://github.com/moritz-john/kmk-config-klor/releases).
4) Reboot

Repeat those steps for both the left and right microcontroller.

<p>
  <img alt="KLOR KMK logo" src="images/klor_drive.png">
</p>
