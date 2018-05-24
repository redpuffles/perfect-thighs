#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

Created on --24/05/18--

@authors: -- Roger Wu, Rex-Xue Lin --

Purpose: This file defines the function '-', which -.

Inputs:
                           |    {}

Outputs:
                           |    {}

"""


import sim_biofuel as sb
import find_max_and_oscillation as fmo
import numpy as np


def generate(data_set_to_use, time_array, INITIAL_BACTERIA_AMOUNT,
             alpha_b_array, ALPHA_P_LOWER, ALPHA_P_UPPER, ALPHA_P_STEP):
    #
    alpha_p_array = np.arange(ALPHA_P_LOWER, (ALPHA_P_UPPER + ALPHA_P_STEP),
                              ALPHA_P_STEP)

    #
    max_internal_biofuel = \
        np.zeros((np.size(alpha_b_array), np.size(alpha_p_array)))
    oscillation_internal_biofuel = \
        np.zeros((np.size(alpha_b_array), np.size(alpha_p_array)))
    final_external_biofuel = \
        np.zeros((np.size(alpha_b_array), np.size(alpha_p_array)))

    #
    for i in range(0, np.size(alpha_b_array)):
        for j in range(0, np.size(alpha_p_array)):
            array_bacteriaAmount, array_sensor, array_pump, array_biofuelInt, \
                array_biofuelExt = sb.sim_biofuel(data_set_to_use, time_array,
                                      INITIAL_BACTERIA_AMOUNT, i, j)

            #
            max_biofuel_int, oscillation_size = \
                fmo.find_max_and_oscillation(array_biofuelInt)

            #
            max_internal_biofuel[i, j] = max_biofuel_int
            oscillation_internal_biofuel[i, j] = oscillation_size
            final_external_biofuel[i, j] = max_biofuel_int

    #
    return (alpha_b_array, alpha_p_array, max_internal_biofuel,
            oscillation_internal_biofuel, final_external_biofuel)