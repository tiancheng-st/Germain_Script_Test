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

SCOPE_VISA_ADDRESS = "USB0::0x0957::0xBE18::K-86100D-20187::0::INSTR"

def init_DCA():
    rm = visa.ResourceManager()
    rm.list_resources()

    FlexDCA = rm.open_resource(SCOPE_VISA_ADDRESS)
    print(FlexDCA.query("*IDN?"))

    FlexDCA.read_termination = '\n'
    FlexDCA.write_termination = '\n'
    FlexDCA.timeout = 5000

    return FlexDCA

def acquire_csv_and_jpg(FlexDCA, channel, location, filename):
    ## Setup Acquisition Limit and acquire data
    FlexDCA.write(":ACQuire:CDISplay")
    # FlexDCA.write(":LTESt:ACQuire:CTYPe:WAVeforms 2")
    # FlexDCA.write(":LTESt:ACQuire:STATe ON")
    FlexDCA.write(":ACQuire:RUN")
    FlexDCA.write("*OPC?")

    # Waveform
    time.sleep(2)
    FlexDCA.write(":DISK:WAV:FFOR TEXT")
    FlexDCA.write(":DISK:WAV:FNAM " + location + filename + "_waveform.txt\"")
    #print ":DISK:WAV:FNAM " + location + filename + "_waveform.txt\""
    FlexDCA.query(":DISK:WAV:SAVE; *OPC?")

    # Screenshot
    time.sleep(2)
    FlexDCA.write(":DISK:SIMage:FNAM " + location + filename + "_img.jpg\"")
    FlexDCA.query(':DISK:SIMage:save; *OPC?')


###################################################
#                     Main                        #
###################################################

if __name__ == '__main__':
    FlexDCA = init_DCA()

    testname = 'test'
    filename = 'file'
    channel = "FUNCtion1"

    timestamp = time.strftime('%H%M%S_%d%b_')
    path = "\"" + 'D:\User Files\Results\\' + timestamp + testname +'\\'

    FlexDCA.write(":" + channel + "DISPlay ON")
    acquire_csv_and_jpg(FlexDCA, channel, path, filename)


    FlexDCA.write(":SYSTem:GTLocal")    # Local Mode


