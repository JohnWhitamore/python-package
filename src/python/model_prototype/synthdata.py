import numpy as np

def generate_synthetic_weights(X):
    
    # ... dimensions
    _, M = X.shape
    
    # ... sample weights from a Gaussian distribution
    w_gen = np.random.multivariate_normal(np.zeros(M), np.eye(M))
    
    return w_gen

def generate_synthetic_data(X, w_gen, emission_variance_gen):
    
    # ... dimensions of the design matrix X
    N, _ = X.shape
    
    # ... random noise
    emission_st_dev_gen = np.sqrt(emission_variance_gen)
    emission_noise = np.random.normal(0, emission_st_dev_gen, size = N)
    
    # ... synthetic data
    synth_data = np.dot(X, w_gen) + emission_noise
    
    return synth_data