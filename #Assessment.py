#Assessment

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



def chosen_categories():
    game_categories = []

    for entry in range(0,4):
        random_index = random.randint(0,len(multiple_dictionaries)-1)
        game_categories.append(multiple_dictionaries[random_index])
        multiple_dictionaries.remove(multiple_dictionaries[random_index])
    return game_categories
    # for example in game_categories:
    #     print(example["Words"])
game_categories = chosen_categories()
chosen_categories()
# runs the function


# flatten all the words and put them into one big list
# shuffle the words
def flat_list1():
    flat_list = []
    for example in game_categories:
        for word in example["Words"]:
            flat_list.append(word)
            
    random.shuffle(flat_list)
    print(flat_list)
flat_list1()


def populate_grid():
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("|                    |                    |                    |                    |")
    print("+--------------------+--------------------+--------------------+--------------------+")

print(populate_grid)



