from sympy import *
import numpy as np
  
class MZI:
    def __init__(self, top_row, bot_row): #Could pass in a deformity variable def
        self.phi_1 = np.pi
        self.phi_2 = 0
        self.r = 1
        self.matrix_eq = Matrix([top_row,bot_row])
        
        
    def multiply(self, mzi_matrix):
        
        return self.matrix_eq.multiply(mzi_matrix.matrix_eq)

    #
    # Can add useful information here later
    #

