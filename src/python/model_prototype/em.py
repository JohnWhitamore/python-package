import numpy as np

def obtain_posterior(xTx, xTy, prior_variance, emission_variance_em):
    
    # Dimensions
    _, M = xTx.shape

    # Posterior covariance
    
    # ... emission precision as reciprocal of emission variance
    emission_precision = 1 / emission_variance_em
    
    # ... prior precision as inverse of diagonal-structured prior covariance
    prior_precision = np.zeros([M, M])
    
    for m in range(M):
        
        prior_precision[m, m] = 1 / prior_variance
    
    # ... obtain posterior values
    posterior_precision = prior_precision + emission_precision * xTx
    posterior_covariance = np.linalg.inv(posterior_precision)
    
    # Posterior mean
    posterior_mean = emission_precision * np.dot(posterior_covariance, xTy)
    
    return posterior_mean, posterior_covariance

def manage_number_of_effective_parameters(X, prior_variance, posterior_mean, posterior_covariance):
    
    # Dimensions
    N, M = X.shape
    
    # ... alpha (prior_precision scalar) from prior_variance
    alpha = 1 / prior_variance
    
    # ... running totals
    sum_gamma = 0.0
    trace_posterior_covariance = 0.0
    posterior_mean_norm = 0.0
    
    # ... loop through the basis functions
    for m in range(M):
        
        # ... gamma (number of effective parameters from each basis function)
        gamma = 1.0 - alpha * posterior_covariance[m, m]
        sum_gamma += gamma
        
        # ... accumulate the trace of the posterior covariance
        trace_posterior_covariance += posterior_covariance[m, m]
        
        # ... accumulate the posterior mean L2 norm
        posterior_mean_norm += posterior_mean[m] * posterior_mean[m]
        
    # ... update prior_precision, alpha
    denominator = posterior_mean_norm + trace_posterior_covariance
    alpha = M / denominator
    
    return sum_gamma, alpha

def reestimate_parameter_values(y, X, sum_gamma, alpha, posterior_mean):
    
    # ... dimensions
    N, _ = X.shape
    
    # ... re-estimate the emission variance
    distance = y - np.dot(X, posterior_mean)
    distance_sq = np.dot(np.transpose(distance), distance)
    denominator = N - sum_gamma
    emission_variance = distance_sq / denominator
    
    # ... re-estimate the prior_variance
    prior_variance = 1 / alpha
    
    return prior_variance, emission_variance

def run_m_step(y, X, prior_variance, posterior_mean, posterior_covariance):
    
    # ... manage number of effective parameters
    sum_gamma, alpha = manage_number_of_effective_parameters(X, prior_variance, posterior_mean, posterior_covariance)
    
    # ... re-estimate parameter values
    prior_variance, emission_variance = reestimate_parameter_values(y, X, sum_gamma, alpha, posterior_mean)

    return prior_variance, emission_variance, X, posterior_mean
    

def run_em_algorithm(num_iterations, y, X, prior_mean, prior_variance, emission_variance_em):
    
    # ... pre-calculate useful inner products xTx, xTy
    xTx = np.dot(np.transpose(X), X)
    xTy = np.dot(np.transpose(X), y)
    
    for i in range(num_iterations):

        # ... E-step
        posterior_mean, posterior_covariance = obtain_posterior(xTx, xTy, prior_variance, emission_variance_em)
        
        # ... M-step
        prior_variance, emission_variance, X, posterior_mean = run_m_step(y, X, 
                                                          prior_variance, posterior_mean, posterior_covariance)
    
    
    
    return posterior_mean