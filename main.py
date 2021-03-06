import numpy
import random
from tkinter import *
import time
import graphic
from graphic import *


def endgen(grid):
    for j in range(1, len(grid), 2):
        for i in range(1, len(grid[j]), 2):
            if grid[i][j] != grid[1][1]:
                return False
    return True


def grid_creator(grid, maze_size):
    k = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if i % 2 == 0:
                grid[i][j] = -1
            if j % 2 == 0:
                grid[i][j] = -1
            if j == maze_size - 1:
                grid[i][j] = -1
            if i == maze_size - 1:
                grid[i][j] = -1
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] == 0:
                k += 1
                grid[i][j] = k
    grid[1][0] = 1
    grid[maze_size - 2][maze_size - 1] = k
    """for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == -1:
                t.changecell(root, i, j, True)
            else:
                t.changecell(root, i, j, False)
            root.update()
    root.mainloop()"""


def generate_maze(grid, maze_size, complexe):
    finished = False
    grid_creator(grid, maze_size)
    while not endgen(grid):
        x = random.randint(1, maze_size - 2)
        if x % 2 == 0:
            y = random.randint(1, maze_size - 2)
            if y % 2 == 0:
                if x == 1:
                    x += 1
                    cell1 = grid[y - 1][x]
                    cell2 = grid[y + 1][x]
                else:
                    x -= 1
                    cell1 = grid[y - 1][x]
                    cell2 = grid[y + 1][x]
            else:
                cell1 = grid[y][x - 1]
                cell2 = grid[y][x + 1]
        else:
            y = random.randint(1, maze_size - 2)
            if y % 2 == 0:
                cell1 = grid[y - 1][x]
                cell2 = grid[y + 1][x]
            else:
                if x == 1:
                    x += 1
                    cell1 = grid[y][x - 1]
                    cell2 = grid[y][x + 1]
                else:
                    x -= 1
                    cell1 = grid[y][x - 1]
                    cell2 = grid[y][x + 1]
        if cell1 != cell2:
            grid[x][y] = 0
            for j in range(1, len(grid), 2):
                for i in range(1, len(grid[j]), 2):
                    if grid[j][i] == cell2:
                        grid[j][i] = cell1
    for j in range(1, len(grid)):
        if complexe:
            x = random.randint(1, maze_size - 2)
            if x % 2 == 0:
                y = random.randint(1, maze_size - 2)
                grid[y][x] = 0
    grid[1][0] = grid[1][1]
    grid[maze_size - 2][maze_size - 1] = grid[1][1]
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[i][j] > 0:
                grid[i][j] = 0
    return grid


def distance(grid, maze_size):
    grid[maze_size - 2][maze_size - 1] = 1
    k = 1
    while grid[1][1] == 0:
        for j in range(len(grid) - 2, 0, -1):
            for i in range(len(grid[j]) - 2, 0, -1):
                if grid[i][j] == 0:
                    if grid[i + 1][j] > 0 or grid[i - 1][j] > 0 or grid[i][j + 1] > 0 or grid[i][j - 1] > 0:
                        k += 1
                        grid[i][j] = k
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = k + 1
    return grid


def solveMaze(grid, maze_size):
    x = 1
    y = 1
    graphic.changecell(0, 1)
    graphic.changecell(y, x)
    while x != maze_size - 1 and y != maze_size - 1:
        if grid[x][y] >= grid[x + 1][y] > 0:
            grid[x][y] = 0
            x += 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x - 1][y] > 0:
            grid[x][y] = 0
            x -= 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x][y - 1] > 0:
            grid[x][y] = 0
            y -= 1
            graphic.changecell(y, x)
        elif grid[x][y] >= grid[x][y + 1] > 0:
            grid[x][y] = 0
            y += 1
            graphic.changecell(y, x)
    grid[1][0] = 0
    grid[maze_size - 2][maze_size - 1] = 0


if __name__ == '__main__':
    g = graphic()
    g.end()
