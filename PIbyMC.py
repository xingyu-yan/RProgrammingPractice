#!/usr/local/bin/python3.4
# encoding: utf-8
'''
@author: xingyu, created on December 5, 2016, at Ecole Centrale de Lille
https://github.com/xingyu-yan

This program is for PI estimation with Monte Carlo simulation

General Idea: we will simulate a square with a circle inscribing it.
The square area = a^2, and the circle area = (pi*x^2)/4. 
Thus the ratio of circle to square is equal to pi/4. 
Therefore, if we can get the ratio, and multiply it by 4, we will have the value of pi.
To get the ratio, certain number of points will be randomly placed inside the geometric object
and see where each point lands. 
As the number of random placements increases, we'll get closer and closer to the ratio.
'''

import numpy 
import matplotlib.pyplot as plt

N_total = 10000
#The larger this number is, the more accurate the estimation will be 
#However, it will take more time 
N_in_circle = numpy.zeros(N_total)
estimatePI =  numpy.zeros(N_total)

for i in range(N_total):
    
    #Randomly initialize each point, with the central point (0,0) 
    #and the range is [a, b]
    a = -1
    b = 1
    X = a + (b-a)*numpy.random.random(1)
    Y = a + (b-a)*numpy.random.random(1)    
    
    #Calculate the distance between the generated point and central point (0,0)
    #If it is in the circle, noted 1; otherwise, noted 0
    DistenceN = X**2 + Y**2
    if DistenceN < 1:
        N_in_circle[i] = 1
    else:
        N_in_circle[i] = 0
    
    #Calculate the estimation of PI
    estimatePI[i] = 4*sum(N_in_circle[:])/(i+1) # i is from 0 to (N_total-1)

EstimatePI = 4*sum(N_in_circle)/N_total
print('Estimation of PI is %f' % EstimatePI)
  
#Plot the result  
plt.figure(1)
plt.plot(estimatePI)
plt.title('N= %d ' ' Estimate of PI = %f' % (N_total,estimatePI[N_total-1]))
plt.ylabel('Estimation of PI')
plt.xlabel('Number of Iteration')
plt.show()    
