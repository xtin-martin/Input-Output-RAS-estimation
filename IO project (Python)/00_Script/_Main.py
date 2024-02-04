#Libraries
import read_input as ri
import converge as co
import save_output as so

#Parameter Settings
max_iteration = 100 #Change to how many attempts you are willing to estimate the table
error_accuracy= 0.0001 #Change to how much difference the estimated table would have vs your given
input_path = "C:\\Users\\kristine.martin\\OneDrive - Interpublic\\Desktop\\Python\\IO project (Python)\\01_Input\\"
output_path = "C:\\Users\\kristine.martin\\OneDrive - Interpublic\\Desktop\\Python\\IO project (Python)\\02_Result\\"
output_filename = ""

#Reading and pre-processing of inputs
ras_matrices = ri.read_input(input_path)

#RAS estimation
result = co.converge(max_iteration, error_accuracy, ras_matrices)

#Save
so.save(result, output_path, output_filename)