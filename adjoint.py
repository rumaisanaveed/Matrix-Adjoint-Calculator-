def inputMatrix():
    rows = int(input("Enter number of rows of matrix:"))
    cols = int(input("Enter number of columns of matrix:"))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            number = float(input(f"Enter the number for row {i+1} and column {j+1}:"))
            row.append(number)
        matrix.append(row)
    return matrix

def findMinor(mat,x,y):
    ans = []
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if row == col: # make sure to only make 1 only the diagonal elements
                pe = mat[row][col]
                ans.append(pe)  # Stores the diagonal elements
                if pe != 0:
                    for r in range(len(mat[0])):
                        mat[row][r] = round(mat[row][r] / pe, 3)
                    for j in range(len(mat)):
                        if j > row:
                            makeZero = mat[j][col]
                            for k in range(len(mat[0])):
                                mat[j][k] = round(mat[j][k] - mat[row][k] * makeZero, 3)
    result = 1
    # This part mutliplies the diagonal numbers
    for r in range(len(ans)):
        result *= ans[r]
    res = round(result)
    # This part checks for the sign of the cofactor
    signOfCofactor = x + y
    if signOfCofactor % 2 == 0:
        return res
    else:
        res *= -1
        return res

def printMatrix(adjMatrix):
    print("The adjoint of the given matrix is:")
    for i in adjMatrix:
        for j in i:
            print("%10.3F" % j, end=" ")
        print()

def transposeMatrix(coMatrix,oMatrix):
    adjointMatrix = []
    for i in range(len(coMatrix)):
        rows = []
        for j in range(len(oMatrix[0])):
            num = coMatrix[j][i]
            rows.append(num)
        adjointMatrix.append(rows)
    return adjointMatrix

def findAdjoint():
    # This will take matrix as input
    m = inputMatrix()
    '''This code first go through each element of matrix,and delete it's row and column and finds the
    determinant of the new obtained matrix.And,if the row + column is even,then don't change the sign of determinant 
    otherwise,change the sign of determinant '''
    cofactorMatrix = [] # It stores the minors of every position i,j
    for i in range(len(m)):
        r = []
        for j in range(len(m[0])):
            newMinorMatrix = [] # It returns a new minor matrix for each number
            for k in range(len(m)):
                row = []
                for l in range(len(m[0])):
                    if k == i: # It is for the deletion of row
                        continue
                    elif l == j: # It is for the deletion of column
                        continue
                    else:
                        row.append(m[k][l])
                if row != []:
                    newMinorMatrix.append(row)
            # It returns the cofactor of every position i,j
            Cofactor = findMinor(newMinorMatrix, i, j)
            r.append(Cofactor)
        cofactorMatrix.append(r)
    # It will return the transpose of cofactor matrix
    adjointMatrix = transposeMatrix(cofactorMatrix,m)
    # It will print the result to the screen
    printMatrix(adjointMatrix)

findAdjoint()
