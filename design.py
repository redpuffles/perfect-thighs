#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:42:18 2018

@author: Rex
"""


import numpy as np

 

def design(THRESHOLD_MAX_INTERNAL_FUEL, THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL,
alpha_b_array, alpha_p_array, max_internal_biofuel, 
oscillation_internal_biofuel, final_external_biofuel) :

    
    
    # finding poor
    
    index = (np.argmax(final_external_biofuel))
    print(index)
    poor_alpha_b = (alpha_b_array[index//len(alpha_p_array)])
    poor_alpha_p = (alpha_p_array[index%len(alpha_p_array)])
    
    
    # condition
    c = ((max_internal_biofuel < THRESHOLD_MAX_INTERNAL_FUEL) & (oscillation_internal_biofuel < THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL))
    
    # set all false values to 0 
    # change to negative infinity?
    (final_external_biofuel[~c]) = 0

    
    
    # finding best
    index = (np.argmax(final_external_biofuel))
    best_alpha_b = (alpha_b_array[index//len(alpha_p_array)])
    best_alpha_p = (alpha_p_array[index%len(alpha_p_array)])
    
 
    return(best_alpha_b, best_alpha_p, poor_alpha_b, poor_alpha_p)