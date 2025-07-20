#ifndef MODEL_CORE_H
#define MODEL_CORE_H

double* create_design_matrix(int num_rows, int num_columns);
void dispose_array(double** ptr_ref);
double generate_synthetic_data(double input_value);
double run_regression(double x, double y);

#endif