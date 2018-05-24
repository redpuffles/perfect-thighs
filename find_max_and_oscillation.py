#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on --23/05/18--

@authors: -- Roger Wu, Rex-Xue Lin --

Purpose: This file defines the function 'find_max_and_oscillation', which
         calculates the maximum value of a given array and its biofuel
         oscillation size.

Input:
    input_array            |    {Array} An array of biofuel measures inside the
                                bacteria.

Outputs:
    max_biofuel_int        |    {Float/integer} Highest amount of biofuel
                                inside bacteria.
    oscillation_size       |    {Float/integer} Size of oscillation.

"""


# Import library.
import numpy as np


def find_max_and_oscillation(input_array):
    # Find maximum biofuel value.
    max_biofuel_int = np.max(input_array)

    # Find index of the first instance of this maximum value.
    first_max_index = int(np.where(input_array == max_biofuel_int)[0])

    # If this is the last index in the array, oscillation size is 0.
    if (first_max_index == (np.size(input_array) - 1)):
        oscillation_size = 0
    # Otherwise, find the minimum value after this index and calculate
    # oscillation size.
    else:
        min_biofuel_int = np.min(input_array[first_max_index:])
        oscillation_size = max_biofuel_int - min_biofuel_int

    # Return maximum value and oscillation size.
    return max_biofuel_int, oscillation_size
