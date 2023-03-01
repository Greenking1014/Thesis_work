from sympy import *

import cmath
class MZI:
    def __init__(self, config_selection): #Could pass in a deformity variable def
        # self.phi_1 = np.pi
        # self.phi_2 = 0
        self.x = complex(0,1)
        self.r = 1
        if (config_selection == 0):
            matrix1 = Matrix ([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            matrix2 = matrix1.multiply(Matrix( [[-1,0],[0,1]]))
            matrix3 = Matrix([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            self.matrix_eq = matrix2.multiply(matrix3)
            self.name = "Matrix MZI bar_configuration (S=0)"
        elif (config_selection == 1):
            matrix1 = Matrix ([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            matrix2 = matrix1.multiply(Matrix( [[1,0],[0,1]]))
            matrix3 = Matrix([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            self.matrix_eq = matrix2.multiply(matrix3) 
            self.name = "Matrix MZI cross_configuration (S=1)"
        elif (config_selection == 2):
            self.phi_1 = 2.4
            matrix1 = Matrix ([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            matrix2 = Matrix([[cmath.rect(self.r,self.phi_1),0],[0,cmath.rect(self.r,0)]])
            matrix3 = Matrix([[0.707, -0.707*self.x],[-0.707*self.x, 0.707]])
            self.matrix_eq = matrix3.multiply(matrix2.multiply(matrix1)) 
            self.name = "Matrix MZI bar_configuration (S=0) deformed"
        
        
    def multiply(self, mzi_matrix):
        
        return self.matrix_eq.multiply(mzi_matrix.matrix_eq)

    #
    # Can add useful information here later
    #

