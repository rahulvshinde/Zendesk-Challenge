#!/usr/bin/python

#createRandomMatrix(): function definition to generate a sample 4x4 matrix  
def createRandomMatrix():   
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print "\nThe original Matrix:"    
    displayMatrix(matrix)    
    return matrix

#displayMatrix(): function definition to display the matrix in well - formatted manner
def displayMatrix(mymatrix):
    for row in mymatrix:         
        for val in row:
            #print the matrix in a NxN format
            print '{:4}'.format(val),  
        print

# rotateMatrix(): function definition to rotate a NxN matrix in 90 degree
def rotateMatrix(mymatrix):
    # Gets the length of the matrix
    length = len(mymatrix)  
    # The outer for loop to iterate rows in the matrix 
    for i in range(length/2):  
        j = i
        last = length - i - 1 
        # The inner for loop to iterate columns in the row  
        for j in range(i, last):    
            
            # Saves the top row first element in a temp variable
            temp = mymatrix[i][j]   
            
            # Puts element from left row bottom position to top row first position                                                        
            mymatrix[i][j] = mymatrix[length-1-j][i]   

            # Puts element from bottom row last position to bottom row first position
            mymatrix[length-1-j][i] = mymatrix[length-1-i][length-1-j]  

            # Puts element from first row last position to bottom row last position
            mymatrix[length-1-i][length-1-j] = mymatrix[j][length-1-i]

            # Puts value from temp variable at first row last position
            mymatrix[j][length-1-i] = temp

    print "\nThe 90 degree rotated Matrix:"
    displayMatrix(mymatrix)
    return mymatrix

mymatrix = createRandomMatrix()
rotateMatrix(mymatrix)

