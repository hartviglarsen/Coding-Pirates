from random import randint

names = ["Trine", "Eric", "Mahmoud", "Morten"]
verbs = ["buys", "rides", "kicks", "punches"]
nouns = ["lion", "bicycle", "plane", "house"]

def pick(list):
    length = len(list)
    rand = randint(0, length - 1)
    word = list[rand]

    return word

while True:
    print(pick(names), pick(verbs), "a", pick(nouns), end = ".")
    input()
