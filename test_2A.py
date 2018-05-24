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
## Load the data for checking,  Read from file
data_cheking_file = open('set'+ str(data_set_to_use) + '_check.pickle', 'rb')
data_checking = pickle.load(data_cheking_file)  
data_cheking_file.close()
# END - DO NOT CHANGE 



## Task 2A: Caclulating the design objective and constraints for many pairs
# of (alphaB,alphaP) 
# Time vector
# Create a list of regularly spaced time instants
# [0,0.25,0.5,0.75,...,20] 
# 
time_array = np.arange(TIME_START, TIME_END+TIME_DELTA/2, TIME_DELTA)

num_time_points = len(time_array) 

# Parameter vectors for design 
# The vector vecAlphaB has been defined for you 
alpha_b_array = np.logspace(ALPHA_B_EXP_LOWER, ALPHA_B_EXP_UPPER, num=ALPHA_B_NUMBER_POINTS) 
# 

alpha_b_array, alpha_p_array, max_internal_biofuel, oscillation_internal_biofuel, final_external_biofuel =  \
    gn.generate(data_set_to_use, time_array, INITIAL_BACTERIA_AMOUNT, 
                alpha_b_array, ALPHA_P_LOWER, ALPHA_P_UPPER, ALPHA_P_STEP) 


#
# Code to check your answers below .. 
#
diffmax_max_internal_biofuel = np.amax(abs(np.subtract(max_internal_biofuel, data_checking['max_internal_biofuel_check']) )) 
diffmax_max_oscillation_internal_biofuel = np.amax(abs(np.subtract(oscillation_internal_biofuel , data_checking['oscillation_internal_biofuel_check']) ))
diffmax_max_final_external_biofuel = np.amax(abs(np.subtract(final_external_biofuel , data_checking['final_external_biofuel_check'])) )

  
print('Difference in the maximum amount of internal biofuel  = ' + str(diffmax_max_internal_biofuel) )
print('Difference in the maximum amount of oscillation_internal_biofuel  = ' + str(diffmax_max_oscillation_internal_biofuel) )
print('Difference in the maximum amount of final_external_biofuel = ' + str(diffmax_max_final_external_biofuel) )
       

