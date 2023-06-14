"""Test cases for the model defined in model.py."""

# modules used in model - update the 'modules' list below to output version
# info for each. 
import numpy as np
import pandas as pd
import shutil
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
    

# make a directory for the test case: 
test_dirname = os.getcwd() + "\\test_cases\\test_case_CZv0"

if not(os.path.isdir(test_dirname)):
    os.mkdir(test_dirname)

# specify input and output config filenames: 
fname_input_params = "test_parameter_input.csv"
fname_test_case_input = test_dirname + "\\test_case_parameter_input.csv"
fname_config_out = test_dirname + "\\test_case_config_output.txt"
fname_model_out = test_dirname + "\\test_case_model_output.csv" 

# specify input values as arguments: 
# parameter read-in from file (no hard-coded arguments): 
params_df = pd.read_csv(fname_input_params)
params_dict = dict( (params_df.parameter[i], params_df.value[i]) for i in params_df.index )

#copy parameter file into test case folder: 
shutil.copyfile(fname_input_params, fname_test_case_input)

#add input info to config output
param_str = params_df.to_string(index = False)

s = '*** model input args ***\n'
s = s + param_str #note that to_string can be slow
config_out = config_out + '\n\n' + s

# Run the model.
# run model and record info such as rng type: 
model_output, info_string = run_model(params_dict['seed'], \
                                      params_dict['n_samples'], \
                                      params_dict['loc_val'],\
                                      params_dict['scale_val'])


# record output
pd.DataFrame(model_output).to_csv(fname_model_out, header=False)

#add model info to config output
config_out = config_out + "\n\n*** model info ***" + info_string 

# write test case info to file. 
config_f = open(fname_config_out, "w") #note: should add a timestamp
config_f.write(config_out)
config_f.close()
