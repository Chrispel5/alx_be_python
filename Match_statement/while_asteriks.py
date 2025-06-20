rows = 5
current_row = 1
while current_row <= rows:
    
    space = 1
    while space <= rows - current_row:
        print(" ", end="")
        space+=1

    star = 1
    while star <= 2 * current_row - 1:
        star += 1
        print("*", end="")

    print()
    current_row += 1

