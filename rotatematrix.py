#!/usr/bin/python

import random
random.seed(12345)

#createRandomMatrix(): function definition to take a user input (N) and generate  
#                      NxN matrix using random numbers in the range from 0 - 100. 
def createRandomMatrix():
    n = input("\nEnter N Value for NxN matrix: ")
    maxVal = 100
    matrix = []
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for i in range(n):
        matrix.append([random.randint(0,maxVal) for el in range(n)])
    print "\nThe original Matrix:"    
    displayMatrix(matrix)    
    return matrix

#displayMatrix(): function definition to display the matrix in well - formatted manner
def displayMatrix(mymatrix):
    for row in mymatrix:
        for val in row:
            print '{:4}'.format(val),
        print

# rotateMatrix(): function definition to rotate a NxN matrix in 90 degree
def rotateMatrix(mymatrix):
    length = len(mymatrix)  #gets the length of the matrix
    print length
    for i in range(length/2):   
        j = i
        last = length - i - 1
        for j in range(i, last):
            temp = mymatrix[i][j]
            mymatrix[i][j] = mymatrix[length-1-j][i]
            mymatrix[length-1-j][i] = mymatrix[length-1-i][length-1-j]
            mymatrix[length-1-i][length-1-j] = mymatrix[j][length-1-i]
            mymatrix[j][length-1-i] = temp
    print "\nThe 90 degree rotated Matrix:"
    displayMatrix(mymatrix)
    return mymatrix

mymatrix = createRandomMatrix()
rotateMatrix(mymatrix)

