<p align="center">
  <img alt="KLOR KMK logo" width="500" src="images/klor_kmk.svg">
</p>


This is a work in progress [KMK firmware](http://kmkfw.io/) for the [KLOR](https://github.com/GEIGEIGEIST/klor) keyboard.

Tested on the KLOR "SAEGEWERK" variant & RP2040 Pro Micro by SparkFun.

## Not yet implemented:

- LED support (because my KLOR does not use LEDs)
- OLED support
- Speaker support
- Haptic feedback
- Pixart Paw3204 trackball

___
## Installation:
Follow the [KMK firmware TL;DR Quick start guide](http://kmkfw.io/docs/Getting_Started/#tldr-quick-start-guide) or the steps bellow:

*Install CircuitPython, rename microcontroller, install KMK + `kb.py` & `main.py`*

#### 1) Install CircuitPython:
[Follow these steps](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

#### 2) Rename your microcontroller
Rename your microcontrollers / USB drives to "KLORL" (for the left keyboard side) and "KLORR" (for the right keyboard side) in order for KMK to figure out which side is which. 

  Follow this tutorial: ["Renaming CIRCUITPY through CircuitPython"](https://learn.adafruit.com/welcome-to-circuitpython/renaming-circuitpy#renaming-circuitpy-through-circuitpython-3014813)

**OR**

- take the `utilities/rename_klor_left/boot.py` file and drag it on your **left** microcontroller (currently named: "CIRCUITPY")
- take the `utilities/rename_klor_right/boot.py` file and drag it on your **right** microcontroller (currently named: "CIRCUITPY")

After a reboot the microcontroller should now appear as "KLORL" and "KLORR" respectively.

#### Install KMK 
1) Get [a copy](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip) of KMK from the master branch 
2) Unzip the file and copy the `kmk` folder and the `boot.py` file at the root of the USB drive (override the `boot.py` file used in step 2)
3) Download the `kb.py` & `main.py` files from this repository and also copy them onto your USB drive
4) Reboot

Repeat those steps for both the left and right microcontroller.

<p>
  <img alt="KLOR KMK logo" src="images/klor_drive.png">
</p>

> :warning: **Single push reset button**: Reboot microcontroller - USB drive is called "CIRCUITPY" or e.g. "KLORL"

> :warning: **Double push reset button**: UF2 Bootloader mode - USB drive is called "RPI-RP2"
___
   
### Coord mapping for other KLOR variants
[This code](http://kmkfw.io/docs/porting_to_kmk/#find-your-coord-mapping) gave me the following coord_map on my "SAEGEWERK" KLOR. You can try it on your KLOR variant with the `utilities/coord_mapping/code.py` file [HERE](utilities/coord_mapping/code.py).

```
1)
LEFT side:            Right side:
001 002 003 004 005   029 028 027 026 025
007 008 009 010 011   035 034 033 032 031
013 014 015 016 017   041 040 039 038 037
019 020 021 023       047 045 044 043

```
I assume the missing coordinates for "Polydactyl", "KONRAD", "Yubitsume" are the following:

```
1) [Left side only as showcase]

XXX = assumption

LEFT side:             
X00 001 002 003 004 005
X06 007 008 009 010 011
X12 013 014 015 016 017
X18 019 020 021 X22 023
```
To match [qmk-config-klor](https://github.com/GEIGEIGEIST/qmk-config-klor/blob/main/klor/klor.h#L33) by @GEIGEIGEIST  I made the following changes:
```
3) [Left side only as showcase]

001-017: columnar staggered keys
019-022: thumb keys
    023: rotary encoder key
024-025: encoder scanners

LEFT side:                   LEFT side:                      LEFT side: 
    001 002 003 004 005  >       001 002 003 004 005      >      001 002 003 004 005             
006 007 008 009 010 011  >   006 007 008 009 010 011      >  006 007 008 009 010 011    
012 013 014 015 016 017  >   012 013 014 015 016 017 023  >  012 013 014 015 016 017 023     
    019 020 021 022 023  >           019 020 021 022      >          019 020 021 022
                         >                                >                  024 025     
```
- removed keys 000 and 013 (not used by the keyboard)
- moved thumb keys inwards
- moved rotary encoder upwards
- added 024-025 to the coord_map needed for the encoder scanners

```
4) Final coord_map for both sides:

    coord_mapping = [
            1,  2,  3,  4,  5,         31, 30, 29, 28, 27,
        6,  7,  8,  9, 10, 11,         37, 36, 35, 34, 33, 32,
       12, 13, 14, 15, 16, 17, 23, 49, 43, 42, 41, 40, 39, 38,
               19, 20, 21, 22,         48, 47, 46, 45,                
                       24, 25,         51, 50,
    ]
```

