import random

name = raw_input("Hi! What's your name?")

print "Ok, %s, I'm thinking of a number between 1 and 100" % name

number = random.randint(1, 100)

print "shhhh --- the number is %i" % number

name_guess = None


times = 0

while name_guess != number:
    try:
        name_guess = int(raw_input("What's your guess?"))
    except ValueError:
        print "That's not an integer!!!!!"
        times = times + 1
        continue
    if name_guess < number and name_guess > 0 and name_guess < 100:
        print "Your guess is too low, try again!"
        times = times + 1
    elif name_guess > number and name_guess > 0 and name_guess < 100:
        print "Your guess it too high, try again!"
        times = times + 1
    elif name_guess > 100 or name_guess < 1:
        print "That guess is not in range, try again"

if name_guess == number:
    print "You're right! You guess it in %i amount of tries." % times
