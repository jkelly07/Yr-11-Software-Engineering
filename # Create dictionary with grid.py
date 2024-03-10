# Create dictionary with grid
# SD arrays

grid = [
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]

connections = [
    {"Connecting Word": "Major Cities", "Words": ["Washington", "Mumbai", "Colombia", "Tokyo"]},
    {"Connecting Word": "Places named after leaders", "Words": ["Saudi Arabia", "Alexandria", "Udaipur", "Phillipines"]},
    {"Connecting Word": "Shit soccer teams", "Words": ["Everton", "Man U", "Man Citeh", "Real Madrid"]},
    {"Connecting Word": "Colours", "Words": ["Red", "Green", "Yellow", "Blue"]},
]

# outer loop designed to loop through rows

row = 0

for connection in connections: # for each of the connections, access the dictionary
    col = 0
    for word in connection["Words"]: # within the dictionary, get each word
        # put the word inside the correct grid reference
        grid[row][col] = word
        col = col + 1 # moves to the next column
    row = row + 1 # moves to the next row

print(grid)

import random