# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:33:15 2017

@author: JoeWork
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:01:27 2017

@author: JoeWork
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:08:23 2017

@author: JoeWork
"""

import numpy as np
import matplotlib.pyplot as plt 
import scipy
from scipy import interpolate 
import pandas as pd 
import os  
from scipy.interpolate import spline

os.chdir('C:/Users/JoeWork/AnacondaProjects/')
df=pd.read_excel('C:/Users/JoeWork/AnacondaProjects/example.xlsx')

#include rows and columns within array
df.definedarea=df.iloc[0:31, 0:4]

#replace datetime index
dftimeindex=df.definedarea.ix[:,0]=[ 0.32, 0.66 , 0.99 , 1.32 , 1.66 , 1.99 , 2.32 , 2.66 , 2.99 , 3.32 , 3.66 , 3.99 , 4.32 , 4.66 , 4.99 , 5.32 , 5.66 , 5.99 , 6.32 , 6.66 ,
 6.99 , 7.32 , 7.66 , 7.99 , 8.32 , 8.66 , 8.99 , 9.32 , 9.66 , 9.99,  10.32]

#array as floats
floatarray=df.definedarea.astype(float)

#define x as time colum
x=floatarray['A1']
y=floatarray['B2']
#linesmoother
xnew = np.linspace(x.min(),x.max(),1000) #101 represents number of points to make between T.min and T.max

#loop for interpolate

#spline + Crit finder
smooth=interpolate.interp1d(x,y, kind='cubic')
plt.plot(x,y,'o',xnew,smooth(xnew),'-')
