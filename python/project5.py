from random import randint

names = ["Trine", "Eric", "Mahmoud", "Morten"]
verbs = ["buys", "rides", "kicks", "pounches"]
nouns = ["lion", "bicycle", "plane", "house"]

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    words_picked = words[num_picked]

    return words_picked

while True:
    print(pick(names), pick(verbs), pick(nouns), end = ".")
    input()