# MANVI SINGHAL

# Test Cases
'''
1.  number of passengers - 30
    size = 4
    2D array - [[3,2], [4,3], [2,3], [3,4]]

2.  number of passengers - 50
    size = 4
    2D array - [[3,4], [4,5], [2,3], [3,4]]

3.  number of passengers - 25
    size = 3
    2D array - [[5, 3], [4, 2], [2, 7]]

4.  number of passengers - 3
    size = 2
    2D array - [[5, 5], [3, 4]]

5.  number of passengers - 15
    size = 2
    2D array - [[3, 3], [2, 2]]
'''


# ALGORITHM

fill = 0
num = int(input("Enter no of passengers: "))
row = 0
temp = -1
size = int(input("Enter size: "))
grid = []
queue = 0
total = 0

# input
for x in range(size):
    grid.append([int(y) for y in input().split()])

for i in range(len(grid)):
    for j in range(len(grid[i]) - 1):
        total += grid[i][j] * grid[i][j + 1]

if total <= num:
    queue = num - total
else:
    queue = 0

def build(grid):
    seats = []
    for i in grid:
        rows = i[1]
        cols = i[0]
        mat = []
        for i in range(rows):
            mat.append([-1] * cols)
        seats.append(mat)
    return seats


# Print Seat.
def printSeats(seats):
    blksize = len(str(num))
    rows = [x[1] for x in grid]
    cols = [x[0] for x in grid]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' ' * blksize
                    rowl += ' ' * blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' ' * blksize
                        rowl += '-' * blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k) + (' ' * (blksize - len(str(k))))
                        rowl += '-' * blksize
                        row += '|'
                        rowl += '+'

            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))


# Aisle Seat

def aisle():
    global fill
    row = 0
    temp = -1
    while fill < num and fill != temp:
        temp = fill
        for i in range(length):
            if grid[i][1] > row:
                if i == 0 and grid[i][0] > 1:
                    fill += 1
                    aisleCol = grid[i][0] - 1
                    seats[i][row][aisleCol] = fill
                    if fill >= num:
                        break
                elif i == length - 1 and grid[i][0] > 1:
                    fill += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = fill
                    if fill >= num:
                        break
                else:
                    fill += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = fill
                    if fill >= num:
                        break
                    if grid[i][0] > 1:
                        fill += 1
                        aisleCol = grid[i][0] - 1
                        seats[i][row][aisleCol] = fill
                        if fill >= num:
                            break
        row += 1


# Window Seat
def window():
    global fill
    global num
    row = 0
    temp = 0
    while fill < num and fill != temp:
        temp = fill
        if grid[0][1] > row:
            fill += 1
            window = 0
            seats[0][row][window] = fill
            if fill >= num:
                break
        if grid[length - 1][1] > row:
            fill += 1
            window = grid[length - 1][0] - 1
            seats[length - 1][row][window] = fill
            if fill >= num:
                break
        row += 1


# Middle Seat
def middle():
    global fill
    row = 0
    temp = 0
    breakp = 0
    while fill < num and fill != temp:
        temp = fill
        for i in range(length):
            if grid[i][1] > row:
                if grid[i][0] > 2:
                    for col in range(1, grid[i][0] - 1):
                        fill += 1
                        seats[i][row][col] = fill
                        if fill >= num:
                            breakp = 1
                            break
            if breakp == 1:
                break
        row += 1


seats = build(grid)

length = len(grid)

# Aisle
aisle()

# Window
window()

# Center
middle()

# print seats
printSeats(seats)

# print reamaining passengers in queue
print("num of passengers in queue", queue)