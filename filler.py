import random as rand

#The same number cannot exist in the same row, column, or cluster

def fillList(): #use the rules of sudoku to fill in the 2d array use helper methods
    sudoku=[[rand.randint(1,9) for _ in range(9)] for _ in range(9)]
    rowRule(sudoku)
    return sudoku

def rowRule(sudoku):
    for row in range(len(sudoku)): #each row in sudoku
        for col in range(len(sudoku[0])): # each column number in the row
            temp=sudoku[row][col] #temporary number holding the position of row and columns
            #print("temp is: "+str(temp))
            if temp!= 0:
                for i in range(col+1,len(sudoku[0])):#check the rest of the values in the row
                    if temp == sudoku[row][i]:#replace the duplicate with 0
                        sudoku[row][i]=0
    return sudoku

def colRule():
    print()

def clusterRule():
    print()