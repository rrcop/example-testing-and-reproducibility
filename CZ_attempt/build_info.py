# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:19:06 2023

@author: czachreson
prints out build info
"""

#specify modules to import
modules = ["platform", "sys", "numpy", "pandas"] 


for m in modules:
    # executes string as python command
    exec('import ' + m)
    print('imported ' + m)

    #import platform
    #import numpy
    #import sys

#operating system: 
def print_os():
    s = '\n' + 'Operating System: ' + platform.platform()
    print(s)
    return s

# python version:
def print_python_version():
    s = "\n" + "Python version: " + sys.version
    print(s)
    return s

# imported modules: 
# note, listing all imported packages is fairly verbose due to IDE dependencies
# should figure out a good way to iterate through a subset of imported modules
def print_np_ver():
    print('numpy version: ' + numpy.__version__)

def print_platform_ver():
    print('platform version: ' + platform.__version__)
    
    
def print_module_versions(module_set):
    s_out = '\n\n** module versions **'
    for m in module_set:
        
        s = eval( m + '.__version__')
        s2 = m + ' version: ' + s
        print( s2 )
        
        s_out  = s_out + "\n" + s2
    return s_out
        
        
    

module_set = ["platform", "numpy"]

test = print_module_versions(module_set)