import random

lower = ["a", "b" , "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", "9", "i", "j", "k", "l", "?", "/", "+", "=", "$", "#", "!", "A", "B" , "C", "D", "E", "F", "G", "H", "O", "P", "Q", "R", "S", "T", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def convert(mylist):
    new = ""
    for x in mylist:
        new += x
    return new

mylist = random.choices(lower, weights = None, k=15)

print(convert(mylist))


