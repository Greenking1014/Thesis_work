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
mziX_3 = MZI(0)
print(mziX_3.matrix_eq)
Input_1 = sym.Matrix([[1],[G_o]])
F_o_F_1 =([mziX_3.matrix_eq*Input_1])
print(F_o_F_1)

print('')

#Second MZI X_2
print('Second MZI X_2')
G_3 = F_o_F_1[0][1]
G_1 = symbols('G_1')
mziX_2 = MZI(1)
Input_2 = sym.Matrix([[G_1],[G_3]])
print(Input_2)
F_2_F_3 = ([mziX_2.matrix_eq*Input_2])
print(F_2_F_3)

print('')

#Third MZI X_1
print('Third MZI X_1')
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix([[G_4],[G_5]])
print(Input_3)
mziX_1 = MZI(0)
Z_i_F_4 = ([mziX_1.matrix_eq*Input_3])
print(Z_i_F_4)

print('')

#Fourth MZI X_3
print('Fourth MZI X_3')
G_6 = symbols('G_6')
G_7 = Z_i_F_4[0][1]
Input_4 = sym.Matrix([[G_6],[G_7]])
F_5_F_6 = ([mziX_3.matrix_eq*Input_4])
print(F_5_F_6)

print('')

#Fifth MZI X_0
print('Fifth MZI X_0')
G_8 = F_5_F_6[0][0]
Input_5 = sym.Matrix([[0], [G_8]])
mziX_0= MZI(0)
F_7_F_8 = ([mziX_0.matrix_eq*Input_5])
print (F_7_F_8)

# #Deformed X_o matrix
# print('Deformed X_o matrix')
# mziDef_X_o = MZI(2)
# print(mziDef_X_o.matrix_eq)
# np.abs(mziDef_X_o.matrix_eq)

print('')

#Deformed Fifth MZI X_0
print('Deformed Fifth MZI X_0')
G_8 = F_5_F_6[0][1]
Input_5 = sym.Matrix([[0], [G_8]])
mziDeforX_0 = MZI(2)
F_7_F_8 = ([mziDeforX_0.matrix_eq*Input_5])
print(F_7_F_8)
print(np.abs(F_7_F_8))

print('')

#Fourth MZI X_3
print('Fourth MZI X_3')
G_6 = F_7_F_8[0][0]
G_7 = Z_i_F_4[0][1]
Input_4 = sym.Matrix([[G_6],[G_7]])
F_5_F_6 = ([mziX_3.matrix_eq*Input_4])
print(F_5_F_6)
print(np.abs(F_5_F_6))

print('')

#Second MZI X_2
print('Second MZI X_2')
G_1 = F_5_F_6[0][0]
G_3 = F_o_F_1[0][1]
Input_2 = sym.Matrix([[G_1],[G_3]])
F_2_F_3 = ([mziX_2.matrix_eq*Input_2])
print(F_2_F_3)
print(np.abs(F_2_F_3))

print('')
#Third MZI X_1
print('Third MZI X_1')
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix([[G_4],[G_5]])
Z_i_F_4 = ([mziX_1.matrix_eq*Input_3])
print(Z_i_F_4)
print(np.abs(Z_i_F_4))