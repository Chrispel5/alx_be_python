days = input("Enter the day of the week (Monday - Sunday) ").lower()

match days:
    case "monday":
        print(f"Ugh {days}, again?")

    case "tuesday":
        print(f"its {days}, mate let move")

    case "wednesday":
        print(f"Hump {days}!")

    case "thursday":
        print(f"Almost there...")
    case "friday":
        print(f"TGIF!")
    case "saturday" | "sunday":
        print(f"Ladies and Gentle men, it's the Weekend")
    case _:
        print(f"invalid day entered.")