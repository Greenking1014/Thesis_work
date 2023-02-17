
# MZI matrix
from sympy import *
import numpy as np
import math
import time
import cmath
#start = time.time()
phi_1 = np.pi
phi_2 = 0
x = complex(0,1)
r = 1
matrix1 =Matrix ([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

matrix_2 =Matrix( [[-1,0],
            [0,1]])
result = matrix_2.multiply(matrix1)
print(result)
matrix3 = Matrix([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

mzi_output_1 = matrix3.multiply(result)
print("Matrix MZI bar_configuration (S=0)", mzi_output_1)
#print (mzi_output_1[0,0])


# In[2]:


# MZI matrix
# MZI matrix
from sympy import *
import numpy as np
import math
import cmath
phi_1 = np.pi
phi_2 = 0
x = complex(0,1)
r = 1
matrix1 =Matrix ([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

matrix_2 =Matrix( [[1,0],
            [0,1]])
result = matrix_2.multiply(matrix1)
print(result)
matrix3 = Matrix([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

mzi_output_2 = matrix3.multiply(result)
print("Matrix MZI cross_configuration (S=1)", mzi_output_2)


# In[3]:


# FOR INPUT X_3_X_2_X_1_X_0 = 0100
#First MZI X_3
import sympy as sym
from sympy import symbols
G_o= symbols('G_o')
#G_o = 0
X_3 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
print (X_3)
Input_1 = sym.Matrix([[1],[G_o]])
F_o_F_1 =([X_3*Input_1])
print(F_o_F_1)


# In[4]:


#Second MZI X_2
#Second MZI X_2
F_1 = F_o_F_1[0][1]
print(F_o_F_1[0][1])
G_3 = F_1
print(G_3)
G_1 = symbols('G_1')
#G_1 = 0
X_2 = sym.Matrix([[mzi_output_2[0,0],mzi_output_2[0,1]],[mzi_output_2[1,0],mzi_output_2[1,1]]])
#print(X_2)
Input_2 = sym.Matrix([[G_1],[G_3]])
print(Input_2)
F_2_F_3 = ([X_2*Input_2])
print(F_2_F_3)


# In[5]:


#Third MZI X_1
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix ([[G_4],[G_5]])
print(Input_3)
X_1 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
Z_i_F_4 = ([X_1*Input_3])
print(Z_i_F_4)


# In[6]:


#Fourth MZI X_3
G_6 = symbols('G_6')
G_7 = Z_i_F_4[0][1]
#G_7 = 0
Input_4 = sym.Matrix ([[G_6],[G_7]])
X_3 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
F_5_F_6 = ([X_3*Input_4])
print(F_5_F_6)


# In[7]:


#Fifth MZI X_0
G_8 = F_5_F_6[0][0]
Input_5 = sym.Matrix ([[0],[G_8]])
X_0 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
F_7_F_8 =  ([X_0*Input_5])
print(F_7_F_8)
#np.abs(F_7_F_8)


# In[8]:


#Deformed X_o matrix

from sympy import *
import numpy as np
import math
import cmath
phi_1 = 2.4
#phi_2 = 0
#phi_2 = 0.6
x = complex(0,1)
r = 1
matrix1 =Matrix ([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

#matrix_2 =Matrix( [[-1,0],
#            [0,1]])
#matrix_2 = Matrix([[cmath.rect(r,phi_1), 0],[0, cmath.rect(r,-phi_2)]])
matrix_2 = Matrix([[cmath.rect(r,phi_1), 0],[0, cmath.rect(r,0)]])
result = matrix_2.multiply(matrix1)
print(result)
matrix3 = Matrix([[0.707, -0.707*x], 
           [-0.707*x, 0.707]])

mzi_output_1_deformed = matrix3.multiply(result)
print("Matrix MZI bar_configuration (S=0)", mzi_output_1_deformed)
#print (mzi_output_1[0,0])
np.abs(mzi_output_1_deformed)


# In[12]:


#Deformed Fifth MZI X_0
G_8 = F_5_F_6[0][1]
Input_5 = sym.Matrix ([[0],[G_8]])
X_0 = sym.Matrix([[mzi_output_1_deformed [0,0],mzi_output_1_deformed [0,1]],[mzi_output_1_deformed [1,0],mzi_output_1_deformed [1,1]]])
F_7_F_8 =  ([X_0*Input_5])
print(F_7_F_8)
np.abs(F_7_F_8)


# In[14]:


#Fourth MZI X_3
G_6 = F_7_F_8[0][0]
#under ideal condition G_7 = 1
#G_7 = 1
#Fourth MZI X_3
#G_6 = symbols('G_6')
G_7 = Z_i_F_4[0][1]
#G_7 = 0
Input_4 = sym.Matrix ([[G_6],[G_7]])
X_3 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
F_5_F_6 = ([X_3*Input_4])
print(F_5_F_6)
np.abs(F_5_F_6)


# In[16]:


#Second MZI X_2
G_1 = F_5_F_6[0][0]
G_3 = F_o_F_1[0][1]
#Second MZI X_2
#F_1 = F_o_F_1[0][1]
#print(F_o_F_1[0][1])
#G_3 = F_1
#print(G_3)
#G_1 = symbols('G_1')
#G_1 = 0
X_2 = sym.Matrix([[mzi_output_2[0,0],mzi_output_2[0,1]],[mzi_output_2[1,0],mzi_output_2[1,1]]])
#print(X_2)
Input_2 = sym.Matrix([[G_1],[G_3]])
print(Input_2)
F_2_F_3 = ([X_2*Input_2])
print(F_2_F_3)
np.abs(F_2_F_3)


# In[17]:


#Third MZI X_1
G_4 = F_2_F_3[0][1]
G_5 = F_o_F_1[0][0]
Input_3 = sym.Matrix ([[G_4],[G_5]])
print(Input_3)
X_1 = sym.Matrix([[mzi_output_1[0,0],mzi_output_1[0,1]],[mzi_output_1[1,0],mzi_output_1[1,1]]])
Z_i_F_4 = ([X_1*Input_3])
print(Z_i_F_4)
np.abs(Z_i_F_4)


# In[ ]:




