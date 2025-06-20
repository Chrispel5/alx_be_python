value = input("Enter a value (numbers or letters)")

match value:
    case int():
        print(f"Your Literally Entered a Number: {value}")

    case str():
        print(f"You literally entered a letter/text: {value}")
    
