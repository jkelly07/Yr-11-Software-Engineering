# 2 DIMENSIONAL ARRAYS

grid =[] # EMPTY GRID
placeholder = 1

for i in range(0,4):
    row = []
    for col in range(0,4):
        row.append(placeholder)
        placeholder += 1
    grid.append(row)


print(grid[0]) # reference the entire row without column
print(grid[0][1]) # refers to a specific cell

for row in grid:
    print(row)
