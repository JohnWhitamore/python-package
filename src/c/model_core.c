#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Allocate a design matrix of shape [rows x cols]
int* create_design_matrix(int rows, int cols) 
{
    int* result = (int*)malloc(rows * cols * sizeof(int));

    if (result == NULL) 
	{
        printf("[create_design_matrix] Allocation failed.\n");
        return NULL;
    }

    // ... populate matrix with placeholder values
    for (int i = 0; i < rows; ++i) 
	{
        for (int j = 0; j < cols; ++j) 
		{  
            result[i * cols + j] = (i + 1) * (j + 1); 
        }
    }

    return result;
}

// Fully clean up and nullify the pointer
void dispose_array(int** ptr_ref) 
{
    if (ptr_ref && *ptr_ref) 
	{
        free(*ptr_ref);
        *ptr_ref = NULL;
    }
}

double generate_synthetic_data(double input_value)
{
    double output = input_value + 42.0;
    printf("[generate_synthetic_data] Input: %lf → Output: %lf\n", input_value, output);
	
    return output;
}

double run_regression(double x, double y)
{
    double slope = 2.0;
    double intercept = 1.0;
	
    double prediction = slope * x + intercept * y;
    printf("[run_regression] x: %lf, y: %lf → prediction: %lf\n", x, y, prediction);
	
    return prediction;
}