from random import randint

print("Ghost game is about to start ...")

feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 3)
    
    print("Three doors ahead ... ")
    print("A ghost is behind one.")
    print("Which door door do you open?")

    while True:
        try:
            door_num = int(input("1, 2 or 3?"))
        except ValueError:
            print("That's not a number!")
            continue
        else:
            if 1 <= door_num <= 3:
                break
            else:
                print("Invalid door")

    if (door_num == ghost_door):
        print("GHOST!!!")
        print("Run away!!\n")
        feeling_brave = False
    else:
        print("Phew ... no ghost!")
        print("You enter the next room.\n")
        score = score + 1

print("Game over! You scored: ", score)