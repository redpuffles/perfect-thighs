#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  ENGG1811 Assignment 2 
  Purpose: You can use this program to test these two functions:
           (1) sim_biofuel
           (2) find_max_and_oscillation
 
"""
import numpy as np 
import pickle
import biofuel_simulation_design_parameter_sets as bsdps
import sim_biofuel as sb
import find_max_and_oscillation as fmo


# Use the variable data_set_to_use to choose which parameter set you
# want to use
data_set_to_use = 2 # Either 1 or 2

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


## Preliminary code for simulation  
# Time array
time_array = np.arange(TIME_START, TIME_END + TIME_DELTA/2,  TIME_DELTA)
num_time_points = len(time_array) 

# Three different pairs of (alpha_b,alpha_p)
alpha_b_test = np.array([0.01623777, 0.14384499, 1.00 ])
alpha_p_test = np.array([0.07,       0.06,       0.05 ])
## You can choose between three different pairs of (alpha_b,alpha_p)
#  by specifying the variable test_index to 0, 1, or 2 
test_index = 2  # Use 0, 1, 2 
# Get the alpha_b and alpha_p for test_index  
alpha_b = alpha_b_test[test_index] 
alpha_p = alpha_p_test[test_index]  

# Simulation 
bacteria_amount_array,sensor_array,pump_array,biofuel_int_array,biofuel_ext_array =   \
        sb.sim_biofuel(data_set_to_use,time_array,INITIAL_BACTERIA_AMOUNT,alpha_b,alpha_p) 
        
# Compare your simulation result aginst the benchmark 
max_diff_bacteria = max(abs(np.subtract(bacteria_amount_array, data_checking['bacteria_check'][:,test_index] ))) 
max_diff_sensor = max(abs(np.subtract(sensor_array, data_checking['sensor_check'][:,test_index])) )
max_diff_pump = max(abs(np.subtract(pump_array, data_checking['pump_check'][:,test_index] )) )
max_diff_biofuel_int = max(abs(np.subtract(biofuel_int_array, data_checking['biofuel_int_check'][:,test_index])) )
max_diff_biofuel_ext = max(abs(np.subtract(biofuel_ext_array, data_checking['biofuel_ext_check'][:,test_index])) )
# The difference should be small 
print('Maximu difference in the amount of bacteria = ' + str(max_diff_bacteria) )
print('Maximu difference in the sensor             = ' + str(max_diff_sensor) )
print('Maximu difference in the number of pumps    = ' + str(max_diff_pump) )
print('Maximu difference in the internal biofuel   = ' + str(max_diff_biofuel_int) )
print('Maximu difference in the external biofuel   = ' + str(max_diff_biofuel_ext) )


## Test 1B below
#
# You can use the following code to test the function find_max_and_oscillation
# You need to comment out the following 5 lines to run the test 
max_internal_fuel, oscillation_internal_fuel = fmo.find_max_and_oscillation(biofuel_int_array) 
diffmax_internal_fuel = abs(max_internal_fuel - data_checking['max_biofuel_int_check'][test_index]) 
diff_oscillation_internal_fuel = abs(oscillation_internal_fuel - data_checking['oscillation_biofuel_int_check'][test_index]) 
  
print('Difference in the maximum amount of internal biofuel  = ' + str(diffmax_internal_fuel) )
print('Difference in the amount of oscillation of internal biofuel  = ' + str(diff_oscillation_internal_fuel) )
