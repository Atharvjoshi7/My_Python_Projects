from turtle import left


name = input("type your name")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt rode, it has come to an end and you can go left or right, which way would you like to go ?").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("you walked a lot and ran out of water")

    else:
        print("not a valid option")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. do you talk to then (yes/no) ?")
        if answer =="yes":
            print("you talk to the stranger and win gold!")
        elif answer == "no":
            print("you ignore the stranger and they are angry you lose!")
        else:
            print("not a valid option")
    else:
        print("not a valid option")
else:
    print("not a valid option")
