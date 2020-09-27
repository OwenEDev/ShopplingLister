
recipes = {
    "pizza": "tomato, cheese, pizza base",
    "spaghetti": "Spaghetti, garlic, basil",
    "nachos": "Cheese gunk, Nachos",
    "tacos": "Tacos, Lettuce, Potato",
    "butternut squash risotto": "butternut Squash, Risotto Rice",
    "skip": "Day Skipped",
}

userInput1 = input("Monday: ").lower()
if userInput1 in recipes:
    userInput1 = userInput1
elif userInput1 == 'kill'.lower():
    quit()
else: userInput1 = 'skip'
userInput2 = input("Tuesday: ").lower()
if userInput2 in recipes:
    userInput2 = userInput2
else: userInput2 = 'skip'
userInput3 = input("Wednesday: ").lower()
if userInput3 in recipes:
    userInput3 = userInput3
else: userInput3 = 'skip'
userInput4 = input("Thursday: ").lower()
if userInput4 in recipes:
    userInput4 = userInput4
else: userInput4 = 'skip'
userInput5 = input("Friday: ").lower()
if userInput5 in recipes:
    userInput5 = userInput5
else: userInput5 = 'skip'
userInput6 = input("Saturday: ").lower()
if userInput6 in recipes:
    userInput6 = userInput6
else: userInput6 = 'skip'
userInput7 = input("Sunday: ").lower()
if userInput7 in recipes:
    userInput7 = userInput7
else: userInput7 = 'skip'

print(recipes[userInput1],"\n",recipes[userInput2],"\n",recipes[userInput3],"\n",recipes[userInput4],"\n",recipes[userInput5],"\n",recipes[userInput6],"\n",recipes[userInput7])
