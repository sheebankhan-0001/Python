import random

x="y"
while x=="y":
    randnumber = random.randint(1,6)
    if randnumber ==1:
        print("\n[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[     ]")
    if randnumber ==2:
        print("\n[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[     ]")
    elif randnumber ==3:
        print("\n[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif randnumber ==4:
        print("\n[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif randnumber ==5:
        print("\n[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif randnumber ==6:
        print("\n[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

    print("\nPRESS y TO ROLL THE DICE AGAIN e TO EXIT")
    x=input()
    print("Thank for using the dice")


