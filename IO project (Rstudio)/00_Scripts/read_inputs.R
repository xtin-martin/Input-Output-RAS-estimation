
#Set raw data and processed
raw_data <- paste0(getwd(), "/01_Input")

# Read input files and transform into matrices and vectors

df_coeff <- suppressMessages(readxl::read_excel(paste0(raw_data, "\\Base Year - Technical Coefficient matrix.xlsx"), skip = 6, col_names = FALSE))
df_matrix_coeff <- as.matrix(df_coeff[,-1])
df_total_consumption <- suppressMessages(readxl::read_excel(paste0(raw_data, "\\Target Year - Total Intermediate Input.xlsx"),  skip = 6, col_names = FALSE))
df_matrix_consumption <- as.numeric(df_total_consumption[,-1])
df_total_intermediate_demand <- suppressMessages(readxl::read_excel(paste0(raw_data, "\\Target Year - Total Intermediate Demand.xlsx"),  skip = 6, col_names = FALSE))
df_matrix_intermediate_demand <- as.numeric(df_total_intermediate_demand[[2]])
df_total_output <- suppressMessages(readxl::read_excel(paste0(raw_data, "\\Target Year - Total Output.xlsx"),  skip = 6, col_names = FALSE))
df_matrix_output <- as.numeric(df_total_output[[2]])
  
# Check if sizes of the inputs are the same
data_structures <- list(
  list(name = "df_matrix_consumption", data = df_matrix_consumption),
  list(name = "df_matrix_intermediate_demand", data = df_matrix_intermediate_demand),
  list(name = "df_matrix_output", data = df_matrix_output)
)

if (ncol(df_matrix_coeff) != nrow(df_matrix_coeff)){
  stop(paste("ERROR: Technical Coefficient is not a square matrix. Please check.\n"))
} else{
  cat(paste("df_matrix_coeff successfully read. \n"))
}

num_cols_coeff <- ncol(df_matrix_coeff)
# Iterate through data structures and check for discrepancies
for (structure in data_structures) {
  num_rows <- length(structure$data)
  
  if (num_cols_coeff != num_rows) {
    stop(paste("ERROR: The number of rows in", structure$name, "is not equal to the number of columns in df_matrix_coeff. Please check.\n"))
  } else{
    cat(paste0(structure$name, " successfully read. \n"))
  }
}
