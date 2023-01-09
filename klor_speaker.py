def speaker_code(keyboard):
    import digitalio
    import pwmio
    import time
    from storage import getmount

    drive_name = str(getmount('/').label)
    # Play a startup beep on the left keyboard side:
    if drive_name.endswith('L'):
        buzzer = pwmio.PWMOut(keyboard.buzzer_pin, variable_frequency=True)
        OFF = 0
        ON = 2**15
        buzzer.duty_cycle = ON
        buzzer.frequency = 2000
        time.sleep(0.2)
        buzzer.frequency = 1000
        time.sleep(0.2)
        buzzer.duty_cycle = OFF
