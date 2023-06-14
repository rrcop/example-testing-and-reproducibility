"""Define a simple stochastic model."""

import numpy as np


def run_model(seed, n_samples, loc_val, scale_val):
    """A simple model that draws samples from a normal distribution."""
    
    info_s = ''
    
    rng = np.random.default_rng(seed)
    info_s = info_s + '\n' + 'rng: ' + str(rng)
    info_s = info_s + '\n' + 'seed: ' + str(seed)
    
    values = rng.normal(loc=loc_val, scale=scale_val, size=n_samples)
    
    return values, info_s # note that there is an info string generated as output
