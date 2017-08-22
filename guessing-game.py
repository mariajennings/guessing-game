import random

name = raw_input("Hi! What's your name?")

print "Ok, %s, I'm thinking of a number between 1 and 100" % name

number = random.randint(1, 100)

print "shhhh --- the number is %i" % number

name_guess = int(raw_input("What's your guess?"))

times = 0

while name_guess != number:
    if name_guess < number:
        print "Your guess is too low, try again!"
        times = times + 1
        name_guess = int(raw_input("What's your guess?"))
    elif name_guess > number:
        print "Your guess it too high, try again!"
        times = times + 1
        name_guess = int(raw_input("What's your guess?"))


if name_guess == number:
    print "You're right! You guess it in %i amount of tries." % times
