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
    print()

def clusterRule(sudoku):
    print()

def validateGrid(sudoku):
    rowRule(sudoku)
    colRule(sudoku)
    clusterRule(sudoku)

    #logic for replacing the number and recursive call
    #back tracking algorithm