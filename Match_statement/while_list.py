shopping_list = ["plate", "spoon", "towel"]
item_found = False

while not item_found:
    item = input("Search for an item im your list (or 'q' to quit): ")
    if item == 'q':
        break

    if item in shopping_list:
        item_found = True
        print(f"{item} is in your shopping list")

    else:
        print (f"{item} not in your shopping list")
 
        