#
# Code property of Jared Scarito
#
# http://acmgnyr.org/year2017/problems/C-Capsules.pdf
#
from random import randint
class Solver:
    grid = []
    regions = []
    squares = []
    def __init__(self, grid):
        self.grid = grid
    def addRegion(self, region):
        self.regions.append(region)
    def setupSquaresArray(self):
        for gridRow in range(len(self.grid)):
            for i in range(len(self.grid[gridRow])):
                squareVal = self.grid[gridRow][i]
                squareRow = gridRow
                squareCol = i
                gridSquare = GridSquare(squareRow, squareCol)
                if squareVal != "-":
                    gridSquare.setVal(int(squareVal))
                else:
                    gridSquare.setVal(int(0))
                self.squares.append(gridSquare)
    def setupNumbersAllowed(self):
        for regionRow in range(len(self.regions)):
            for i in range(len(self.regions[regionRow])):
                if i != 0:
                    # The following are all coords for a region
                    if '(' in str(self.regions[regionRow]):
                        numsAllowed = int(self.regions[regionRow][0])
                        coord = self.regions[regionRow][i]
                        for sqIndex in range(len(self.squares)):
                            square = self.squares[sqIndex]
                            if(str(square.getLocation()) == str(coord)):
                                numsAllowedArr = []
                                for numAllowed in range(numsAllowed):
                                    numsAllowedArr.append(numAllowed)
                                square.setNumbersAllowed(numsAllowedArr)
                            self.squares[sqIndex] = square
    def getSquareAt(self, row, col):
        for i in range(len(self.squares)):
            if(self.squares[i].getLocation == (row, col)):
                return self.squares[i]
        return None
    def getSquaresWith(self, numbersAllowed):
        squareArr = []
        for i in range(len(self.squares)):
            if(self.squares[i].getNumbersAllowed() == numbersAllowed):
                squareArr.append(self.squares[i])
        return squareArr
    def solveBT(self):
        for sqIndex in range(len(self.squares)):
            square = self.squares[sqIndex]
            if square.getVal() != 0:
                numToInput = randint(0, (len(square.getNumbersAllowed())-1))
                if(self.isSafe(square, numToInput)):
                    square.setVal(numToInput)
                    if(self.solveBT()):
                        return True
    def isSafe(self, square, inputNumber):
        x = square.getLocation()[0]
        y = square.getLocation()[1]
        left = self.getSquareAt(x, (y - 1))
        right = self.getSquareAt(x, (y + 1))
        bottomRightDig = self.getSquareAt((x + 1), (y + 1))
        bottomLeftDig = self.getSquareAt((x + 1), (y - 1))
        topRightDig = self.getSquareAt((x - 1), (y + 1))
        topLeftDig = self.getSquareAt((x - 1), (y - 1))
        bottom = self.getSquareAt((x + 1), y)
        top = self.getSquareAt((x - 1), y)
        num = int(inputNumber)
        if (left is None or left.getVal() !=num) and (right is None or right.getVal() !=num) and (bottomRightDig is None or bottomRightDig.getVal() !=num) and (bottomLeftDig is
        None or bottomLeftDig.getVal() !=num) and (topRightDig is None or topRightDig.getVal() !=num) and (topLeftDig is None or topLeftDig.getVal() !=num) and (bottom is
        None or bottom.getVal() !=num) and (top is None or top.getVal() !=num):
            return True
        return False
    def getSolutionGrid(self):
        # TODO
class GridSquare:
    row = 0
    col = 0
    val = 0
    numbersAllowed = []
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def setVal(self, val):
        self.val = val
    def getVal(self):
        return self.val
    def getLocation(self):
        return (self.row, self.col)
    def setLocation(self, row, col):
        self.row = row
        self.col = col
    def getNumbersAllowed(self):
        return self.numbersAllowed
    def setNumbersAllowed(self, numbersAllowed):
        self.numbersAllowed = numbersAllowed





testCases = int(input('How many test cases do you want?: \n'))
gridsMaster = []
regionsMaster = []
gridCount = 0
while testCases > 0:
    print("What are the Grid Margins?:")
    gridMargins = str(input()) # 1 3 5
    rowCount = 0
    grids = []
    while rowCount < int(gridMargins[2]):
        grids.append(str(input()))
        rowCount += 1
    gridCount += 1
    # We just got the grid layouts and have them in our grids array
    print("Regon count:")
    regionCount = int(input())
    cout = 0
    regions = []
    print("Regions:")
    while cout < regionCount:
        cout += 1
        regions.append(str(input()))
    regionsMaster.append(regions)
    gridsMaster.append(grids)
    testCases -= 1
# Now we need to solve the dilemma then print it
for i in range(len(gridsMaster)):
    solver = Solver(gridsMaster[i])
    for regionIndex in range(len(regionsMaster[i])):
        region = regionsMaster[i][regionIndex]
        solver.addRegion(region)
    solver.setupSquaresArray()
    solver.setupNumbersAllowed()
    solver.solveBT()
    print(solver.getSolutionGrid())