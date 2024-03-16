#runs the files

from board import makeBoard
from filler import fillList

nums = [[1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2],
        [1,2,3,4,5,6,7,8,9,],[2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2]]

fill=fillList()

makeBoard(nums)
print()
makeBoard(fill)