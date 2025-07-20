import numpy as np
import matplotlib.pyplot as plt

import xdata
import synthdata
import em

"""
This code implements Bayesian regression. It was adapted from RVM code in Python
that I had already written. The purpose of this code is to serve as a basis
for implementing the functionality in C. For that reason, the code uses loops
where they would not usually be used in Python.
"""

"""
Data and basis functions
"""

# Specify calendar parameter values

# ... calendar
num_years = 2
days_per_year = 365
seasons_per_year = 4

# Generate basis functions

# ... note that X represents the "full" design matrix with all basis functions included
X = xdata.generate_basis_functions(num_years, seasons_per_year, days_per_year)

# ... obtain dimensions
N, M = X.shape

print(N, M)

"""
Synthetic data generation
"""

# ... generate synthetic weights
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

# Run the EM algorithm
posterior_mean = em.run_em_algorithm(num_iterations, y, X, 
                                      prior_mean, prior_variance, emission_variance_em)

# Predictive density
predictive_mean = np.dot(X, posterior_mean)

# Display output
plt.plot(np.arange(N), y, 'go', alpha = 0.4)
plt.plot(np.arange(N), mean_gen, 'b-')
plt.plot(np.arange(N), predictive_mean, 'k-')
plt.show()

