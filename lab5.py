#lab5

#3.1

alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points.")
    
#3.2

alien_color = "red"

if alien_color == "green":
    print("You just earned 5 points for shooting the alien.")
else: 
    print("You just earned 10 points.")
    
#3.3

favorite_fruits = ["oranges","pineapples","blueberries"]
if "oranges" in favorite_fruits:
    print("You must benefit from the Vitamin C in oranges.")
if "pineapples" in favorite_fruits: 
    print("Pineapples are a tropical delight.")
if "blueberries" in favorite_fruits:
    print("Blueberries are also quite delicious.")
else:
    print("I find your lack of fruit-sense disturbing.")
    
#3.4

age = 72

if age < 10:
    print("kid")
elif age >= 10 and age < 20:
    print("teenager")
elif age >= 20:
    print("adult")
if age >= 65:
    print("elder")

