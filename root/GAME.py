found_number = False
security_code_number = 7
found_small_key = False
found_note = False
found_hallway_clue = False
found_science_clue = False
found_cabinet_key = False
found_cabinet = False
found_math_clue = False
found_office_clue = False
found_library_clue = False
found_cafeteria_note = False
found_computer_clue = False
found_red_key = False

escaped_school = False

print("Welcome to School Mystery Escape ! <3")

print("On a cold winter day, you accidentally fell asleep in the locker rooms and were left behind.")
print("You then come to find out that the doors to exit the school are locked.")
print("You must find the special RED key to escape.")
print("lowkey how does a whole school forget one student tho...")

print("Want to know How to Play?:")
choice = input("1. Yes    2. Yes: ")

while choice != "1" and choice != "2":
    print("Please choose 1 or 2.")
    choice = input("1. Yes    2. Yes: ")

print("How to Play <3 :")
print("Choose what you want to do using the numbers shown.")
print("Explore the school and look for clues and keys.")
print("You can return to rooms you have already visited.")
print("Pay attention to notes because they might be important!")
print("Find the RED key to escape!")
print("good luck bestie... you're gonna need it.")

input("Press Enter to start...")

print("Narrator: You slowly wake up in a dark room.")
print("Narrator: You quickly check your phone, which is at a whopping 2%.")
print("Narrator: You use that to turn on your flash and realise where you are.")
print("Narrator: The locker rooms....")
print("You try the main school exit, but it's locked.")
print("You need to find the special RED key to escape.")
print("Narrator: Great. stranded at school. literally living the dream.")

room = "locker room"

while True:

    if room == "locker room":
        print("\nYou are in the locker room.")
        print("Your phone battery is still at 2%. tragic.")
        print("1. Search the locker room")
        print("2. Go to the gym")

        if found_red_key == True:
            print("3. Try to escape through the main exit")
            choice = input("Choose 1, 2 or 3: ")

            while choice != "1" and choice != "2" and choice != "3":
                print("Please choose 1, 2 or 3.")
                choice = input("Choose 1, 2 or 3: ")
        else:
            choice = input("Choose 1 or 2: ")

            while choice != "1" and choice != "2":
                print("Please choose 1 or 2.")
                choice = input("Choose 1 or 2: ")

        if choice == "1":
            print("Narrator: You look around the locker room.")
            print("You search the benches and lockers.")

            if found_number == False:
                print("You look under a bench and find the number", security_code_number)
                print("Narrator: Hmm... suspicious. why is there a random number under a bench?")
                found_number = True
            else:
                print("You already found the number.")

        elif choice == "2":
            print("Narrator: You open the door and enter the gym.")
            room = "gym"

        elif choice == "3":
            if found_red_key == True:
                print("Narrator: You take out the RED key and unlock the main exit.")
                print("The door opens slowly.")
                print("You step outside the school into the cold winter air.")
                print("You are finally outside and free!")
                print("FREEDOMMMMM <3")
                print("Congratulations! You escaped School Mystery!")
                escaped_school = True
                break
            else:
                print("You try the exit again, but it's still locked.")
                print("Narrator: okay door, we get it. you're locked.")
                print("You need to find the RED key first.")

    elif room == "gym":
        print("\nYou are in the gym.")
        print("The gym is dark, and you can barely see anything.")
        print("You hear something rolling across the floor.")
        print("...it's just a basketball. calm down.")
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
                print("Narrator: why was there a key under a basketball... anyways")
                found_small_key = True
            else:
                print("You already found the small key.")

        elif gym_choice == "2":
            print("Narrator: You check the equipment room.")

            if found_note == False:
                print("You find a strange note saying 'Look where experiments happen.'")
                print("Narrator: very mysterious. could've just sent an email.")
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
        print("The lights keep flickering. absolutely not.")
        print("You notice a noticeboard covered with school announcements.")

        if found_hallway_clue == False:
            print("One message catches your eye:")
            print("'Where experiments happen, your next clue waits.'")
            found_hallway_clue = True

        print("\nWhat do you want to do?")
        print("1. Read the noticeboard")
        print("2. Enter the Science Room")
        print("3. Return to the gym")
        print("4. Return to the locker room")
        print("5. Enter the Math Room")
        print("6. Enter the Office")
        print("7. Enter the Library")
        print("8. Enter the Cafeteria")
        print("9. Enter the Computer Lab")
        print("10. Enter the Security Room")

        hallway_choice = input("Choose 1-10: ")

        while hallway_choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Please choose a number from 1 to 10.")
            hallway_choice = input("Choose 1-10: ")

        if hallway_choice == "1":
            print("You read the noticeboard carefully.")
            print("'Where experiments happen, your next clue waits.'")
            print("Someone has drawn a tiny smiley face beside the message. iconic.")

        elif hallway_choice == "2":
            print("Narrator: You enter the Science Room.")
            room = "science"

        elif hallway_choice == "3":
            print("You return to the gym.")
            room = "gym"

        elif hallway_choice == "4":
            print("You return to the locker room.")
            room = "locker room"

        elif hallway_choice == "5":
            print("Narrator: You enter the Math Room.")
            room = "math"

        elif hallway_choice == "6":
            print("Narrator: You walk into the school office.")
            room = "office"

        elif hallway_choice == "7":
            print("Narrator: You enter the Library.")
            room = "library"

        elif hallway_choice == "8":
            print("Narrator: You enter the Cafeteria.")
            room = "cafeteria"

        elif hallway_choice == "9":
            print("Narrator: You enter the Computer Lab.")
            room = "computer lab"

        elif hallway_choice == "10":
            print("Narrator: You approach the Security Room.")
            room = "security room"

    elif room == "science":
        print("\nYou are in the Science Room.")
        print("The room is filled with beakers and science equipment.")
        print("Something smells weird. hopefully that's normal.")

        if found_science_clue == False:
            print("A note beside the cabinet says:")
            print("'The first digit is the number of sides on a triangle.'")
            print("Narrator: okay... geometry is involved. noted.")
            found_science_clue = True

        print("\nWhat do you want to do?")
        print("1. Check the cabinet")
        print("2. Return to the hallway")
        print("3. Return to the gym")

        science_choice = input("Choose 1, 2 or 3: ")

        while science_choice != "1" and science_choice != "2" and science_choice != "3":
            print("Please choose 1, 2 or 3.")
            science_choice = input("Choose 1, 2 or 3: ")

        if science_choice == "1":
            print("Narrator: You crouch down to examine the cabinet.")
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

                print("Narrator: You put the key into the cabinet lock.")
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

    elif room == "math":
        print("\nYou are in the Math Room.")
        print("The room is quiet, and papers are scattered across the desks.")
        print("Narrator: the only time math is useful outside math class...")

        if found_math_clue == False:
            print("You notice a math question written on the board.")
            print("'What is 2 + 2?'")
            print("Beside it, someone has written:")
            print("'The answer is the third digit of the security code.'")
            found_math_clue = True
        else:
            print("You already found the math clue.")

        print("\nWhat do you want to do?")
        print("1. Check the board again")
        print("2. Return to the hallway")

        math_choice = input("Choose 1 or 2: ")

        while math_choice != "1" and math_choice != "2":
            print("Please choose 1 or 2.")
            math_choice = input("Choose 1 or 2: ")

        if math_choice == "1":
            print("The answer is 4.")
            print("You remember that 4 is the third digit of the security code.")

        elif math_choice == "2":
            print("You leave the Math Room and return to the hallway.")
            room = "hallway"

    elif room == "office":
        print("\nYou are in the school office.")
        print("There are papers everywhere and a phone ringing with nobody answering it.")
        print("Narrator: HELLO?? is the school even functioning??")

        if found_office_clue == False:
            print("You search the front desk and find an old staff note.")
            print("'The security room is at the end of the east hallway.'")
            print("You also find a staff access card.")
            print("You put the card in your pocket. might come in handy.")
            found_office_clue = True
        else:
            print("You already searched the office.")
            print("The phone is STILL ringing. somebody pick it up omg.")

        print("\nWhat do you want to do?")
        print("1. Search the desk again")
        print("2. Return to the hallway")

        office_choice = input("Choose 1 or 2: ")

        while office_choice != "1" and office_choice != "2":
            print("Please choose 1 or 2.")
            office_choice = input("Choose 1 or 2: ")

        if office_choice == "1":
            print("You search through some papers.")
            print("It's mostly attendance sheets and a lunch menu.")
            print("nothing useful. office people need to clean this desk.")

        elif office_choice == "2":
            print("You leave the office and return to the hallway.")
            room = "hallway"

    elif room == "library":
        print("\nYou are in the Library.")
        print("The library is completely silent.")
        print("Even your footsteps sound loud.")
        print("Narrator: finally, peace and quiet. love that for us.")

        if found_library_clue == False:
            print("You look between two books and find a folded piece of paper.")
            print("It says:")
            print("'The fourth digit is the number of wheels on a bicycle.'")
            print("Narrator: whoever made this code REALLY likes random clues.")
            found_library_clue = True
        else:
            print("You already found the paper between the books.")

        print("\nWhat do you want to do?")
        print("1. Search the bookshelves")
        print("2. Return to the hallway")

        library_choice = input("Choose 1 or 2: ")

        while library_choice != "1" and library_choice != "2":
            print("Please choose 1 or 2.")
            library_choice = input("Choose 1 or 2: ")

        if library_choice == "1":
            print("You check the shelves for another clue.")
            print("You find a book about school history.")
            print("Unfortunately, it does not explain why you're trapped here.")
            print("useless. respectfully.")

        elif library_choice == "2":
            print("You quietly leave the Library.")
            room = "hallway"

    elif room == "cafeteria":
        print("\nYou are in the Cafeteria.")
        print("The tables are empty and the lights are off.")
        print("You are starting to get hungry.")
        print("Narrator: trapped at school AND no snacks?? this is actually evil.")

        if found_cafeteria_note == False:
            print("You look behind the counter and find a note.")
            print("It says 'If you're reading this, clean up your own mess.'")
            print("Narrator: not the time for a life lesson, please.")
            found_cafeteria_note = True
        else:
            print("You already checked behind the counter.")

        print("\nWhat do you want to do?")
        print("1. Search the tables")
        print("2. Check behind the counter again")
        print("3. Return to the hallway")

        cafeteria_choice = input("Choose 1, 2 or 3: ")

        while cafeteria_choice != "1" and cafeteria_choice != "2" and cafeteria_choice != "3":
            print("Please choose 1, 2 or 3.")
            cafeteria_choice = input("Choose 1, 2 or 3: ")

        if cafeteria_choice == "1":
            print("You search the tables.")
            print("You find one abandoned cracker.")
            print("You decide not to risk it. survival instincts <3")

        elif cafeteria_choice == "2":
            print("You check behind the counter again.")
            print("Just trays, cups, and a suspicious amount of ketchup.")

        elif cafeteria_choice == "3":
            print("You leave the Cafeteria and return to the hallway.")
            room = "hallway"

    elif room == "computer lab":
        print("\nYou are in the Computer Lab.")
        print("Rows of computers sit on the desks.")
        print("One computer is still on.")
        print("Narrator: oh?? technology might actually help us for once.")

        if found_computer_clue == False:
            print("You walk over to the computer.")
            print("A message appears on the screen:")
            print("'Security code reminder: put the digits in the order you found them.'")
            print("You remember the clues from the Science Room, locker room, Math Room, and Library.")
            found_computer_clue = True
        else:
            print("The computer still shows the same message.")

        print("\nWhat do you want to do?")
        print("1. Read the computer message again")
        print("2. Return to the hallway")

        computer_choice = input("Choose 1 or 2: ")

        while computer_choice != "1" and computer_choice != "2":
            print("Please choose 1 or 2.")
            computer_choice = input("Choose 1 or 2: ")

        if computer_choice == "1":
            print("The computer message says:")
            print("'Put the digits in order: Science, locker room, Math, Library.'")
            print("Narrator: okay, that's actually helpful for once.")

        elif computer_choice == "2":
            print("You leave the Computer Lab and return to the hallway.")
            room = "hallway"

    elif room == "security room":
        print("\nYou are in the Security Room.")
        print("There are monitors showing different parts of the school.")
        print("One screen shows the locked main exit.")
        print("Another shows the hallway you just walked through.")
        print("Narrator: so someone really could've seen you this whole time??")

        print("\nA keypad is attached to a locked box.")
        print("A note on the wall says:")
        print("'Enter the four-digit security code to access the emergency key.'")

        print("\nWhat do you want to do?")
        print("1. Enter the security code")
        print("2. Look at the monitors")
        print("3. Return to the hallway")

        security_choice = input("Choose 1, 2 or 3: ")

        while security_choice != "1" and security_choice != "2" and security_choice != "3":
            print("Please choose 1, 2 or 3.")
            security_choice = input("Choose 1, 2 or 3: ")

        if security_choice == "1":
            print("Narrator: You stare at the keypad.")
            print("Think about the clues you've found!")
            code = input("Enter the 4-digit security code: ")

            if code == "3742":
                print("The keypad beeps.")
                print("The locked box clicks open!")
                print("Inside is the special RED key!")
                print("Narrator: FINALLY. we are so out of here.")
                found_red_key = True
            else:
                print("The keypad flashes red.")
                print("Incorrect code! try again when you have figured it out <3")

        elif security_choice == "2":
            print("You look at the monitors.")
            print("One camera shows the gym.")
            print("Another shows the cafeteria.")
            print("The last monitor shows the main exit.")
            print("No people anywhere. creepy.")

        elif security_choice == "3":
            print("You leave the Security Room and return to the hallway.")
            room = "hallway"


if escaped_school == True:
    print("YAY YOU MADE IT CONGRATS!!!")
    print("this probably took you long to escape, its okay it took me even longer to make <3")