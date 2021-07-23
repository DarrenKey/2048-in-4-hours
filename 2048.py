import random
import copy


class Game:
    def __init__(self):
        self.grid = []
        for i in range(4):
            temp = []
            for i in range(4):
                temp.append(0)
            self.grid.append(temp)

        self.generateRandomNum()
        self.generateRandomNum()

    def nonZeroPaths(self):

        paths = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != 0:
                    paths.append([i, j])

        return paths

    def moveDown(self, grid):
        for j in range(4):
            freeNum = -1
            for i in range(3, -1, -1):
                if grid[i][j] == 0 and freeNum == -1:
                    freeNum = i
                elif freeNum == -1:
                    freeNum = i
                elif grid[i][j] != 0:
                    if grid[freeNum][j] == 0:
                        grid[freeNum][j] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[freeNum][j] == grid[i][j]:
                        grid[freeNum][j] += grid[freeNum][j]
                        grid[i][j] = 0
                        freeNum -= 1
                    else:
                        temp = grid[i][j]
                        grid[i][j] = 0
                        grid[freeNum - 1][j] = temp
                        freeNum -= 1

    def moveUp(self, grid):
        for j in range(4):
            freeNum = -1
            for i in range(4):
                if grid[i][j] == 0 and freeNum == -1:
                    freeNum = i
                elif freeNum == -1:
                    freeNum = i
                elif grid[i][j] != 0:
                    if grid[freeNum][j] == 0:
                        grid[freeNum][j] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[freeNum][j] == grid[i][j]:
                        grid[freeNum][j] += grid[freeNum][j]
                        grid[i][j] = 0
                        freeNum += 1
                    else:
                        temp = grid[i][j]
                        grid[i][j] = 0
                        grid[freeNum + 1][j] = temp
                        freeNum += 1

    def moveRight(self, grid):
        for i in range(4):
            freeNum = -1
            for j in range(3, -1, -1):
                if grid[i][j] == 0 and freeNum == -1:
                    freeNum = j
                elif freeNum == -1:
                    freeNum = j
                elif grid[i][j] != 0:
                    if grid[i][freeNum] == 0:
                        grid[i][freeNum] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[i][freeNum] == grid[i][j]:
                        grid[i][freeNum] += grid[i][freeNum]
                        grid[i][j] = 0
                        freeNum -= 1
                    else:
                        temp = grid[i][j]
                        grid[i][j] = 0
                        grid[i][freeNum - 1] = temp
                        freeNum -= 1

    def moveLeft(self, grid):
        for i in range(4):
            freeNum = -1
            for j in range(4):
                if grid[i][j] == 0 and freeNum == -1:
                    freeNum = j
                elif freeNum == -1:
                    freeNum = j
                elif grid[i][j] != 0:
                    if grid[i][freeNum] == 0:
                        grid[i][freeNum] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[i][freeNum] == grid[i][j]:
                        grid[i][freeNum] += grid[i][freeNum]
                        grid[i][j] = 0
                        freeNum += 1
                    else:
                        temp = grid[i][j]
                        grid[i][j] = 0
                        grid[i][freeNum + 1] = temp
                        freeNum += 1

    def changeInputs(self, grid, addingDirection):
        if addingDirection == "d":
            self.moveDown(self.grid)

        elif addingDirection == "u":
            self.moveUp(self.grid)

        elif addingDirection == "r":
            self.moveRight(self.grid)

        elif addingDirection == "l":
            self.moveLeft(self.grid)

    def generateRandomNum(self):
        zeroPaths = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    zeroPaths.append((i, j))

        if len(zeroPaths) > 0:
            path = random.sample(zeroPaths, 1)[0]

            self.grid[path[0]][path[1]] = 2

    def singlePass(self, moveInput):
        grid = self.grid

        tempGrid = copy.deepcopy(grid)

        tempGridDown = copy.deepcopy(grid)
        self.moveDown(tempGridDown)

        tempGridUp = copy.deepcopy(grid)
        self.moveUp(tempGridUp)

        tempGridRight = copy.deepcopy(grid)
        self.moveRight(tempGridRight)

        tempGridLeft = copy.deepcopy(grid)
        self.moveLeft(tempGridLeft)

        if tempGridDown == grid and tempGridUp == grid and tempGridLeft == grid and tempGridRight == grid:
            print("You lost!!!")

        self.changeInputs(tempGrid, moveInput)

        if grid != tempGrid:
            grid = tempGrid
            self.generateRandomNum()


gameInstance = Game()

gameInstance.grid[0][0] = 2
gameInstance.grid[0][1] = 2
gameInstance.grid[0][2] = 4

while True:
    print("------------grid---------------")
    for i in gameInstance.grid:
        print(i)

    moveInput = input("Next move, d = down, l = left, r = right, u = up")

    gameInstance.singlePass(moveInput)
