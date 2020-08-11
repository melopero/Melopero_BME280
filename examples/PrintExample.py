#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Leonardo La Rocca
"""

import melopero_bme280 as mp
import time

dev = mp.BME280()

dev.set_indoor_navigation_configuration()

try:
    while True:
        print(dev.get_data())
        time.sleep(.5)
except Exception as e:
    print(e)
    dev.close()
