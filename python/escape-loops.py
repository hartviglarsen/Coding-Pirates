table = 31

for i in range(1, 13):
    print("What's", i, "x", table, "?")
    guess = input()
    answer = i * table

    if int(guess) == answer:
        print("Correct!")
    else:
        print("Nope.. it's ", answer)
        break

print("Done")