"""Test cases for the model defined in model.py."""

# modules used in model - update the 'modules' list below to output version
# infor for each. 
import numpy as np


from model import run_model
from build_info import print_os
from build_info import print_module_versions
from build_info import print_python_version 

config_out = '*** build info ***'

#output build to console (not sure this is useful as-is, but it's a step.)
s = print_os()
config_out = config_out + s

s = print_python_version()
config_out = config_out + s

modules = ["numpy"] #include any modules you want version info for. 
s = print_module_versions(modules)
config_out = config_out + s
    

# Run the model.
# specify input values as arguments: 
s = '*** model input args ***'

seed = 1
s = s + '\n' + str(f'seed: {seed}')

n_samples = 50
s = s + '\n' + str(f'n_samples: {n_samples}')

loc_val = 10
s = s + '\n' + str(f'loc_val: {loc_val}')

scale_val = 1
s = s + '\n' + str(f'scale_val: {scale_val}')

#add input info to config output
config_out = config_out + '\n\n' + s


# record info like rng: 
model_output, info_string = run_model(seed, n_samples, loc_val, scale_val)


#add model info to config output
config_out = config_out + "\n\n*** model info ***" + info_string 


# record test output: 
config_out = config_out + "\n\n*** test results ***"

# Is the output mean close to the expected mean?
expected_mean = loc_val
model_mean = np.mean(model_output)
mean_abs_error = np.abs(model_mean - expected_mean)

mean_max_error = 0.2
if mean_abs_error > mean_max_error:
    test_s = str(f'Sample mean has error {mean_abs_error}')
    raise ValueError(test_s)
    config_out = config_out + '\n' + 'mean_abs_error fail: ' + test_s
else:
        config_out = config_out + '\n' + str(f'mean_abs_error pass (mean_abs_error < {mean_max_error})')

# Is the output standard deviation close to the expected standard deviation?
expected_sd = scale_val
model_sd = np.std(model_output)
sd_abs_error = np.abs(model_sd - expected_sd)

sd_max_error = 0.15
if sd_abs_error > sd_max_error:
    test_s = str(f'Sample sd has error {sd_abs_error}')
    raise ValueError(test_s)
    config_out = config_out + '\n' + 'sd_abs_error fail: ' + test_s
else:
    config_out = config_out + '\n' + str(f'sd_abs_error pass (sd_abs_error < {sd_max_error})')
        
    
    
    
# write run info to file. 
config_f = open("config_output_run.txt", "w") #note: should add a timestamp
config_f.write(config_out)
config_f.close()
