import datetime as dt
import pandas as pd
import os
from pathlib import Path
#pip install XlsxWriter

def save (result, output_path: Path, output_filename: str):

    if (result.get_is_successful()):
        output_directory =  output_path
        file = output_directory + output_filename + dt.datetime.now().strftime("%Y%m%d") + ".xlsx"
        filepath = os.path.join(output_directory, file)
        result_current_output = pd.DataFrame(result.current_output )
        result_matrix_tech_coeff = pd.DataFrame(result.matrix_tech_coeff)

        with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
            # Write each DataFrame to a different Excel sheet
            result_current_output.to_excel(writer, sheet_name='New IO table', index=False, header = False)
            result_matrix_tech_coeff.to_excel(writer, sheet_name='New IO table - Tech Coeff', index=False,  header = False)

        print(f"Success. Estimations converged. \nIO table saved as {filepath}")
    
    else:
        raise("Failed. Estimations did not converge.")




