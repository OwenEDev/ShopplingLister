import sqlite3

#establish connection and define cursor
conn = sqlite3.connect("recipes.db")
c = conn.cursor()

#read table function
def read_table():
    c.execute("SELECT * FROM recipes")
    data = c.fetchall()
    [print(rows) for rows in data]
    #print to data to widget

#read row function
def read_row(dish):
    c.execute("SELECT * FROM recipes WHERE dish = ?", (dish,))
    data = c.fetchall()
    [print(rows) for rows in data]
    #print data to widget

#update row function
def update_row(newDish, ingredients, dish):
    c.execute("UPDATE recipes SET dish = (?), ingredients = (?) WHERE dish=(?)", (newDish, ingredients, dish))
    conn.commit()

#delete row function
def delete_row(dish):
    c.execute("DELETE FROM recipes WHERE dish = (?)", (dish,))
    conn.commit()

c.close()
conn.close()