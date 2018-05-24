#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  ENGG1811 Assignment 2 
  Purpose: You can use this program to testthe following function from task 2A:
           (1) generate
 
"""

import numpy as np 
import pickle
import biofuel_simulation_design_parameter_sets as bsdps
import design as dn
import generate as gn


# Use the variable dataSetToUse to choose which parameter set you
# want to use
data_set_to_use = 1  # Either 1 or 2 
# 

# PLEASE DO NOT CHANGE THIS SECTION
# BEGIN - DO NOT CHANGE 

# The following line reads in the simulation parameters for data_set_to_use,
# For example: time increment and other parameters you need for simulation
simulation_design_para = bsdps.biofuel_simulation_design_parameter_sets(data_set_to_use)

# Initial (normalised) amount of bateria 
INITIAL_BACTERIA_AMOUNT = simulation_design_para['INITIAL_BACTERIA_AMOUNT' ] 
# Simulation start and end times, simulation time interval
TIME_START = simulation_design_para['TIME_START' ]     # Start time
TIME_END   = simulation_design_para['TIME_END' ]      # End time
TIME_DELTA = simulation_design_para['TIME_DELTA' ]    # Delta t 
# alpha_b: Lower and upper limits, number of points 
ALPHA_B_EXP_LOWER = simulation_design_para['ALPHA_B_EXP_LOWER'] 
ALPHA_B_EXP_UPPER = simulation_design_para['ALPHA_B_EXP_UPPER']
ALPHA_B_NUMBER_POINTS = simulation_design_para['ALPHA_B_NUMBER_POINTS']    
# alpha_p: Lower and upper limits, step size 
ALPHA_P_LOWER = simulation_design_para['ALPHA_P_LOWER'] 
ALPHA_P_UPPER = simulation_design_para['ALPHA_P_UPPER'] 
ALPHA_P_STEP = simulation_design_para['ALPHA_P_STEP']             
#
# Design parameters for biofuel system 
# Upper limit on the amount of internal fuel
THRESHOLD_MAX_INTERNAL_FUEL = simulation_design_para['THRESHOLD_MAX_INTERNAL_FUEL']
# Upper limit on the amount of oscillation 
THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL = simulation_design_para['THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL'] 
#

## Load the data for checking,  Read from file
data_cheking_file = open('set'+ str(data_set_to_use) + '_check.pickle', 'rb')
data_checking = pickle.load(data_cheking_file)  
data_cheking_file.close()


# END - DO NOT CHANGE 

time_array = np.arange(TIME_START, TIME_END+TIME_DELTA/2, TIME_DELTA)
num_time_points = len(time_array) 
# Parameter vectors for design 
# The vector vecAlphaB has been defined for you 
alpha_b_array = np.logspace(ALPHA_B_EXP_LOWER, ALPHA_B_EXP_UPPER, num=ALPHA_B_NUMBER_POINTS) 

## Task 2B: Caclulating the design objective and constraints for many pairs
# 
# 

alpha_b, alpha_p, max_internal_biofuel, oscillation_internal_biofuel, final_external_biofuel =  \
    gn.generate(data_set_to_use, time_array, INITIAL_BACTERIA_AMOUNT, alpha_b_array, ALPHA_P_LOWER, ALPHA_P_UPPER, ALPHA_P_STEP) 


best_alpha_b, best_alpha_p, poor_alpha_b, poor_alpha_p = \
    dn.design( THRESHOLD_MAX_INTERNAL_FUEL, THRESHOLD_MAX_OSCILLATION_INTERNAL_FUEL, 
           alpha_b, alpha_p, 
           max_internal_biofuel, oscillation_internal_biofuel, final_external_biofuel)
    
    
    
    

#
# Print your answers, and manually check them against the expected answers, 
# available from the link provided in the specs (see below). 
# Answers for this part are at, https://www.cse.unsw.edu.au/~en1811/18s1/assigns/ass2/answers.html
# You need to manually compare/check these answers.

    
