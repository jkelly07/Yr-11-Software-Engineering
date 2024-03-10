# Question 1
games = ["Fortnite", "Minecraft", "Among Us"]

# Your task: Add "Rocket League" to the beginning of the list

games.insert(0, "Rocket League")
print(games)

# Question 2
road_trip = ("New York", "Los Angeles", 5, ["John", "Peter", "Sam"])
print(road_trip[1])

# Question 3

my_cards = {"Card1", "Card2", "Card3", "Card4"}
your_cards = {"Card3", "Card4", "Card5", "Card6"}
print(my_cards.difference(your_cards))

# Question 4
scores = [100, 200, 300, 400]
average = sum(scores)/len(scores)

total = 0
for score in scores:
    total += score
print(total/len(scores))
