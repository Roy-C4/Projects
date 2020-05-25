print('Welcome to the Adventure'.title())
choice = input('are you ready? : Y/N: '.title()).upper()

if choice == "Y":
    print("Welcome to the Jungle Amigo!")
    print("Here you shall find only what you seek!")
elif choice == "N":
    print("You do not possess the courage. Come back when you are a man!")
    exit(0)
else:
    print("You must give a valid input")
print("\n")
print("You have entered the jungle.Infront you have the DEVILLA Mansion.The haunting atmosphere has made it more crooked!Guess there's no turning back now")

while True:
    forward = input("Press f to move forward into the mansion: ").upper()
    if forward.isalpha() == False:
        print("Please enter an alphabet")
        
    elif forward == "F":
        print("\nThe hallway of the mansion gives a creepy feeling amigo! To its right and left you have a door...")
        print("You have the stairs infront leading to the second level...ooooh the paintings give me the creeps...they stare into the soul!!")
        break
    else:
        print("Enter a valid input")

visit_left = False
visit_right = False

while True:
    sideways = input("Press R to go right or L to go left: ").upper()
    
    if sideways == "R":
        visit_right = True
        print("You have Entered Your room to the right.The vines of the trees have destroyed the dilapidated walls!")
        while True:
            direction = input("Press F/B/L/R to move: ").upper()
            if direction == "R":
                print("There are walls Amigo! You cant move further in this direction. You can go to your left.")
            elif direction == "B":
                print("You have comeback to the hallway.")
                break
            elif direction == "L":
                print("There is a bunch of old caskets..Seems pretty empty to me!Lets go back..")
            elif direction == "F":
                print("Thats Count Vermont.. the owner of the house! Relax its just a painting!")
            else :
                print("Invalid input")
            
    elif sideways == "L":
        visit_left = True
        print("You have Entered Your room to the left.The room smells of old cat pee and coconut milk!")
        while True:
            direction = input("Press F/B/L/R to move: ").upper()
            if direction == "R":
                print("Oh my! The shackles thrusted in the walls...Looks like someone was chained here amigo!.")
            elif direction == "B":
                print("You have comeback to the hallway.")
                break
            elif direction == "L":
                print("There is an old chair..looks like an electrocuting chair!..")
                while True:
                    object = input("Looks like we found a... key. Press P to pick it up: ").upper()
                    if object == "P":
                        print("Good job!")
                        break
                    else:
                        print("You'll need it later.You must pick it up!")
            elif direction == "F":
                print("There is a wall..You cant go further!")
            else :
                print("Invalid input")

        
    if visit_left & visit_right == True:
        
        break
    else:
        pass
print("Lets move up!")

while True:
    forward = input(" Press F to move forward or B to get out of here:  ").upper()
    if forward == "F":
        print("\nNice that we have made it to the second level! So many doors so many secrets!")
        print("WATCH OUT! THERES A GIANT NINJA CENTIPEDE!! Look there's a fireplace poker. Use it to your advantage")

        while True:
                poker = input("QUICK! Press P to pick up fireplace poker:  ").upper()
                if poker == "P":
                    print("Good job!")
                    break
                else:
                    print("QUICK! PICK IT UP!")
        print("Now we need to fight it off. Hit in the following sequence: U,F,L,D,R,B")
        fight = ["U","F","L","D","R","B"]
        fight1 = []
        print("Enter input: ")

        for i in range(len(fight)):
            data = str(input().upper())
            fight1.append(data)

        for i in range(len(fight)):
            if fight[i] == fight1[i]:
                print("Good job")
            else:
                print("You died!") 
                exit(1)

        print("Great we have almost defeated the monster! Its creepy but it kinda looks like...the Count! ")
        print("\nMONSTER: YOU SHALL NOT PASS YET. ANSWER THE RIDDLE AND YOU MAY!TELL ME:")
        sumatra = 0

        while (sumatra<=2):
            sumatra += 1
            print("\nThe person who built it sold it. The person who bought it never used it. The person who used it never saw it. What is it?")
            while True: 
                hint = input("Should you need a hint press H else press N").upper()
                if hint == "H":
                    print("Its made of wood")
                    break
                elif hint == "N":
                    pass
                    break
                else:
                    print("Enter valid input")
            ans = input("Thats a brainer!Any suggestions amigo? ").title()
            if ans == "Coffin":
                print("WELL DONE! YOU MUST BE THE ONE HAVING THE KEY TO MY RELEASE")
                break
            else:
                print("YOU DIED!")
                exit(3)

        print("Good Job Amigo!\n Look at that door. Its huge. The centipede was guarding it. There must be something in it!")
        use_key = input("Use the key we picked up.Press Y").upper()
        if use_key == "Y":
            print("Use key to enter room")
            insert = input("Press I to Insert key: ").upper()
            if insert == "I":
                print("The door opened. Thats brilliant. Its a pretty big room to have. Smells like dust!")
                choice = input("Look theres a coffin. The count said soemthing about RELEASE. But will it be a good idea to open it ?y/n:  ").upper()
                while True:
                    if choice == "Y":
                        print("Lets do it! I was born ready!")
                        break
                    elif choice == "N":
                        print("I am scared! Lets go back")
                        exit(2)
                    else :
                        print("Invalid input")
                print("Well whatever you say amigo!")
                coffin = input("Press O to open: ").upper()
                while True:
                    if coffin == "O":
                        print("Look its the coffin of the COUNT!!!\nA shadow is rising!")
                        print("YOU HAVE RELEASED ME! NOW I CAN TRAVEL TO MY HEAVENLY ABODE! THANK YOU")
                        print("THAT WAS AWESOME!!")
                        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print ("YOU HAVE COMPLETED YOUR ADVENTURE")
                        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
                        exit(4)
                    else:
                        print("Invalid input")
            else:
                print("Enter valid input")
        break
    elif forward == "B":
        print("Okay scaredy-cat! See you later")
        break
        exit(5)
    else:
        print("Invalid input")







