from MZI import MZI 
import sympy as sym
from sympy import symbols
import numpy as np


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
print('First MZI X_3')
G_o = symbols('G_o')
Input = sym.Matrix([[1],[G_o]])
mziX_3 = MZI(0,Input,None)
print(mziX_3.name)
print(mziX_3.matrix_eq)

F_o_F_1 =(mziX_3.f_Output)
print(F_o_F_1)

print('')

#Second MZI X_2
print('Second MZI X_2')
G_3 = F_o_F_1[0][1]
G_1 = symbols('G_1')
Input_2 = sym.Matrix([[G_1],[G_3]])
mziX_2 = MZI(1,None,Input_2)
print(mziX_2.name)
print(mziX_2.matrix_eq)
F_2_F_3 = (mziX_2.g_Output)
print(F_2_F_3)