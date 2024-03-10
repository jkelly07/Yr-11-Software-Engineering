# CREATE GRID
def create_word_grid():
    # create a 4x4 grid with a placeholder word in each cell.

    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('hello')
        word_grid.append(row)
    
    return word_grid

grid = create_word_grid()
print(grid[0])


# stack overflow
