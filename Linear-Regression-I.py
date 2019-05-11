# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:48:34 2019

@author: Mohamad
"""

#Partial Derivative functions
def theta0PartialDerivative():
    multBy=40.0
    total=temp=0
    
    for i in range(40):
        temp+=theta0
        temp+=theta1*sepalWidth[i]
        temp+=theta2*petalLength[i]
        temp+=theta3*petalWidth[i]
        temp-=sepalLength[i]
        total=total+temp
        temp=0
    return (float(multBy*total))

def theta1PartialDerivative():
    multBy=40.0
    total=temp=0
    
    for i in range(40):
        temp+=theta0
        temp+=theta1*sepalWidth[i]
        temp+=theta2*petalLength[i]
        temp+=theta3*petalWidth[i]
        temp-=sepalLength[i]
        temp*=sepalWidth[i]
        total=total+temp
        temp=0
    return (multBy*total)

def theta2PartialDerivative():
    multBy=40.0
    total=temp=0
    
    for i in range(40):
        temp+=theta0
        temp+=theta1*sepalWidth[i]
        temp+=theta2*petalLength[i]
        temp+=theta3*petalWidth[i]
        temp-=sepalLength[i]
        temp*=petalLength[i]
        total=total+temp
        temp=0
    return (multBy*total)

def theta3PartialDerivative():
    multBy=40.0
    total=temp=0
    
    for i in range(40):
        temp+=theta0
        temp+=theta1*sepalWidth[i]
        temp+=theta2*petalLength[i]
        temp+=theta3*petalWidth[i]
        temp-=sepalLength[i]
        temp*=petalWidth[i]
        total=total+temp
        temp=0
    return (multBy*total)

#Gradient descent function
def gradientDescent():
    alpha=0.5
    global theta0,theta1,theta2,theta3
    theta0After=theta1After=theta2After=theta3After=1
    while(theta0After!=theta0 and theta1After!=theta1 and 
          theta2After!=theta2 and theta3After!=theta3):
        theta0=theta0After
        theta1=theta1After
        theta2=theta2After
        theta3=theta3After

        theta0After=theta0 - (alpha * theta0PartialDerivative())
        theta1After=theta1 - (alpha * float(theta1PartialDerivative()))
        theta2After=theta2 - (alpha * float(theta2PartialDerivative()))
        theta3After=theta3 - (alpha * float(theta3PartialDerivative()))
        
#Testing function
def testModel():
    total=0
    for i in range(40,50):
        prediction=theta0+(theta1*sepalWidth[i])+(theta2*petalLength[i])
        +(theta3*petalWidth[i])
        total+=min(prediction,sepalLength[i])/max(prediction,sepalLength[i])
    return (total/10.0)
#Open file
iris = open("input.txt", "r")

#Create lists for measurement storage
sepalLength=[]
sepalWidth=[]
petalLength=[]
petalWidth=[]

#Read entire file
data =iris.readlines()

#Close file
iris.close()

#Populate measurements lists
for line in data:
    measurements=line.split(" ")
    sepalLength.append(float(measurements[0]))
    sepalWidth.append(float(measurements[1]))
    petalLength.append(float(measurements[2]))
    petalWidth.append(float(measurements[3]))
    
#Create Parameters and prediction list
theta0=theta1=theta2=theta3=accuracy=0
prediction=[]

#Run program
gradientDescent()
accuracy=testModel()
print(accuracy)

#Testing
'''
print(theta0PartialDerivative())
'''
    
    