from connections import dictionaries

def check_win(guessed_categories):
    # check if user has gussed all cateogies;
    # if yes then return true
    # otherwise return false
    return True


def update_categories(guess, populated_grid, chosen_categories, lives, guessed_categories):
    # check the user guess
    # compare against the original cateories
    # if its correct, update the guessed categories
    # if its not, changes lives by -1
    # update the grid if the user guessses right
    return (populated_grid, lives, guessed_categories)


def get_guess():
    guess = input("Enter your guess")
    return guess


def display_game_state(populated_grid, guessed_categories, lives):
    # draws the latest screen to the user
    # first screen is the full grid
    # as guesses have been validated, the grid will look different
    # also underneath, show how many lives are left
    pass

def play_game(chosen_categories, populated_grid):
    lives = 4
    check_win = False
    guessed_categories = []
    while lives >0 and check_win == False:
        display_game_state(populated_grid,guessed_categories, lives)
        guess = get_guess()
        update_categories(guess, populated_grid, chosen_cateogies, lives, guessed_categories)
        check_win = (check_win())



def generate_grid(chosen_categories):
    empty_grid = [["1","2","3","4",],
                ["5","6","7","8",],
                ["9","10","11","12",],
                ["13","14","15","16",]]
    
    # for dictionary in chosen_cateogies:
    #     for word in dictionary["words"]:
    #         print(word)

    # print(empty_grid)
    # print(empty_grid[0])
    # print(empty_grid[3][3])
    # empty_grid[3][3] = "test" # you can update the values inside of the grid!
    
    # loop through the dictionaries and put the words into the grid
    x = 0
    y = 0
    for category in chosen_categories:
        y = 0
        for word in category["words"]:
            empty_grid[x][y] = word
            y = y + 1
        x = x + 1
    return empty_grid

def choose_categories(dictionaries):
    # choose 4 random categories from the dictionaries
    # imported from the dictionaries file
    
    
    # print(dictionary[0]) # just print first dictionary
    # print(dictionary[0]["words"]) # just print first dictionary
    # for dictionary in dictionaries:
    #     for word in dictionary["words"]:
    #         print(word)
    
    return dictionaries

def connections():
    play_game = True
    while play_game == True:
        #get categories
        chosen_categories = choose_categories(dictionaries())
        populated_grid = generate_grid(chosen_categories)
        # set lives to 4
       
        guessed_cagegories = []

        play_game(chosen_categories, populated_grid)

connections()
