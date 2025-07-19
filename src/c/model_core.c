// model_core.c

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int* create_design_matrix(int rows, int cols) {
    
	printf("[create_design_matrix] Input: rows=%d, cols=%d\n", rows, cols);

    int* result = (int*)malloc(2 * sizeof(int));
	
    if (result == NULL) {
        printf("[create_design_matrix] Allocation failed.\n");
        return NULL;
    }

    result[0] = rows;
    result[1] = cols;
	
    return result;
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