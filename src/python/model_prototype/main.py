import numpy as np
import matplotlib.pyplot as plt

import xdata
import synthdata
import em

"""
This code reflects the Relevance Vector Machine of Mike Tipping.
The idea is to start with a "full" set of basis functions and then
to prune them in successful iterations of the EM algorithm.

Note that the pruning necessitates that care be taken over the
certain quantities, including the design matrix, X, whose
columns each represent a basis function.
"""

"""
Data and basis functions
"""

# Specify calendar parameter values

# ... calendar
num_years = 2
days_per_year = 365
seasons_per_year = 4

# ... number of time-steps
num_time_steps = days_per_year * num_years

# Generate basis functions

# ... note that X represents the "full" design matrix with all basis functions included
X = xdata.generate_basis_functions(num_time_steps, seasons_per_year, days_per_year)

# ... obtain dimensions
N, M = X.shape

print(N, M)

"""
Synthetic data generation
"""

# ... generate synthetic weights
# ... note that w_gen and X_gen reflect only the basis functions that are being used
w_gen = synthdata.generate_synthetic_weights(X)

# ... generate synthetic observed data
emission_variance_gen = 0.0001
y = synthdata.generate_synthetic_data(X, w_gen, emission_variance_gen)

# ... calculate conditional mean
mean_gen = np.dot(X, w_gen)

"""
Inference and learning
"""

# Specify inference parameter values

# ... number of iterations of the EM algorithm
num_iterations = 10

# ... initial estimates of parameter values
# ... - can often bootstrap estimates from a simpler model
emission_variance_em = emission_variance_gen * 1.2
prior_mean = np.zeros(M)
prior_variance = 1.0
prior_covariance = prior_variance * np.eye(M)

# Run the EM algorithm
posterior_mean = em.run_em_algorithm(num_iterations, y, X, 
                                      prior_mean, prior_covariance, emission_variance_em)

# Predictive density
predictive_mean = np.dot(X, posterior_mean)

# Display output
plt.plot(np.arange(N), y, 'go', alpha = 0.4)
plt.plot(np.arange(N), mean_gen, 'b-')
plt.plot(np.arange(N), predictive_mean, 'k-')
plt.show()

