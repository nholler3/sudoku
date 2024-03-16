#creates the sudoku board

def makeBoard(nums):
    for i in range(len(nums)):
        if i % 3 ==0:
            print("-------------------------")


        print("|", end=" ") #vertical line at the beginning
        
        for j in range(len(nums[0])):
            if j%3==0 and j!=0:
                print("|", end=" ") #vertical line at the end

            if j==8:
                print(str(nums[i][j]) + " |") #print last number and frame + move to the next line
            else:
                print(nums[i][j], end=" ") #prints the number
    print("-------------------------")