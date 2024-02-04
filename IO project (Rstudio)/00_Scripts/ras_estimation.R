# Begin calculation here
## Initialize matrices and variables
diag_total_output_matrix <- diagonalize_vector(df_matrix_output)
temp_coeff <- as.matrix(df_matrix_coeff)
temp_output <- calculate_output(temp_coeff, diag_total_output_matrix)
row_info <- calculate_row_diff_ratio(temp_output, df_matrix_intermediate_demand)
col_info <- calculate_col_diff_ratio(temp_output, df_matrix_consumption)
start_time <-  proc.time()
## Start iterations
for (Iteration in 1:MaxIteration) {
  if (row_info$row_diff <= error_accuracy && col_info$col_diff <= error_accuracy) {
    break  # Exit the loop if convergence criteria are met
  }
  
  if (row_info$row_diff > error_accuracy) {
    diagonalize_ratio <- as.matrix(diagonalize_vector(as.numeric(row_info$row_ratio)))
    temp_coeff <- diagonalize_ratio %*% temp_coeff
    temp_output <- calculate_output(temp_coeff, diag_total_output_matrix)
    row_info <- calculate_row_diff_ratio(temp_output, df_matrix_intermediate_demand)
    col_info <- calculate_col_diff_ratio(temp_output, df_matrix_consumption)
  }
  
  if (col_info$col_diff > error_accuracy) {
    diagonalize_ratio <- as.matrix(diagonalize_vector(as.numeric(col_info$col_ratio)))
    temp_coeff <- temp_coeff %*% diagonalize_ratio
    temp_output <- calculate_output(temp_coeff, diag_total_output_matrix)
    row_info <- calculate_row_diff_ratio(temp_output, df_matrix_intermediate_demand)
    col_info <- calculate_col_diff_ratio(temp_output, df_matrix_consumption)
  }
  
  print(paste0("Iteration: ", Iteration, ". Difference between totals: ", format(row_info$row_diff,big.mark = ",")))
    
}
end_time <-  proc.time()
time_spent <- end_time - start_time

