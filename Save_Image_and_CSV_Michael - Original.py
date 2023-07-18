# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:04:30 2018

@author: michael.steib
"""

import visa
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import time
import sys

rm = visa.ResourceManager()
rm.list_resources()

# %%
dc = rm.open_resource('GPIB0::8::INSTR')
dc.write(':TRIG:COUN 1')
print(dc.query("*IDN?"))

FlexDCA = rm.open_resource('GPIB0::7::INSTR')
print(FlexDCA.query("*IDN?"))

FlexDCA.read_termination = '\n'
FlexDCA.write_termination = '\n'
FlexDCA.timeout = 5000

# %%
FlexDCA.write(":DISK:WAV:SAVE:SOUR CHAN4A")

file0 = '"MPW2_'

time.sleep(1)

file = file0 + '.jpg"'

## Setup Acquisition Limit and acquire data
FlexDCA.write(":ACQuire:CDISplay")
FlexDCA.write(":LTESt:ACQuire:CTYPe:WAVeforms 32")
FlexDCA.write(":LTESt:ACQuire:STATe ON")
FlexDCA.write(":ACQuire:RUN")
FlexDCA.write("*OPC?")

time.sleep(4)
FlexDCA.write(":DISK:SIMage:FNAM " + file)
FlexDCA.write(':DISK:SIMage:save; *OPC?')

file = file0 + '.txt"'
FlexDCA.write(":DISK:WAV:FFOR TEXT")
FlexDCA.write(":DISK:WAV:FNAM " + file)
FlexDCA.write(":DISK:WAV:SAVE; *OPC?")

FlexDCA.write(":SYSTem:GTLocal")
