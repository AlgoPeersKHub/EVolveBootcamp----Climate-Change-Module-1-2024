temperature = 0
soil_moisture_level = pins.analog_read_pin(AnalogPin.P0)
soil_moisture_level_in_percentage = 0

def on_forever():
    global soil_moisture_level_in_percentage, temperature, soil_moisture_level
    soil_moisture_level = pins.analog_read_pin(AnalogPin.P0)
    temperature = input.temperature()
    soil_moisture_level_in_percentage = soil_moisture_level / 1023 * 100
    soil_moisture_level_in_percentage_rounded = Math.round(soil_moisture_level_in_percentage
    )
    basic.show_number(soil_moisture_level_in_percentage_rounded)
    serial.write_value("Temp", temperature)
    serial.write_value("Soil Moisture", soil_moisture_level_in_percentage_rounded)
    datalogger.log(datalogger.create_cv("Temp", temperature),
        datalogger.create_cv("Soil Moisture", soil_moisture_level_in_percentage))
    if temperature > 30:
        music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("High Evapotraspiration Rate")
    if soil_moisture_level_in_percentage_rounded <= 30:
        for h in range(4):
            basic.show_icon(IconNames.NO)
            basic.pause(1000)
            basic.show_leds("""
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            """)
        basic.show_string("Very Low Soil Moisture")
        basic.show_string("High Drought")
    elif soil_moisture_level_in_percentage_rounded > 30 and soil_moisture_level_in_percentage_rounded <= 70:
        for m in range(4):
            basic.show_icon(IconNames.DIAMOND)
            basic.pause(1000)
            basic.show_icon(IconNames.COW)
        basic.show_string("Moderate Soil Moisture")
        basic.show_string("Moderate Drought")
    else:
        for l in range(4):
            basic.show_icon(IconNames.GHOST)
            basic.pause(1000)
            basic.show_icon(IconNames.HOUSE)
        basic.show_string("Low Soil Moisture")
        basic.show_string("Low Drought Alert!")

basic.forever(on_forever)
