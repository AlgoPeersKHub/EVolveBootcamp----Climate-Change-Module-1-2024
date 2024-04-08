
temperature_reading_in_daytime = 0

def on_forever():
    global temperature_reading_in_daytime
    temperature_reading_in_daytime = input.temperature()
    basic.show_number(temperature_reading_in_daytime)
    serial.write_value("temp", temperature_reading_in_daytime)
    datalogger.log(datalogger.create_cv("temp", temperature_reading_in_daytime))
    if temperature_reading_in_daytime == 30:
        # Green Led - Temp is below the average daily temperature.
        pins.digital_write_pin(DigitalPin.P0, 0)
        # Yellow Led - Temp is average daily temperature.
        pins.digital_write_pin(DigitalPin.P1, 1)
        # Red Led - Temp is above average daily temperature.
        pins.digital_write_pin(DigitalPin.P2, 0)
    elif temperature_reading_in_daytime > 30:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        music.play(music.builtin_playable_sound_effect(soundExpression.mysterious),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_icon(IconNames.NO)
        basic.show_string("Possible heatwave in the days ahead!")
    else:
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
basic.forever(on_forever)
