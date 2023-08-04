#!/usr/bin/env python3
"""
Sensor
"""

import board
import mh_z19
from busio import I2C
import adafruit_bme680


class Sensor:
    """Sensor Class"""

    def __init__(self):
        self.mhz19 = mh_z19.read_all()
        self.i2c = I2C(board.SCL, board.SDA)
        self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(self.i2c, debug=False)

        self.temperature_offset = -7.5
        self.bme680.sea_level_pressure = 1013.25

    def get_data(self):
        """Get data from sensors"""

        data = {
            "temperature": self.bme680.temperature + self.temperature_offset,
            "relative_humidity": self.bme680.relative_humidity,
            "humidity": self.bme680.humidity,
            "pressure": self.bme680.pressure,
            "altitude": self.bme680.altitude,
            "gas": self.bme680.gas,
            "co2": self.mhz19["co2"],
        }

        return data