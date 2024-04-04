#Grid attempt 4
# Dictionary 1
import random

example_one = {
    "Linking Word": "Things that can go with the word surf",
    "Words": ["Board", "Skate", "Body", "Ski"]
}

example_two = {
    "Linking Word": "Hands",
    "Words": ["Nail", "Finger", "Palm", "Thumb"]
}

example_three = {
    "Linking Word": "Shit",
    "Words": ["Laim", "Yanited", "Manshity", "Arsenal"]
}

example_four = {
    "Linking Word": "Minecraft",
    "Words": ["Block", "Wood", "Pumpkin", "TNT"]
    
}

example_five = {
    "Linking Word": "Colours",
    "Words": ["Red", "Orange", "Yellow", "Green"]
    
}

example_six = {
    "Linking Word": "Words for adventure",
    "Words": ["Mission", "Geste", "Emprise", "Expedition"]
}

example_seven = {
    "Linking Word": "Clothing items",
    "Words": ["Bolero", "Ascot", "Culottes", "Corset"]
}

example_eight = {
    "Linking Word": "Homeware brands",
    "Words": ["Roomie", "PonyRider", "Armadillo", "Double"]
}

multiple_dictionaries = [example_one, example_two, example_three, example_four, example_five, example_six, example_seven, example_eight]

# this function randomises the choice of dictionaries for each game
def chosen_categories():
    game_categories = []

    for entry in range(0,4):
        random_index = random.randint(0,len(multiple_dictionaries)-1)
        game_categories.append(multiple_dictionaries[random_index])
        multiple_dictionaries.remove(multiple_dictionaries[random_index])
    
    return game_categories
    # for example in game_categories:
    #     print(example["Words"])

# flatten all the words and put them into one big list
# shuffle the words
def flat_list(game_categories):
    flat_list = []
    for example in game_categories:
        for word in example["Words"]:
            flat_list.append(word)
            
    random.shuffle(flat_list)
    return(flat_list)

def take_flat_list_and_put_into_2d_array(flat_list):
    game_grid= []
    game_grid.append(flat_list[0:4])
    game_grid.append(flat_list[4:8])
    game_grid.append(flat_list[8:12])
    game_grid.append(flat_list[12:16])
    return game_grid

def print_grid(game_grid):
    for row in game_grid:
        print(row)

def get_guess():
    print("Type in four words with a space seperating them. Eg. Red Green Blue Yellow: ")
    guess = input("Type your words: ")
    return guess

def check_guess(guess, game_categories):
    guess = guess.split(" ") # converts to a list object we can use to compare
    correct = False
    category_guessed = None
    print(guess)
    if set(guess) == set(game_categories[0]["Words"]):
        correct = True 
        print(game_categories[0]["Linking Word"])
        category_guessed = game_categories[0]["Linking Word"]
    if set(guess) == set(game_categories[1]["Words"]):
        correct = True 
        print(game_categories[1]["Linking Word"])
        category_guessed = game_categories[1]["Linking Word"]
    if set(guess) == set(game_categories[2]["Words"]):
        correct = True
        print(game_categories[2]["Linking Word"])
        category_guessed = game_categories[2]["Linking Word"]
    if set(guess) == set(game_categories[3]["Words"]):
        correct = True
        print(game_categories[3]["Linking Word"])
        category_guessed = game_categories[3]["Linking Word"]

    return correct, category_guessed
        

def float_correct_words_to_top(, guess):
    game_grid.remove(guess[0])
    game_grid.remove(guess[1])
    game_grid.remove(guess[2])
    game_grid.remove(guess[3])




# main - setup for the game 
game_categories = chosen_categories()
flat_list = flat_list(game_categories)
game_grid = take_flat_list_and_put_into_2d_array(flat_list)


lives = 4
categories_guessed = 0

while lives >0 and categories_guessed <4:
    print_grid(game_grid)
    guess = get_guess()
    correct, category_guessed = check_guess(guess, game_categories)
    if correct == True:
        categories_guessed += 1
        float_correct_words_to_top(flat_list, guess)
        print("You guessed the category: ",category_guessed)
        print("You have successfully guessed ", categories_guessed, " categories")
    else:
        lives = lives - 1
        print("Wrong guess loser")

if lives == 0:
    print("You Lose, you suck")
else:
    print("You win")
