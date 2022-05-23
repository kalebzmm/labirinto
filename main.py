import queue
import os
import time

clear = lambda: os.system('cls')

def pathPrettyPrint(path):
    return path.replace('U', '↑').replace('R', '→').replace('D', '↓').replace('L', '←')

def readMaze():
	with open('./maze.txt') as file:
		lines = file.readlines()
		return [list(line.rstrip()) for line in lines]

def isStart(e):
    return e == 'S'

def isEnd(e):
    return e == 'E'

def isCheese(e):
    return e == 'C'

def isWall(e):
    return e == '#'

def findStart(maze):
    for x, pos in enumerate(maze):
        if isStart(pos[0]):
            return x

def valid(maze, start, moves):
    x = 0
    y = start
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

        if not (0 <= x < len(maze[0]) and 0 <= y < len(maze)):
            return False
        elif isWall(maze[y][x]):
            return False
        # elif isCheese(maze[y][x]):
        #     print('🧀')

    return True

def findEnd(maze, start, moves):
    x = 0
    y = start
    for move in moves:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

    if isEnd(maze[y][x]):
        clear()
        print('Encontrado em', "%s segundos" % (time.time() - start_time), ':', pathPrettyPrint(add))
        printMaze(maze, start, add)
        return True

    return False

def printMaze(maze, start, path=""):
    x = 0
    y = start
    pos = set()
    for move in path:
        if move == "L":
            x -= 1

        elif move == "R":
            x += 1

        elif move == "U":
            y -= 1

        elif move == "D":
            y += 1

        pos.add((y, x))

    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if (y, x) in pos:
                print("\033[92m" + "@ " + "\033[0m", end="")
            else:
                print("\033[91m" + col + " \033[0m", end="")
        print()

def validMoves(maze, lastMove):
    moves = ["L", "R", "U", "D"]
    if(not lastMove):
        return moves
    moves.remove(lastMove)
    moves.insert(0, lastMove)
    if(lastMove == 'R'): moves.remove('L')
    if(lastMove == 'L'): moves.remove('R')
    if(lastMove == 'U'): moves.remove('D')
    if(lastMove == 'D'): moves.remove('U')
    return moves

nums = queue.Queue()
add = ""
nums.put(add)
maze = readMaze()
start = findStart(maze)
lastPos = (start, 0) # y, x
lastMove = ''
start_time = time.time()

while not findEnd(maze, start, add):
    add = nums.get()
    clear()
    moves = validMoves(maze, lastMove)
    print('Tentativa: ', moves, pathPrettyPrint(add))
    printMaze(maze, start, add)
    for j in moves:
        put = add + j
        if valid(maze, start, put):
            nums.put(put)
            lastMove = j
            continue