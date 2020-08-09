#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Leonardo La Rocca
"""

import ctypes

bme280_api = None
bme280_api = ctypes.CDLL("bme280.so")

#setup api
bme280_api.init_device.argtypes = [ctypes.c_uint8, ctypes.c_uint8]
bme280_api.init_device.restype = ctypes.c_int8
bme280_api.set_oversampling.argtypes = [ctypes.c_uint8, ctypes.c_uint8, ctypes.c_uint8]
bme280_api.set_oversampling.restype = ctypes.c_int8
bme280_api.set_filter_coefficient.argtypes = [ctypes.c_uint8]
bme280_api.set_filter_coefficient.restype = ctypes.c_int8
bme280_api.set_sensor_settings.argtypes = [ctypes.c_uint8]
bme280_api.set_sensor_settings.restype = ctypes.c_int8
#bme280_api.update_data.argtype = None
bme280_api.update_data.restype = ctypes.c_int8
#bme280_api.get_pressure.argtype = None
bme280_api.get_pressure.restype = ctypes.c_float
#bme280_api.get_temperature.argtype = None
bme280_api.get_temperature.restype = ctypes.c_float
#bme280_api.get_humidity.argtype = None
bme280_api.get_humidity.restype = ctypes.c_float


def handle_error_codes(error_code):
    if error_code == BME280.OK:
        return
    elif error_code == BME280.E_NULL_PTR:
        raise Exception("null pointer error")
    elif error_code == BME280.E_DEV_NOT_FOUND:
        raise Exception("device not found error")
    elif error_code == BME280.E_INVALID_LEN:
        raise Exception("invalid length error")
    elif error_code == BME280.E_COMM_FAIL:
        raise Exception("I2C communication error")
    elif error_code == BME280.E_SLEEP_MODE_FAIL:
        raise Exception("SLEEP mode fail error")
    elif error_code == BME280.E_NVM_COPY_FAILED:
        raise Exception("NVM copy failed error")
    else :
        return


class BME280:
    NO_OVERSAMPLING = 0x00
    OVERSAMPLING_1X = 0x01
    OVERSAMPLING_2X = 0x02
    OVERSAMPLING_4X = 0x03
    OVERSAMPLING_8X = 0x04
    OVERSAMPLING_16X = 0x05

    FILTER_COEFF_OFF = 0x00
    FILTER_COEFF_2 = 0x01
    FILTER_COEFF_4 = 0x02
    FILTER_COEFF_8 = 0x03
    FILTER_COEFF_16 = 0x04

    I2C_ADDR_PRIM = 0x76
    I2C_ADDR_SEC = 0x77

    OK = 0
    E_NULL_PTR = -1
    E_DEV_NOT_FOUND = -2
    E_INVALID_LEN = -3
    E_COMM_FAIL = -4
    E_SLEEP_MODE_FAIL = -5
    E_NVM_COPY_FAILED = -6

    OSR_PRESS_SEL = 1
    OSR_TEMP_SEL = 1 << 1
    OSR_HUM_SEL = 1 << 2
    FILTER_SEL = 1 << 3
    STANDBY_SEL = 1 << 4
    ALL_SETTINGS_SEL = 0x1F


    def __init__(self, i2c_address=I2C_ADDR_PRIM, i2c_bus=1):
        error_code = bme280_api.init_device(ctypes.c_uint8(i2c_address), ctypes.c_uint8(i2c_bus))
        handle_error_codes(error_code)

    def set_oversampling(self, pressure_os, temperature_os, humidity_os):
        error_code = bme280_api.set_oversampling(ctypes.c_uint8(pressure_os), ctypes.c_uint8(temperature_os), ctypes.c_uint8(humidity_os))
        handle_error_codes(error_code)

    def set_filter_coefficient(self, filter_coefficient):
        error_code = bme280_api.set_filter_coefficient(ctypes.c_uint8(filter_coefficient))
        handle_error_codes(error_code)

    def set_sensor_settings(self, pressure_sensor_active = True, temperature_sensor_active = True,
                            humidity_sensor_active = True, iir_filter_active = True):
        pass