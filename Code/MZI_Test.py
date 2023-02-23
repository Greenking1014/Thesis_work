from MZI import MZI 
import sympy as sym
from sympy import symbols


####### Testing Area #######
# Bar config
# mzi1 = MZI(0)

# # Cross config
# mzi2 = MZI(1)

# print(mzi1.name)
# print(mzi1.matrix_eq)
# print(mzi1.matrix_eq[0,0])
# print(mzi2.name)
# print(mzi2.matrix_eq)

####### Testing Area #######

# FOR INPUT X_3_X_2_X_1_X_0 = 0100
#First MZI X_3

G_o = symbols('G_o')
mziX_3 = MZI(0)
print(mziX_3.matrix_eq)
Input_1 = sym.Matrix([[1],[G_o]])
F_o_F_1 =([mziX_3.matrix_eq*Input_1])
print(F_o_F_1)

#Second MZI X_2

G_3 = F_o_F_1[0][1]



