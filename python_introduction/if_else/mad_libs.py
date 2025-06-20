first_adjective = input("input an adjectives for day: ")
second_adjective = input("input an adjective for the monkey: ")
third_adjective = input("input an adjective for the lion: ")
forth_adjective = input("input an adjective for the experience: ")

story = (f"On a beautiful {first_adjective} day, I went to the zoo. " 
         f"I saw a funny {second_adjective} monkey swinging from the trees. " 
         f"Then, I spotted a majestic {third_adjective} lion lounging in the sun. " 
         f"What a wild and {forth_adjective} experience!"
         )

if forth_adjective.lower() == "boring":
    story+= "I expected more excitement from a zoo visit"
elif forth_adjective.lower() in ["amazing", "hilarious", "unforgettable", "magical"]:
    story+= " That day will stay in my memory forever. "
else: 
    story+= " I will never forget the experience"
print("\n Your Mad Libs Story:")
print(story)
