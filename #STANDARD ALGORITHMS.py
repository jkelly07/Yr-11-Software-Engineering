#STANDARD ALGORITHMS
# accepted ways of solving
# particular problems:

# linear search - textbook way
def LinearSearch(arr):
    found = False
    i = 0
    search_term = int(input())
    while found == False and i < len(arr):
        if arr[i] == search_term:
            found == True
        i += 1
    return found


    arr = [7, 4, 8, 18, 19, 5, 348, 6, 1400, 666, 9, 42]

   print(LinearSearch(arr))


# pythonic way....
def shorter_linear():
    found = False
    search_term = int(input())
    for i in arr:
        if i == search_term:
            found = True
            break
    return found

shorter_linear(arr)



# binary serach
# find min/max values
# permutation sort
# merge sort
# selection