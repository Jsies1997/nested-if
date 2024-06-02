#task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#task 2
if attendees < 100:
    print("projector")
elif attendees >= 100:
    print("audio system")
    
meal = input("would you like vegetarian food Y/N?")

if meal == "Y":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meal Caterers")