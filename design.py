#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

Created on --30/05/18--

@authors: -- Roger Wu, Rex-Xue Lin --

Purpose: This file defines the function 'design', which determines the best
         pair of 'alpha_b' and 'alpha_p' values based on:
             - Amount of biofuel that can be collected.
             - Maximum amount of internal biofuel.
             - Amount of oscillation of internal biofuel.
         For comparison purposes, the worst pair is also stated based on the
         same criteria.

Inputs:
    THRESHOLD_MAX_             |    {Float/integer} Threshold on the maximum
        _INTERNAL FUEL         ·    amount of internal biofuel.
    THRESHOLD_MAX_             |    {Float/integer} Threshold on oscillation of
        OSCILLATION_INTERNAL_  ·    internal biofuel.
        FUEL                   ·
    alpha_b_array              |    {Array} An array of 'alpha_b' values.
    alpha_p_array              |    {Array} An array of 'alpha_p' values.
    max_internal_biofuel       |    {Array} An array containing max internal
                               ·    biofuel values calculated using each pair
                               ·    of values between 'alpha_b_array' and
                               ·    'alpha_b_array'.
    oscillation_internal_      |    {Array} An array containing oscillation
        biofuel                ·    sizes calculated using each pair of
                               ·    values etween 'alpha_b_array' and
                               ·    'alpha_b_array'.
    final external_biofuel     |    {Array} An array containing final external
                               ·    biofuel values calculating using each pair
                               ·    of values between 'alpha_b_array' and
                               ·    'alpha_b_array'

Outputs:
    best_alpha_b               |    {Float/integer} Best 'alpha_b' value.
    best_alpha_p               |    {Float/integer} Best 'alpha_p' value.
    poor_alpha_b               |    {Float/integer} Worst 'alpha_b' value.
    poor_alpha_p               |    {Float/integer} Worst 'alpha_p' value.

"""


import numpy as np


def design(THRESHOLD_MAX_INTERNAL_FUEL,
           THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL, alpha_b_array,
           alpha_p_array, max_internal_biofuel, oscillation_internal_biofuel,
           final_external_biofuel):
    # Finding poor.
    index = np.argmax(final_external_biofuel)
    poor_alpha_b = alpha_b_array[index // len(alpha_p_array)]
    poor_alpha_p = alpha_p_array[index % len(alpha_p_array)]

    # Condition: within thresholds.
    c = ((max_internal_biofuel < THRESHOLD_MAX_INTERNAL_FUEL) &
         (oscillation_internal_biofuel <
          THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL))

    # Set all false values to 0.
    # Change to negative infinity?
    (final_external_biofuel[~c]) = 0

    # Finding best.
    index = np.argmax(final_external_biofuel)
    best_alpha_b = alpha_b_array[index // len(alpha_p_array)]
    best_alpha_p = alpha_p_array[index % len(alpha_p_array)]

    # Return outputs.
    return(best_alpha_b, best_alpha_p, poor_alpha_b, poor_alpha_p)
