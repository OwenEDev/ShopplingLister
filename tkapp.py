import tkinter as tk


#dictionary containing recipes
recipes = {
    "Butternut Squash Risotto": "onion \ngarlic \nrisotto rice \nsoup stock \nbutternut squash \nparmasan\n",
    "Pizza": "pepper \nonion \npeeled plum tomatoes \nmozarella \ncheddar \nmushrooms \npizza base\n",
    "Thai Curry": "shallots \ncorriander \ncoconut milk \ncourgette \ncucumber \npepper \ntomato \ncarrots\n",
    "Butternut Squash Tacos": "butternut squash \ntortillas \ncashew nuts \nkale \ncorriander \nparsley \nspring onions \ntamatillo salsa \npink pickled onion \npumpkin seeds \nhot sauce\n",
    "Pepper and Sweetcorn Soup": "peeled plum tomatoes \nsweetcorn \npeppers \nsoup stock \nred onion\n",
    "Pepper and Courgette Pasta": "onion \ngarlic \npeppers \ntomato puree \npeeled plum tomatoes \ncourgettes\n",

}

#converting recipe dictionary to a list
values = recipes.keys()
values_list = list(values)

#building the app
window=tk.Tk()
window.title("Shopping Lister")

frame1 = tk.Frame(master=window, width=500, height=700,)
frame1.pack(side=tk.LEFT, fill=tk.Y)

frame2 = tk.Frame(master=window, width=300, height=700,)
frame2.pack(side=tk.LEFT, fill=tk.Y)

class Button():
    def __init__(self, text):
        self.text = text
        def writeRecipe():
            value = text
            shoppingList.insert(tk.END, f"{recipes[value]}\n")
        button = tk.Button(text=text, master=frame1, command=writeRecipe)
        button.pack(fill=tk.X)
        
#creating the text box
shoppingList = tk.Text(master=frame2)
shoppingList.pack(fill=tk.Y)

buttons = []

for c in range(int(len(recipes.keys()))):
    

    buttons.append(Button(values_list[c]))


window.mainloop()