#runs the files

from board import makeBoard
from grid import fillGrid

nums = [[1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2]]# used to test 

fill=fillGrid()

makeBoard(nums)#make sure boarder is handling the entire 2d list
print()
makeBoard(fill)