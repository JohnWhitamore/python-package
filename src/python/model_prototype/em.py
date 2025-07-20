import numpy as np

def obtain_posterior(xTx, xTy, prior_covariance, emission_variance_em):
    
    # Posterior covariance
    
    # ... emission precision as reciprocal of emission variance
    emission_precision = 1 / emission_variance_em
    
    # ... prior precision as inverse of diagonal-structured prior covariance
    _, M = prior_covariance.shape
    prior_precision = np.zeros([M, M])
    
    for m in range(M):
        
        prior_precision[m, m] = 1.0 / prior_covariance[m, m]
    
    # ... obtain posterior values
    posterior_precision = prior_precision + emission_precision * xTx
    posterior_covariance = np.linalg.inv(posterior_precision)
    
    # Posterior mean
    posterior_mean = emission_precision * np.dot(posterior_covariance, xTy)
    
    return posterior_mean, posterior_covariance

def manage_sparsity(X,prior_covariance, posterior_mean, posterior_covariance):
    
    # ... dimensions before sparsity
    N, M = X.shape
    
    # ... arrays (reduced size)
    gamma = np.zeros(M)
    alpha = 1 / np.diag(prior_covariance)
    alpha_new = np.zeros(M)
    
    # ... running total
    sum_gamma = 0.0
    
    # ... loop through the basis functions that are still being used
    for m in range(M):
        
        # ... prior covariance values
        gamma[m] = 1.0 - alpha[m] * posterior_covariance[m, m]
        alpha_new[m] = gamma[m] / (posterior_mean[m] * posterior_mean[m])
        
        # ... update the sum of gamma values
        sum_gamma += gamma[m]
        
    # ... remove basis functions
    alpha = alpha_new
    
    return N, sum_gamma, alpha, X, posterior_mean

def reestimate_parameter_values(y, X, sum_gamma, alpha, posterior_mean):
    
    # ... dimensions
    N, _ = X.shape
    
    # ... re-estimate the emission variance
    distance = y - np.dot(X, posterior_mean)
    distance_sq = np.dot(np.transpose(distance), distance)
    denominator = N - sum_gamma
    emission_variance = distance_sq / denominator
    
    # ... re-estimate the prior_covariance
    prior_covariance = np.diag(1 / alpha)
    
    return prior_covariance, emission_variance

def run_m_step(y, X, prior_covariance, posterior_mean, posterior_covariance):
    
    # ... manage sparsity
    N, sum_gamma, alpha, X, posterior_mean = manage_sparsity(X, prior_covariance, posterior_mean, posterior_covariance)
    
    # ... re-estimate parameter values
    prior_covariance, emission_variance = reestimate_parameter_values(y, X, sum_gamma, alpha, posterior_mean)

    return prior_covariance, emission_variance, X, posterior_mean
    

def run_em_algorithm(num_iterations, y, X, prior_mean, prior_covariance, emission_variance_em):
    
    # ... pre-calculate useful inner products xTx, xTy
    xTx = np.dot(np.transpose(X), X)
    xTy = np.dot(np.transpose(X), y)
    
    for i in range(num_iterations):

        # ... E-step
        posterior_mean, posterior_covariance = obtain_posterior(xTx, xTy, prior_covariance, emission_variance_em)
        
        # ... M-step
        prior_covariance, emission_variance, X, posterior_mean = run_m_step(y, X, 
                                                          prior_covariance, posterior_mean, posterior_covariance)
    
    
    
    return posterior_mean