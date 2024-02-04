# Documentation ----------------------------------------------------------- 
#' @description RAS estimator of a Leontief IO table given:
#' Base Technical Coefficients, Total Intermediate Demand, Total Consumption or Total Intermediate Input and Total Output.
#' @author Kristine Martin [kristine.martin@uap.asia]
#' 
#' Press Ctrl+Enter to run the program. Start at line #10. 
#' Please edit the parameters section as desired.
#' 
# Parameters---------------------------------------------------------------------------------
error_accuracy <- 0.001   # Change to desired difference between the totals of the estimated IO vs given totals. Positive integer only
MaxIteration <- 10000  # Change to maximum number of attempts to solve IO table. Positive whole number only

# Settings ---------------------------------------------------------------------------------
setwd(dirname(rstudioapi::getSourceEditorContext()$path))
source("00_Scripts/libraries_functions.R")

# Pre-processing----------------------------------------------------------------------------
source("00_Scripts/read_inputs.R")

# RAS estimation----------------------------------------------------------------------------
source("00_Scripts/ras_estimation.R")

# Save Output--- ---------------------------------------------------------------------------
source("00_Scripts/save_output.R")





