import numpy as np


def digit_max(vmax):
    tmpvmax = vmax
    digit_counter = 0
    while 10**digit_counter < tmpvmax:
        vmax = 10**(digit_counter+1)
        digit_counter += 1

    return digit_counter
