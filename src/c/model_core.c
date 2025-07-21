#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>

double* create_design_matrix(int rows, int cols) 
{
    if (rows != cols) {
        printf("[create_design_matrix] Error: matrix must be square.\n");
        return NULL;
    }

    int size = rows * cols;
	
    double* result = (double*)malloc(size * sizeof(double));
	
    if (result == NULL) 
	{
        printf("[create_design_matrix] Allocation failed.\n");
        return NULL;
    }

    // Initialize GSL random number generator
    gsl_rng_env_setup();  // optional: respects environment variables if set
    gsl_rng* rng = gsl_rng_alloc(gsl_rng_default);
	
    if (rng == NULL) 
	{
        printf("[create_design_matrix] Failed to initialize RNG.\n");
        free(result);
        return NULL;
    }

    // Populate with independent N(0,1) samples (mean = 0, stddev = 1)
	// ... placeholder functionality
    for (int i = 0; i < size; ++i) 
	{
        result[i] = gsl_ran_gaussian(rng, 1.0);
    }

    gsl_rng_free(rng);  // Clean up RNG

    return result;
}

// Fully clean up and nullify the pointer
void dispose_array(double** ptr_ref) 
{
    if (ptr_ref && *ptr_ref) 
	{
        free(*ptr_ref);
        *ptr_ref = NULL;
    }
}

// Placeholder
double generate_synthetic_data(double input_value)
{
    double output = input_value + 42.0;
    printf("[generate_synthetic_data] Input: %lf → Output: %lf\n", input_value, output);
	
    return output;
}

// Placeholder
double run_regression(double x, double y)
{
    double slope = 2.0;
    double intercept = 1.0;
	
    double prediction = slope * x + intercept * y;
    printf("[run_regression] x: %lf, y: %lf → prediction: %lf\n", x, y, prediction);
	
    return prediction;
}