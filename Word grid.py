

words = [
 "Hello",
 "I",
 "Like",
 "Word 4",
 "Word 5",
 "Word 6",
 "Word 7",
 "Word 8",
 "Word 9",
 "Word 10",
 "Word 11",
 "Word 12",
 "Word 13",
 "Word 14",
 "Word 15",
 "Word 16",
]

# arrays have index values that start at 0

# 2 DIMENSIONAL ARRAYS


grid = [] # EMPTY GRID
word_index = 0


for row in range(0, 4):   # do the following 4 times
    row = []
    for col in range(0,4):
        row.append(words[word_index])
        word_index += 1
    grid.append(row)



print(grid) # reference the entire row without column

# RANDOMISATION

from random import randint

print(randint(0, 14)) #

print(words[randint(0, len(words))])