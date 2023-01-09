

def basic_rgb(keyboard, pixels):
    from kmk.extensions.RGB import RGB
    rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=pixels, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
    keyboard.extensions.append(rgb)

# def basic_rgb_konrad():
#     from kmk.extensions.RGB import RGB
#     rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=20, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
#     keyboard.extensions.append(rgb)

# def basic_rgb_yubitsume():
#     from kmk.extensions.RGB import RGB
#     rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=19, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
#     keyboard.extensions.append(rgb)

# def basic_rgb_saegewerk():
#     from kmk.extensions.RGB import RGB
#     rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=18, val_limit=50, hue_default=0, sat_default=100, val_default=100,)
#     keyboard.extensions.append(rgb)
