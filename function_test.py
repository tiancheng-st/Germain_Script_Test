import pyvisa as visa
import struct
import matplotlib.pyplot as plt


rm = visa.ResourceManager()
# USB0::0x0957::0x9009::MY53120106::0::INSTR
# USB0::0x0957::0xBE18::K-86100D-20187::0::INSTR
scope = rm.open_resource("USB0::0x0957::0xBE18::K-86100D-20187::0::INSTR")

def do_query_string(query):
    global scope
    result = scope.query("%s" % query)
    return result

def do_query_number(query):
    global scope
    results = scope.query("%s" % query)
    return float(results)

idn_string = do_query_string("*IDN?")
print(idn_string)



# preamble_string = do_query_string(":WAVeform:PREamble?")
# ( wav_form, acq_type, wfmpts, avgcnt, x_increment, x_origin, x_reference, y_increment, y_origin, y_reference, coupling,
# x_display_range, x_display_origin, y_display_range,
# y_display_origin, date, time, frame_model, acq_mode,
# completion, x_units, y_units, max_bw_limit, min_bw_limit
# ) = preamble_string.split(",")

# x_increment = do_query_number(":WAVeform:XINCrement?")
# x_origin = do_query_number(":WAVeform:XORigin?")
# y_increment = do_query_number(":WAVeform:YINCrement?")
# y_origin = do_query_number(":WAVeform:YORigin?")

# print(x_origin)