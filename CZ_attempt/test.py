"""Test cases for the model defined in model.py."""

# modules used in model - update the 'modules' list below to output version
# infor for each. 
import numpy as np
import pandas as pd
import os

#include any modules you want version info for. 
modules = ["numpy", "pandas"] 

from model import run_model
from build_info import print_os
from build_info import print_module_versions
from build_info import print_python_version 


#output build info to file
config_out = '*** build info ***'

s = print_os()
config_out = config_out + s

s = print_python_version()
config_out = config_out + s

s = print_module_versions(modules)
config_out = config_out + s
    
#specify test case:
test_case_label = "CZv0"
test_case_dirname = os.getcwd() + "\\test_cases\\test_case_" + test_case_label

# specify input and output config filenames: 
# input: 
fname_input_params = test_case_dirname + "\\test_case_parameter_input.csv"

#output: 
fname_config_out = "test_config_output.txt"
fname_model_out = "test_model_output.txt"


# specify input values as arguments: 
# parameter read-in from file: 
params_df = pd.read_csv(fname_input_params)
params_dict = dict( (params_df.parameter[i], params_df.value[i]) for i in params_df.index )

#add input info to config output
s = '*** model input args ***\n'
s = s + params_df.to_string(index = False) #note that to_string can be slow
config_out = config_out + '\n\n' + s

# Run the model.
# run model and record info such as rng type: 
model_output, info_string = run_model(params_dict['seed'], \
                                      params_dict['n_samples'], \
                                      params_dict['loc_val'],\
                                      params_dict['scale_val'])

#add model info to config output
config_out = config_out + "\n\n*** model info ***" + info_string 


# Test the model results: 
    
# record of test output: 
config_out = config_out + "\n\n*** test results ***"


#####
#Test 1: 
# Is the output mean close to the expected mean?
expected_mean = params_dict['loc_val']
model_mean = np.mean(model_output)
mean_abs_error = np.abs(model_mean - expected_mean)

mean_max_error = 0.2
if mean_abs_error > mean_max_error:
    test_s = str(f'Sample mean has error {mean_abs_error}')
    raise ValueError(test_s)
    config_out = config_out + '\n' + 'mean_abs_error fail: ' + test_s
else:
        config_out = config_out +\
            '\n' + str(f'mean_abs_error pass (mean_abs_error < {mean_max_error})')


#####
#Test 2: 
# Is the output standard deviation close to the expected standard deviation?
expected_sd = params_dict['scale_val']
model_sd = np.std(model_output)
sd_abs_error = np.abs(model_sd - expected_sd)

sd_max_error = 0.15
if sd_abs_error > sd_max_error:
    test_s = str(f'Sample sd has error {sd_abs_error}')
    raise ValueError(test_s)
    config_out = config_out + '\n' + 'sd_abs_error fail: ' + test_s
else:
    config_out = config_out +\
        '\n' + str(f'sd_abs_error pass (sd_abs_error < {sd_max_error})')
        
   
#####
#Test 3: 
# does the output match the test case with the same input parameters? 

# load test vals from the test case specified above: 
test_case_output_fname = test_case_dirname + "\\test_case_model_output.csv"
test_case_output = pd.read_csv(test_case_output_fname, header=None)
test_vals = np.array(test_case_output[1])
#note that these are 64bit floats and there will be precision limitations from read-in
# to facilitate comparison, select test precision: 
test_precision = 10 #number of decimal places to round off. 

#compare all values: 
val_comparison = (np.around(model_output, test_precision) == \
                  np.around(test_vals, test_precision))
if not(all(val_comparison)):
    #test failed
    test_s = str(f'Sample values are not identical to test vals at precision {test_precision}')
    raise ValueError(test_s)
    config_out = config_out + \
        '\n' + 'val_compare_error fail: ' + test_s 
else:
    config_out = config_out + \
        '\n' + str(f'val_compare_error pass (values equal at precision {test_precision})')
            
  
    
  
# write run info to file. 
config_f = open(fname_config_out, "w") #note: should add a timestamp
config_f.write(config_out)
config_f.close()
