import pandas as pd
import numpy as np
import read_input as ri
import libraries_functions as lf

class ConvergeOutputData:

    def __init__(self, is_successful, current_output, matrix_tech_coeff, iteration, difference) -> None:
        
        self.current_output = current_output
        self.matrix_tech_coeff = matrix_tech_coeff
        self.iteration = iteration
        self.difference = difference
        self.is_successful= is_successful

    def get_is_successful(self) -> bool:
        return self.is_successful

def converge (max_iteration: int, error_accuracy: float, ras_matrices: pd.DataFrame) -> pd.DataFrame: 
    """
    This method employs ras estimation methodology to estimate a square matrix whose row and sum totals align to the given row and sum total vectors by the user.\n
    The difference between the given and the result are ensured to be less than or equal to the error_accuracy desired by the user. \n
    Finally, it also returns the table's responding technical coefficients.
    """
    # Diagonalize the total output matrix
    diagonalized_total_output_matrix = np.diag(ras_matrices.df_matrix_output)
    # Create temporary coefficient
    temp_coeff = ras_matrices.df_matrix_coeff
    # Calculate temporary output matrix
    current_output = lf.calculate_output(temp_coeff, diagonalized_total_output_matrix)
    # # Get row info and column info
    row_info = lf.get_all_row_info(current_output, ras_matrices.df_matrix_intermediate_demand)
    col_info = lf.get_all_col_info(current_output, ras_matrices.df_matrix_consumption)
    # TODO: add time spent to calculate the whole iteration
    iteration = 0

    def recalculate_matrices(temp_coeff, diagonalized_total_output_matrix, ras_matrices):
        current_output = lf.calculate_output(temp_coeff, diagonalized_total_output_matrix)
        row_info = lf.get_all_row_info(current_output,ras_matrices.df_matrix_intermediate_demand)
        col_info = lf.get_all_col_info(current_output,ras_matrices.df_matrix_consumption)

        return (current_output, row_info, col_info)
    
    def get_tech_coeff(current_output, ras_matrices: ri.RASMatrices) -> pd.DataFrame:
        transposed_total_output_matrix = ras_matrices.df_matrix_output.reshape(1, -1) 
        matrix_tech_coeff = current_output / transposed_total_output_matrix

        return matrix_tech_coeff

    while ((row_info[lf.ROW_DIFF_KEY] > error_accuracy  or col_info[lf.COL_DIFF_KEY] > error_accuracy) and iteration <= max_iteration):
        if row_info[lf.ROW_DIFF_KEY] > error_accuracy :
            diagonalized_ratio = np.diag(row_info[lf.ROW_RATIO_KEY])
            temp_coeff = np.matmul(diagonalized_ratio, temp_coeff)
            current_output, row_info, col_info = recalculate_matrices(temp_coeff, diagonalized_total_output_matrix, ras_matrices)
        
        if col_info[lf.COL_DIFF_KEY] > error_accuracy:
            diagonalized_ratio = np.diag(col_info[lf.COL_RATIO_KEY])
            temp_coeff = np.matmul(temp_coeff, diagonalized_ratio)
            current_output, row_info, col_info = recalculate_matrices(temp_coeff, diagonalized_total_output_matrix, ras_matrices)

        iteration = iteration +1
        difference = row_info[lf.ROW_DIFF_KEY]
        matrix_tech_coeff = get_tech_coeff(current_output, ras_matrices)
        print(f"Iteration: {iteration}. Difference between totals: {row_info[lf.ROW_DIFF_KEY]}")    

    is_successful = iteration <= max_iteration + 1

    return  ConvergeOutputData(is_successful, current_output, matrix_tech_coeff, iteration, difference)




