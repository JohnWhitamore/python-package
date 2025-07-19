// model_core.c

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int create_design_matrix(int num_rows, int num_columns)
{
    printf("[create_design_matrix] Requested matrix with %d rows and %d columns.\n", num_rows, num_columns);
	int output = num_rows * num_columns;
	
    return output;
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