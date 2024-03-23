#runs the files

from board import makeBoard
from grid import fillGrid
from grid import fillGrid2

nums = [[1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2]]# used to test 

fill=fillGrid()

#print("nums board:")
#makeBoard(nums)#make sure boarder is handling the entire 2d list
#print()
#print("fill board (with row rule): ")
#makeBoard(fill)
#print()
print("fillGrid2 (no need for row rule): ")
makeBoard(fillGrid2())