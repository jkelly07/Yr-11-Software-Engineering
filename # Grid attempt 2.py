# Grid attempt 2


# width = int(input(4))
# height = int(input(4))
# grid = []
# row = []
# space = " . "
# for i in range(width):
#     grid.append(space)
# for i in range(height):
#     grid.append(row)
# while True:
#     for i in range(len(grid)):
#         print(grid[i])


def generate_grid(chosen_categories):
    empty_grid = [["1","2","3","4",],
                ["5","6","7","8",],
                ["9","10","11","12",],
                ["13","14","15","16",]]
    for example in chosen_categories:
        for word in example["Words"]:
            print(word)

    x = 0
    y = 0
    for example in chosen_categories:
        y = 0
        for word in example["Words"]:
            empty_grid[x][y] = word
            y = y + 1
        x = x + 1
    return empty_grid
    # for dictionary in chosen_cateogies:
    #     for word in dictionary["words"]:
    #         print(word)

    # print(empty_grid)
    # print(empty_grid[0])
    # print(empty_grid[3][3])
    # empty_grid[3][3] = "test" # you can update the values inside of the grid!
    
    # loop through the dictionaries and put the words into the grid


