import numpy as np
import pandas as pd
import read_input as ri

ROW_SUMS_KEY = "row_sums"
ROW_DIFF_KEY = "row_diff"
ROW_RATIO_KEY= "row_ratio"
COL_SUMS_KEY = "col_sums"
COL_DIFF_KEY = "col_diff"
COL_RATIO_KEY= "col_ratio"

#function to calculated output table
def calculate_output(coeff_matrix: pd.DataFrame, diagonal_matrix: pd.DataFrame):
    return (np.matmul(coeff_matrix, diagonal_matrix))

#function to get vector difference
def calulate_diff(output: pd.DataFrame, target_vector: pd.DataFrame):
    diff_array = (np.array(output) - np.array(target_vector))
    return  max(abs(diff_array))

#function to get vector ratio
def calulate_ratio(output: pd.DataFrame, target_vector: pd.DataFrame):
    return (np.array(target_vector) / np.array(output))

#function to get all row info
def get_all_row_info(output: pd.DataFrame, target_vector: pd.DataFrame):
    row_sums = np.sum(output, axis=1)
    row_diff = calulate_diff(row_sums, target_vector)
    row_ratio = calulate_ratio(row_sums,target_vector)

    result_dict = dict()
    result_dict[ROW_SUMS_KEY] = row_sums
    result_dict[ROW_DIFF_KEY] = row_diff  
    result_dict[ROW_RATIO_KEY] = row_ratio

    return result_dict

#function to get all column info
def get_all_col_info(output: pd.DataFrame, target_vector: pd.DataFrame):
    col_sums = np.sum(output, axis=0)
    col_diff = calulate_diff(col_sums, target_vector)
    col_ratio = calulate_ratio(col_sums, target_vector)

    result_dict = dict()
    result_dict[COL_SUMS_KEY] = col_sums
    result_dict[COL_DIFF_KEY] = col_diff  
    result_dict[COL_RATIO_KEY] = col_ratio

    return result_dict

# ras_matrices = ri.read_input()
# output = ras_matrices.df_matrix_coeff
# target = ras_matrices.df_matrix_consumption
# print(output)
# print(target)
# col_sums = np.sum(output, axis=0)
# print(col_sums)


# col_ratio = calulate_ratio(col_sums, target)
# print(col_ratio)
# col_diff = calulate_diff(col_sums, target)
# print(col_diff)

# print(target.shape)
# print(col_sums.shape)