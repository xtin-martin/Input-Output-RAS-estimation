# Library------------------------------------------------------------------------------------
if(!require(readxl)){suppressMessages(install.packages("readxl")); library(readxl)}
if(!require(writexl)){suppressMessages(install.packages("writexl")); library(writexl)}
if(!require(utils)){suppressMessages(install.packages("utils")); library(utils)}
if(!require(plyr)){suppressMessages(install.packages("plyr")); library(plyr)}

# Define functions
diagonalize_vector <- function(vector) {
  if (!is.vector(vector) || !is.vector(vector, mode = "numeric")) {
    stop("Input must be a numeric column vector.")
  }
  diagonal_matrix <- diag(vector)
  return(as.matrix(diagonal_matrix))
}

calculate_output <- function(coeff_matrix, diag_matrix) {
  return(coeff_matrix %*% diag_matrix)
}

calculate_diff <- function(output, target_vector) {
  return(max(abs(output - target_vector)))
}

calculate_ratio <- function(target_vector, output) {
  return(target_vector/output)
}

calculate_row_diff_ratio <- function(output, target) {
  row_sum <- rowSums(output)
  row_diff <- calculate_diff(row_sum, target)
  row_ratio <- calculate_ratio(target, row_sum)
  return(list(row_sum = row_sum, row_diff = row_diff, row_ratio = row_ratio))
}

calculate_col_diff_ratio <- function(output, target) {
  col_sum <- colSums(output)
  col_diff <- calculate_diff(col_sum, target)
  col_ratio <- calculate_ratio(target, col_sum)
  return(list(col_sum = col_sum, col_diff = col_diff, col_ratio = col_ratio))
}

