#task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: action =="cross a river"
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
    
    #task2
    
if place == "cave":
    torch = input("would you like to light a torch or proceed in the dark?")
    if torch == "light a torch":
        print("torch is lit")
    if torch == "proceed in the dark": print("be careful you cant see clearly")
else: pass
            