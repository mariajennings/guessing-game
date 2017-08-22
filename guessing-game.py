import random

name = raw_input("Hi! What's your name?")

print "Ok, %s, I'm thinking of a number between 1 and 100" % name

number = random.randint(1, 100)

print "shhhh --- the number is %i" % number

name_guess = int(raw_input("What's your guess?"))

times = 0

if name_guess <= 0 or name_guess > 100:
    print "Your guess is out of range. Try again!"
    name_guess = int(raw_input("What's your guess?"))
    times = times + 1

while name_guess != number:
    if name_guess < number:
        print "Your guess is too low, try again!"
        times = times + 1
        name_guess = int(raw_input("What's your guess?"))
    elif name_guess > number:
        print "Your guess it too high, try again!"
        times = times + 1
        name_guess = int(raw_input("What's your guess?"))
    elif name_guess > 100 or name_guess < 1:
        print "That guess is not in range, try again"
        name_guess = int(raw_input("What's your guess?"))

if name_guess == number:
    print "You're right! You guess it in %i amount of tries." % times
