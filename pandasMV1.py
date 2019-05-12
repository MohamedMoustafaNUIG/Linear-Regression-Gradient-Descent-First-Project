# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:49:59 2019

@author: Mohamad
"""
import pandas as pd

#Read entire file
data = pd.read_csv("input.csv",header=None,names=["sepalLength","sepalWidth"
                                                  ,"petalLength","petalWidth"])
#Squared mean error function partial derivative
def partialDerivative(x):
    multBy=1/40.0
    total=temp=0
    for i in range(0,40):
        temp+=theta[0]
        temp+=theta[1]*data.iloc[i,1]
        temp+=theta[2]*data.iloc[i,2]
        temp+=theta[3]*data.iloc[i,3]
        temp-=data.iloc[i,0]
        if(x==0):
            temp=temp
        else:
            temp=temp*data.iloc[i,x]
        total+=temp
        temp=0
    total=total*multBy
    return total

#Gradient descent function
def gradientDescent():
    alpha=0.13
    global theta
    thetaAfter=[1,1,1,1]
    while(theta[0]!=thetaAfter[0] and theta[1]!=thetaAfter[1] 
    and theta[2]!=thetaAfter[2] and theta[3]!=thetaAfter[3]):
        
        #Simultaneously adjust all parameters
        theta[0]=thetaAfter[0]
        theta[1]=thetaAfter[1]
        theta[2]=thetaAfter[2]
        theta[3]=thetaAfter[3]
        
        #Calculate new parameters
        thetaAfter[0]=theta[0]-(alpha*partialDerivative(0))
        thetaAfter[1]=theta[1]-(alpha*partialDerivative(1))
        thetaAfter[2]=theta[2]-(alpha*partialDerivative(2))
        thetaAfter[3]=theta[3]-(alpha*partialDerivative(3))
        
        #To observe convergence and adjust step(alpha)
        '''
        print(partialDerivative(0))
        print(partialDerivative(1))
        print(partialDerivative(2))
        print(partialDerivative(3))
        '''
#Test trained model on last 10 tuples
def testModel():
    total=0.0
    for i in range(40,50):
        prediction=theta[0]+(theta[1]*data.iloc[i,1])
        +(theta[2]*data.iloc[i,2])+(theta[3]*data.iloc[i,3])
        total+=min(prediction,data.iloc[i,0])/max(prediction,data.iloc[i,0])
    return (total*10.0)

#Program Start
theta=[0,0,0,0]
gradientDescent()
print("accuracy = %f"%testModel())