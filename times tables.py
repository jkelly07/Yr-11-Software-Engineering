# create a program that accepts X an integer
# output the times table for X, Y number of times


def times_table(x, y):
    for i in range(1, y):
        print(x * i)

times_table(100, 100)