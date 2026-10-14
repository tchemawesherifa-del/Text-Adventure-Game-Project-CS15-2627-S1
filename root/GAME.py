found_number = False
security_code_number = 7
found_small_key = False
found_note = False
found_hallway_clue = False
found_science_clue = False
found_cabinet_key = False
found_cabinet = False

print("Welcome to School Mystery Escape !")

print("On a cold winter day, you accidentally fell asleep in the locker rooms and were left behind.")
print("You then come to find out that the doors to exit the school are locked.")
print("You must find the special RED key to escape.")

print("Want to know How to Play?:")
choice = input("1. Yes    2. Yes: ")

while choice != "1" and choice != "2":
    print("Please choose 1 or 2.")
    choice = input("1. Yes    2. Yes: ")

print("How to Play <3 :")
print("Choose what you want to do using the numbers shown.")
print("Explore the school and look for clues and keys.")
print("You can return to rooms you have already visited.")
print("Find the RED key to escape!")

input("Press Enter to start...")

print("Narrator: You slowly wake up in a dark room.")
print("Narrator: You quickly check your phone, which is at a whopping 2%.")
print("Narrator: You use that to turn on your flash and realise where you are.")
print("Narrator: The locker rooms....")
print("You try the main school exit, but it's locked.")
print("You need to find the special RED key to escape.")

room = "locker room"

while True:

    if room == "locker room":
        print("\nYou are in the locker room.")
        print("1. Search the locker room")
        print("2. Go to the gym")

        choice = input("Choose 1 or 2: ")

        while choice != "1" and choice != "2":
            print("Please choose 1 or 2.")
            choice = input("Choose 1 or 2: ")

        if choice == "1":
            print("Narrator: You look around the locker room.")

            if found_number == False:
                print("You look under a bench and find the number", security_code_number)
                found_number = True
            else:
                print("You already found the number.")

        elif choice == "2":
            print("Narrator: You open the door and enter the gym.")
            room = "gym"

    elif room == "gym":
        print("\nYou are in the gym.")
        print("The gym is dark, and you can barely see anything.")
        print("1. Search near the basketballs")
        print("2. Check the equipment room")
        print("3. Enter the main hallway")
        print("4. Return to the locker room")

        gym_choice = input("Choose 1, 2, 3 or 4: ")

        while gym_choice != "1" and gym_choice != "2" and gym_choice != "3" and gym_choice != "4":
            print("Please choose 1, 2, 3 or 4.")
            gym_choice = input("Choose 1, 2, 3 or 4: ")

        if gym_choice == "1":
            print("Narrator: You search near the basketballs.")

            if found_small_key == False:
                print("You find a small key hidden underneath one of them.")
                found_small_key = True
            else:
                print("You already found the small key.")

        elif gym_choice == "2":
            print("Narrator: You check the equipment room.")

            if found_note == False:
                print("You find a strange note saying 'Look where experiments happen.'")
                found_note = True
            else:
                print("You already found the note.")

        elif gym_choice == "3":
            print("Narrator: You walk out of the gym and enter the main hallway.")
            room = "hallway"

        elif gym_choice == "4":
            print("You return to the locker room.")
            room = "locker room"

    elif room == "hallway":
        print("\nYou are in the main hallway.")
        print("The hallway is dark and silent.")
        print("You notice a noticeboard covered with school announcements.")

        if found_hallway_clue == False:
            print("One message catches your eye:")
            print("'Where experiments happen, your next clue waits.'")
            found_hallway_clue = True

        print("What do you want to do?")
        print("1. Read the noticeboard")
        print("2. Enter the Science Room")
        print("3. Return to the gym")
        print("4. Return to the locker room")

        hallway_choice = input("Choose 1, 2, 3 or 4: ")

        while hallway_choice != "1" and hallway_choice != "2" and hallway_choice != "3" and hallway_choice != "4":
            print("Please choose 1, 2, 3 or 4.")
            hallway_choice = input("Choose 1, 2, 3 or 4: ")

        if hallway_choice == "1":
            print("You read the noticeboard carefully.")
            print("'Where experiments happen, your next clue waits.'")

        elif hallway_choice == "2":
            print("Narrator: You enter the Science Room.")
            room = "science"

        elif hallway_choice == "3":
            print("You return to the gym.")
            room = "gym"

        elif hallway_choice == "4":
            print("You return to the locker room.")
            room = "locker room"

    elif room == "science":
        print("\nYou are in the Science Room.")
        print("The room is filled with beakers and science equipment.")
        print("You notice a locked cabinet.")

        if found_science_clue == False:
            print("A note beside the cabinet says:")
            print("'The first digit is the number of sides on a triangle.'")
            found_science_clue = True

        print("What do you want to do?")
        print("1. Check the cabinet")
        print("2. Return to the hallway")
        print("3. Return to the gym")

        science_choice = input("Choose 1, 2 or 3: ")

        while science_choice != "1" and science_choice != "2" and science_choice != "3":
            print("Please choose 1, 2 or 3.")
            science_choice = input("Choose 1, 2 or 3: ")

        if science_choice == "1":
            print("Narrator: You crouch down to examine the cabinet.")
            print("Narrator: You notice scratches around its lock.")
            print("Narrator: Something shiny catches your eye on the floor.")

            if found_cabinet == True:
                print("The cabinet is already unlocked.")
                print("You have already searched inside.")

            else:
                if found_cabinet_key == False:
                    print("You find a small key lying on the floor beside the cabinet.")
                    found_cabinet_key = True
                else:
                    print("You already picked up the key beside the cabinet.")

                print("Narrator: You pick up the key and put it into the cabinet lock.")
                print("Click! The cabinet unlocks.")
                print("Narrator: You open the cabinet and look inside.")
                print("Inside, you find a mysterious note.")
                print("'You are getting closer to the RED key!'")

                found_cabinet = True

        elif science_choice == "2":
            print("Narrator: You leave the Science Room and return to the hallway.")
            room = "hallway"

        elif science_choice == "3":
            print("You leave the Science Room and return to the gym.")
            room = "gym"