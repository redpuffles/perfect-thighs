#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

Created on --23/05/18--

@authors: -- Roger Wu, Rex-Xue Lin --

Purpose: This file defines the function 'sim_biofuel', which aims to simulate
         the biofuel model.

Inputs:
    data_set_to_use        |    {Integer} Set ID for system constants needed
                                for simulation.
    array_time             |    {Array} An array of uniformly distributed time
                                instances.
    init_bacteria_amount   |    {Float/integer} The initial amount of bacteria.
    alpha_b                |    {Float/integer} Value of the parameter alpha_b
                                which is the production rate of biofuel.
    alpha_p                |    {Float/integer} Value of the parameter alpha_p
                                which is the production rate of efflux pumps.

Outputs:
    array_bateriaAmount    |    {Array} Amount of bacteria.
    array_sensor           |    {Array} Sensor output.
    array_pump             |    {Array} Number of efflux pumps.
    array_biofuelInt       |    {Array} Amount of biofuel inside bacteria.
    array_biofuelExt       |    {Array} Amount of biofuel outsie of bacteria.

"""


# Import libraries and files.
import biofuel_system_parameter_sets as bsps
import numpy as np


def sim_biofuel(data_set_to_use, time_array, init_bacteria_amount, alpha_b,
                alpha_p):
    # BEGIN - DO NOT REMOVE ---------------------------------------------------
    # Note: Please do not remove this
    sys_para = bsps.biofuel_system_parameter_sets(data_set_to_use)
    ALPHA_N = sys_para["ALPHA_N"]  # Growth rate (1/h)
    ALPHA_R = sys_para["ALPHA_R"]  # Basal repressor production rate (1/h)
    BETA_R = sys_para["BETA_R"]    # Repressor degradation rate (1/h)
    BETA_P = sys_para["BETA_P"]    # Pump degradation rate (1/h)
    DELTA_N = sys_para["DELTA_N"]  # Biofuel toxicity coefficient (1/(Mh))
    DELTA_B = sys_para["DELTA_B"]  # Biofuel export rate per pump (1/(Mh))
    GAMMA_P = sys_para["GAMMA_P"]  # Pump toxicity threshold
    GAMMA_I = sys_para["GAMMA_I"]  # Inducer saturation threshold (M)
    GAMMA_R = sys_para["GAMMA_R"]  # Repressor saturation threshold
    K_R = sys_para["K_R"]          # Repressor activation constant (h)
    K_P = sys_para["K_P"]          # Pump activation constant (1/h)
    K_B = sys_para["K_B"]          # Repressor deactivation constant (1/M)
    V = sys_para["V"]              # Ratio of intra to extracellular volume
    IND = sys_para["I"]              # Amount of inducer
    # The above lines set the following constants:
    # ALPHA_N ALPHA_R BETA_R  BETA_P  DELTA_N DELTA_B GAMMA_P GAMMA_I
    # GAMMA_R K_R K_P K_B V
    # END - DO NOT REMOVE -----------------------------------------------------

    # You should put your work below this line --------------------------------

    # Define 'delta', the time increment between values in 'time_array' (which
    # is uniform).
    delta = time_array[1] - time_array[0]

    # Create the five output arrays, equal in shape to 'time_array'. All values
    # inside are defaulted to the initial values.
    array_bacteriaAmount = np.full(np.shape(time_array), init_bacteria_amount)
    array_sensor = np.zeros(np.shape(time_array))
    array_pump = np.zeros(np.shape(time_array))
    array_biofuelInt = np.zeros(np.shape(time_array))
    array_biofuelExt = np.zeros(np.shape(time_array))

    # For each time value (excluding 0s as initial values are given), calculate
    # the corresponding value for the:
    # - Amount of bacteria.
    # - Biosensor output.
    # - Amount of efflux pumps.
    # - Amount of biofuel in the interior of the bacteria.
    # - Amount of biofuel in the exterior of the bacteria.
    # This is done using given formulae.
    for i in range(1, np.size(time_array)):
        # Amount of bacteria.
        array_bacteriaAmount[i] = \
            (array_bacteriaAmount[i-1] + (ALPHA_N*array_bacteriaAmount[i-1] *
             (1 - array_bacteriaAmount[i-1]) - DELTA_N*array_biofuelInt[i-1] *
             array_bacteriaAmount[i-1] - (ALPHA_N*array_bacteriaAmount[i-1] *
             array_pump[i-1])/(array_pump[i-1] + GAMMA_P))*delta)
        # Biosensor output.
        array_sensor[i] = \
            (array_sensor[i-1] + (ALPHA_R + K_R*(IND/(IND + GAMMA_I)) -
             BETA_R*array_sensor[i-1])*delta)
        # Amount of efflux pumps.
        array_pump[i] = \
            (array_pump[i-1] + (alpha_p + K_P*(1/((array_sensor[i-1]/(1 +
             K_B*array_biofuelInt[i-1])) + GAMMA_R)) - BETA_P *
             array_pump[i-1])*delta)
        # Amount of biofuel in the interior of the bacteria.
        array_biofuelInt[i] = \
            (array_biofuelInt[i-1] + (alpha_b*array_bacteriaAmount[i-1] -
             DELTA_B*array_pump[i-1]*array_biofuelInt[i-1])*delta)
        # Amount of biofuel in the exterior of the bacteria.
        array_biofuelExt[i] = \
            (array_biofuelExt[i-1] + (V*DELTA_B*array_pump[i-1] *
             array_biofuelInt[i-1]*array_bacteriaAmount[i-1])*delta)

    # Return the five output arrays.
    return (array_bacteriaAmount, array_sensor, array_pump, array_biofuelInt,
            array_biofuelExt)
