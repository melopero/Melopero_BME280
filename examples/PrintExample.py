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
        data = dev.get_data()
        print("{:05.2f}°C {:05.2f}Pa {:05.2f}%".format(data['T'], data['P'], data['H'] * 100))
        time.sleep(.5)
except Exception as e:
    print(e)
    dev.close()
