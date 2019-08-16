#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import serial

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 19200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 0.5
)

# ser = serial.Serial('/dev/ttyUSB0')
# ser.flushInput()

while True:
    ser_bytes = ser.readline()
    if len(ser_bytes) == 0:
        pass
    else:
        print(ser_bytes)

