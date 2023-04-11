from MZI import MZI 
import sympy as sym
from sympy import symbols
import numpy as np

for i in range(16):
    input = "{0:04b}".format(i)
    # FOR INPUT X_3_X_2_X_1_X_0 = 0100
    #First MZI X_3
    X_3 = int(input[0])
    X_2 = int(input[1])
    X_1 = int(input[2])
    X_0 = int(input[3])
    #print (X_3,X_2,X_1,X_0)
    print("This is the begining of test: ",input)
    
    print('First MZI S =', X_3 )
    G_o = symbols('G_o')
    Input_1 = sym.Matrix([[1],[G_o]])
    mzi_1 = MZI(X_3,Input_1)
    F_o_F_1 = mzi_1.output
    print(F_o_F_1)
  

    print('---------------------------------------')

    #Second MZI X_2
    print('Second MZI S =', X_2)
    G_3 = F_o_F_1[0][1]
    G_1 = symbols('G_1')
    Input_2 = sym.Matrix([[G_1],[G_3]])
    mzi_2 = MZI(X_2,Input_2)
    F_2_F_3 = (mzi_2.output)
    print(F_2_F_3)

    print('---------------------------------------')

    #Third MZI X_1
    print('Third MZI S =', X_1)
    G_4 = F_2_F_3[0][1]
    G_5 = F_o_F_1[0][0]
    Input_3 = sym.Matrix([[G_4],[G_5]])
    mzi_3 = MZI(X_1,Input_3)
    Z_i_F_4 = (mzi_3.output)
    print(Z_i_F_4)

    print('---------------------------------------')

    #Fourth MZI X_3
    print('Fourth MZI S =', X_3)
    G_6 = symbols('G_6')
    G_7 = Z_i_F_4[0][1]
    Input_4 = sym.Matrix([[G_6],[G_7]])
    mzi_4 = MZI(X_3,Input_4)
    F_5_F_6 = (mzi_4.output)
    print(F_5_F_6)

    print('---------------------------------------')

    #Fifth MZI X_0
    print('Fifth MZI S =', X_0)
    G_8 = F_5_F_6[0][0]
    Input_5 = sym.Matrix([[0], [G_8]])
    mzi_5= MZI(X_0,Input_5)
    F_7_F_8 = (mzi_5.output)
    print (F_7_F_8)

    print('---------------------------------------')

    #Deformed Fifth MZI X_0
    # print('Deformed Fifth MZI S =', X_0)
    # G_8 = F_5_F_6[0][1]
    # Input_5 = sym.Matrix([[0], [G_8]])
    # mziDeform = MZI(2, Input_5)
    # F_7_F_8 = (mziDeform.output)
    # print(F_7_F_8)


    print('---------------------------------------')

    #Using First MZI X_3
    print('First MZI S =', X_3)
    G_6 = F_7_F_8[0][0]
    G_7 = Z_i_F_4[0][1]
    Input_4 = sym.Matrix([[G_6],[G_7]])
    F_5_F_6 = ([mzi_1.matrix_eq*Input_4])
    print(F_5_F_6)

    print('---------------------------------------')

    # Using Second MZI X_2
    print('Second MZI S =', X_2)
    G_1 = F_5_F_6[0][0]
    G_3 = F_o_F_1[0][1]
    Input_2 = sym.Matrix([[G_1],[G_3]])
    F_2_F_3 = ([mzi_2.matrix_eq*Input_2])
    print(F_2_F_3)

    print('---------------------------------------')
    
    # Using Third MZI X_1
    print('Third MZI S =', X_1)
    G_4 = F_2_F_3[0][1]
    G_5 = F_o_F_1[0][0]
    Input_3 = sym.Matrix([[G_4],[G_5]])
    Z_i_F_4 = ([mzi_1.matrix_eq*Input_3])
    print(Z_i_F_4)
    print(np.abs(Z_i_F_4))
    print( "This is the end of the test: ", input)
    print('---------------------------------------')
        
    