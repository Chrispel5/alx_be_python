positive_integer = int(input("Enter the size of the pattern: "))
row = 0

while row < positive_integer:
    for col in range(positive_integer):
        print("*", end="")
    print ()

    row += 1