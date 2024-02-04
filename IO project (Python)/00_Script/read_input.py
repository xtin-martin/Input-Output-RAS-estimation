import pandas as pd
import numpy as np
from pathlib import Path
#pip install openpyxl

class RASMatrices:

    def __init__(self, df_matrix_coeff: pd.DataFrame, df_matrix_consumption: pd.DataFrame, df_matrix_intermediate_demand: pd.DataFrame, df_matrix_output: pd.DataFrame) -> None:
        
        self.df_matrix_coeff = df_matrix_coeff
        self.df_matrix_consumption = df_matrix_consumption
        self.df_matrix_intermediate_demand = df_matrix_intermediate_demand
        self.df_matrix_output = df_matrix_output
    
    # TODO: check whether sizes match

#get current working directory
def read_input(input_path: Path) -> None:
    """
    Read input excel files "Base Year - Technical Coefficient matrix", "Target Year - Total Intermediate Demand", 
    "Target Year - Total Intermediate Input", and "Target Year - Total Output" 
    from folder 
    """

    current_directory =  input_path

    # Read input files and transform into DataFrames
    df_coeff = pd.read_excel(current_directory + "\\Base Year - Technical Coefficient matrix.xlsx", skiprows=6, header=None)
    df_matrix_coeff = df_coeff.iloc[:, 3:].to_numpy()
    
    df_total_consumption = pd.read_excel(current_directory + "\\Target Year - Total Intermediate Input.xlsx", skiprows=6, header=None)
    df_matrix_consumption = df_total_consumption.iloc[:, 3:].to_numpy()
    df_matrix_consumption = df_matrix_consumption.reshape((df_matrix_consumption.size,))

    #print(df_matrix_consumption)
    
    df_total_intermediate_demand = pd.read_excel(current_directory + "\\Target Year - Total Intermediate Demand.xlsx", skiprows=6, header=None)
    df_matrix_intermediate_demand = df_total_intermediate_demand.iloc[:, 3].to_numpy()
    
    df_total_output = pd.read_excel(current_directory + "\\Target Year - Total Output.xlsx", skiprows=6, header=None)
    df_matrix_output = df_total_output.iloc[:, 3].to_numpy()
    
    ras_matrices = RASMatrices(df_matrix_coeff, df_matrix_consumption, df_matrix_intermediate_demand, df_matrix_output)
    return ras_matrices
    




# print(input.df_matrix_coeff)
# print(input.df_matrix_consumption)
# print(input.df_matrix_intermediate_demand)
# print(input.df_matrix_output)
# diag = np.diag(input.df_matrix_output)
# print(diag)
# print(input)


# Check if sizes of the inputs are the same
# num_cols_coeff = df_matrix_coeff.shape[1]
# data_structures = [
    #     {"name": "df_matrix_coeff", "data": df_matrix_coeff},
    #     {"name": "df_matrix_consumption", "data": df_matrix_consumption},
    #     {"name": "df_matrix_intermediate_demand", "data": df_matrix_intermediate_demand},
    #     {"name": "df_matrix_output", "data": df_matrix_output}
    # ]

    # data_structures[1]["data"] 

    # # Iterate through data structures and check for discrepancies
    # for structure in data_structures:
    #     num_rows = len(structure["data"])
    #     if num_cols_coeff != num_rows:
    #         raise "ERROR: The number of rows in {structure['name']} is not equal to the number of columns in df_matrix_coeff. Please check."
    #     else:
    #         print(f"{structure['name']} successfully read.")
    
    # return (data_structures[0]["data"], data_structures[1]["data"], data_structures[2]["data"], data_structures[3]["data"])


# df_matrix_coeff = result[0]
# df_matrix_consumption = result[1]
# df_matrix_intermediate_demand = result[2]
# df_matrix_output = result[3]