processed_data <- paste0(getwd(), "/02_Final")
# Inform user if estimations converged. Save if successful
if (row_info$row_diff > error_accuracy | col_info$col_diff > error_accuracy) {
  stop(paste0("Failed. Estimations didn't converge. \n",
             "Maximum limit of ",  format(MaxIteration, big.mark = ",") ," iterations reached. \n",
             "Total time spent in estimating IO table : ", format(round((time_spent["elapsed"]/60),2), big.mark = ","), " minutes \n",
             "Max Absoulte Row difference: ", format(row_info$row_diff, big.mark = ","), "\n",
             "Max Absoulte Col difference: ", format(col_info$col_diff, big.mark = ",")))
} else {
  filename <- paste0(processed_data, "/IO_table_", nrow(temp_output), "_x_",  ncol(temp_output),"_", format(Sys.Date(), "%Y%m%d"),".xlsx")
  cat(paste0("Success. Estimations converged. \n",
              "Total number of iterations: ", format(Iteration, big.mark = ","), "\n",
              "Total time spent in estimating IO table : ", format(round((time_spent["elapsed"]/60),2), big.mark = ","), " minutes \n",
              "IO table saved as ", filename))
  final_output <- as.data.frame(temp_output)
  matrix_input <- as.vector(df_matrix_output)
  final_coeff <- as.data.frame(plyr::aaply(temp_output, 1, "/", matrix_input))
  colnames(final_output) <- 1:ncol(final_output)
  colnames(final_coeff) <- 1:ncol(final_coeff)
  final_output$Industry <- 1:nrow(final_output)
  final_coeff$Industry <- 1:nrow(final_coeff)
  final_output <- final_output[c("Industry", setdiff(names(final_output), "Industry"))]
  final_coeff <- final_coeff[c("Industry", setdiff(names(final_coeff), "Industry"))]
  write_xlsx(list("New IO Table" = final_output, "New IO Table - Tech Coeff" = final_coeff), filename)
}

