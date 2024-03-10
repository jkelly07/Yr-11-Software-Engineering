# Dictionary L

# Dictionary 1
import random

example_one = {
    "Linking Word": "Colours",
    "Words": ["Salmon", "Lime Green", "Magenta", "Aqua"]
}

example_two = {
    "Linking Word": "Hands",
    "Words": ["Nail", "Finger", "Pink", "Thumb"]
}

example_three = {
    "Linking Word": "Shit",
    "Words": ["Laim", "Yanited", "Manshity", "Arsenal"]
}

example_four = {
    "Linking Word": "Minecraft",
    "Words": ["Block", "Wood", "Pumkin", "TNT"]
    
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
    "Words": ["Roomie", "Pony Rider", "Armadillo", "Double"]
}

multiple_dictionaries = [example_one, example_two, example_three, example_four, example_five, example_six, example_seven, example_eight]

game_categories = []

for entry in range(0,4):
# im going to create a list, for each entry in that list, do the following (range decides length of list)
    random_index = random.randint(0,len(multiple_dictionaries)-1)

    game_categories.append(multiple_dictionaries[random_index])
# adding(append) something random from multiple dictionaries to game categories
# or cos laim cahnged what he said twice "getting a random index(position in a list from 0) and correlating it with a example_ from multiple dictionaries, and adding it to game categories"
    
    multiple_dictionaries.remove(multiple_dictionaries[random_index])
# removes the chose random index (that correlates to a category) from multiple dictionaries when choosing next index

for example in game_categories:
    print(example["Words"])

# for every entry in game_categories, it will look at the examples from game categories and get the words varaiable and print it (the words)

