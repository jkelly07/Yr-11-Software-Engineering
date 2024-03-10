# Grid attempt 2


width = int(input(4))
height = int(input(4))
grid = []
row = []
space = " . "
for i in range(width):
    grid.append(space)
for i in range(height):
    grid.append(row)
while True:
    for i in range(len(grid)):
        print(grid[i])

