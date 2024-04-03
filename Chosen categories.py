# Dictionary 1
import random

from Dictionary import *


def chosen_categories():
    game_categories = []

    for entry in range(0,4):
        random_index = random.randint(0,len(multiple_dictionaries)-1)
        game_categories.append(multiple_dictionaries[random_index])
        multiple_dictionaries.remove(multiple_dictionaries[random_index])
    
    for example in game_categories:
        print(example["Words"])


chosen_categories()


