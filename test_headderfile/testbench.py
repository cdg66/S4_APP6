from C_header import *
import numpy as  np
array = np.arange(0,100,1)
PY2C(array,filename='coefficient.h',Ctype='int',PYtype=int)