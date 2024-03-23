import random as rand

#The same number cannot exist in the same row, column, or cluster

def fillGrid(): #use the rules of sudoku to fill in the 2d array use helper methods
    sudoku=[[rand.randint(1,9) for _ in range(9)] for _ in range(9)]
    validateGrid(sudoku)
    return sudoku

def fillGrid2(): #does not require rowRule (is it more efficient in the long run?) most likely yes, less 0s to fill in
    sudoku = [[0 for _ in range(9)] for _ in range(9)]  # Initialize a 9x9 grid with zeros
    
    for row in range(9):
        validNums = list(range(1, 10))  # List of numbers from 1 to 9
        rand.shuffle(validNums)  # Shuffle the list to get random order
        
        for col in range(9):
            num = validNums.pop()  # Take the last element from the shuffled list
            sudoku[row][col] = num

    validateGrid(sudoku)
    return sudoku

def rowRule(sudoku): #replaces each duplicate number in a row with 0
    for row in range(len(sudoku)): #each row in sudoku
        for col in range(len(sudoku[0])): # each column number in the row
            temp=sudoku[row][col] #temporary number holding the position of row and columns
            if temp!= 0:
                for i in range(col+1,len(sudoku[0])):#check the rest of the values in the row
                    if temp == sudoku[row][i]:#replace the duplicate with 0
                        sudoku[row][i]=0
    return sudoku

def colRule(sudoku):
    for row in range(len(sudoku)): #each row in sudoku
        for col in range(len(sudoku[0])): # each column number in the row
            temp=sudoku[row][col] #temporary number holding the position of current row and column
            if temp!= 0:
                for i in range(row+1,len(sudoku[0])):#check the rest of the values in the column
                    if temp == sudoku[i][col]:#replace the duplicate with 0
                        sudoku[i][col]=0

def clusterRule(sudoku):
    print()

def validateGrid(sudoku):
    rowRule(sudoku)
    colRule(sudoku)
    #clusterRule(sudoku)
    solveGrid(sudoku, 0, 0)
    
def solveGrid(sudoku, row, col):
    #logic for replacing the number and recursive call
    #back tracking algorithm
    if row >= len(sudoku)-1 and col > len(sudoku)-1:#if we hit the end of the final list then exit
        return
    if col > len(sudoku)-1: #if we hit the end of the row
        col=0
        row+=1

    #beginning of backtracking
    if sudoku[row][col] != 0: #if the index is not empty call again with the next column
        print(col)
        return solveGrid(sudoku, row, col+1)
    else: #if the number is 0
        sudoku[row][col]='*' #replace with the * (for tracking purposes)
        #print(col,"hit")
        return solveGrid(sudoku, row, col+1)