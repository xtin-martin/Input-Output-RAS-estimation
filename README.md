# Input-Output-RAS-estimation
Estimates an IO table using RAS methodology using inputs: Technical coefficient for the base year, total demand for the target year, total consumption for the target year and total intermediate demand for the target year. Two programs are created for flexibility: One in R, another in Python.

# Inputs: 
1)	“Technical Coefficient in Base year” denoted as Matrix A(Y0): 

Technical Coefficient is a square matrix of values representing the amount of inputs required from each sector to produce one unit of output in another sector. Mathematically, it is an element of the input-output matrix A, where Aij represents the amount of input from sector i required to produce one unit of output in sector j. 

Given the absence of an available I-O table for the target year, this initial input assumes that the interrelationships between industries remain consistent with those observed in the base year (Y0).

2)	“Total Intermediate Demand in Target year” denoted as Vector U(Y1):

Total Intermediate Demand is a vector representing the sum of all purchases made by industries from other industries to support their production processes. Intermediate inputs are goods and services that are used as inputs in the production process but are not the final output themselves. These inputs include raw materials, components, energy, and services purchased from other industries.

The Total Intermediate Demand in the target year (Y1) serves as the final row industry totals Ri that must be satisfied by the end of the RAS estimation process. Researchers typically obtain this critical data from a range of sources, including national statistical agencies, industry surveys, and economic databases. 

3)	“Total Intermediate Consumption in Target year” denoted by Vector V(Y1): 

Total Intermediate Consumption refers to the portion of intermediate inputs that are consumed or used up in the production process.

The Total Intermediate Consumption in the target year (Y1) serves as the ultimate column industry totals Ci that needs to be met by the end of the RAS estimation process. Similar to total intermediate demand in the target year, total intermediate consumption is typically collected by researchers from sources such as national statistical agencies, industry surveys, and economic databases. 


4)	“Total Output in Target year” denoted by Vector X(Y1): 

This represents the total value of all goods and services produced by an economy, encompassing both final outputs for consumption and intermediate outputs used in production by other industries in the target year. 

After gathering these inputs, technical coefficients A(Y0) and total output X(Y1) are utilized to compute for row sum (Ut) and column sum (Vt) in each iteration t. Subsequently, the iterative adjustment process ensues, aiming for these sums to closely match the pre-determined targets U(Y1) and V(Y1). 
