import math
from MZI import MZI 
x = complex(0,1)


mzi1 = MZI([0.707, -0.707*x],[-0.707*x, 0.707])
mzi2 = MZI([-1,0],[0,1])
result = mzi1.multiply(mzi2)
print(result)