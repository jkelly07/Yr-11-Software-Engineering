#flat list

from Chosen_categories1 import *

import random
game_categories = chosen_categories()

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