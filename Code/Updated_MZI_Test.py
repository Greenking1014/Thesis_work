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
print('First MZI S = X_3')
G_o = symbols('G_o')
Input = sym.Matrix([[1],[G_o]]) # [1] goes to P and [G_o] goes to q
mzi_1 = MZI(0,Input)
print(mzi_1.name)
print(mzi_1.matrix_eq)

F_o_F_1 =(mzi_1.output)
print(F_o_F_1)

print('---------------------------------------')

#Second MZI X_2
print('Second MZI S = X_2')
G_3 = F_o_F_1[0][1]
G_1 = symbols('G_1')
Input_2 = sym.Matrix([[G_1],[G_3]])
mzi_2 = MZI(1,Input_2)
print(mzi_2.name)
print(mzi_2.matrix_eq)
F_2_F_3 = (mzi_2.output)
print(F_2_F_3)

print('---------------------------------------')

#Third MZI X_1
print('Third MZI S = X_1')
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix([[G_4],[G_5]])
print(Input_3)
mzi_3 = MZI(0,Input_3)
print(mzi_3.name)
print(mzi_3.matrix_eq)
Z_i_F_4 = (mzi_3.output)
print(Z_i_F_4)

print('---------------------------------------')

#Fourth MZI X_3
print('Fourth MZI S = X_3')
G_6 = symbols('G_6')
G_7 = Z_i_F_4[0][1]
Input_4 = sym.Matrix([[G_6],[G_7]])
mzi_4 = MZI(0,Input_4)
print(mzi_4.name)
print(mzi_4.matrix_eq)
F_5_F_6 = (mzi_4.output)
print(F_5_F_6)

print('---------------------------------------')

# #Fifth MZI S = X_0
# print('Fifth MZI S = X_0')
# G_8 = F_5_F_6[0][0]
# Input_5 = sym.Matrix([[0], [G_8]])
# mzi_5= MZI(0,Input_5)
# print(mzi_5.name)
# print(mzi_5.matrix_eq)
# F_7_F_8 = (mzi_5.output)
# print (F_7_F_8)

# print('---------------------------------------')

#Deformed Fifth MZI X_0
print('Deformed Fifth MZI S = X_0')
G_8 = F_5_F_6[0][1]
Input_5 = sym.Matrix([[0], [G_8]])
mzi_5_Defor = MZI(2,Input_5)
print(mzi_5_Defor.name)
print(mzi_5_Defor.matrix_eq)
F_7_F_8 = (mzi_5_Defor.output)
print(F_7_F_8)

print('---------------------------------------')

#Using First MZI X_3
print('First MZI S = X_3')
G_6 = F_7_F_8[0][0]
G_7 = Z_i_F_4[0][1]
Input_4 = sym.Matrix([[G_6],[G_7]])
F_5_F_6 = ([mzi_1.matrix_eq*Input_4])  # Uses the first mzi matrix equation
                                #Should I keep it this way to make sure no new Mzi.
                                # also how does this translate to the file reader? 
                                # there is an order it goes in so how can i make sure it follows that order?
                                
print(F_5_F_6)

print('---------------------------------------')

# Using Second MZI X_2
print('Second MZI S = X_2')
G_1 = F_5_F_6[0][0]
G_3 = F_o_F_1[0][1]
Input_2 = sym.Matrix([[G_1],[G_3]])
F_2_F_3 = ([mzi_2.matrix_eq*Input_2])
print(F_2_F_3)

print('---------------------------------------')

# Using Third MZI X_1
print('Third MZI S = X_1')
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix([[G_4],[G_5]])
Z_i_F_4 = ([mzi_3.matrix_eq*Input_3])
#print(Z_i_F_4)
print(np.abs(Z_i_F_4))
