import random

name = raw_input("Hi! What's your name?")

print "Ok, %s, I'm thinking of a number between 1 and 100" % name

number = random.randint(1, 100)

name_guess = None

times = 0

play = "yes"

best_score = 0

print "shhhh --- the number is %i" % number

while play == "yes":
        while name_guess != number:
            if times == 3:
                print "too many tries!"
                play = raw_input("would you like to play again? yes or no?")
            else:
                try:
                    name_guess = int(raw_input("What's your guess?"))
                    times = times + 1
                except ValueError:
                    print "That's not an integer!!!!!"
                    continue
                if name_guess < number and name_guess > 0 and name_guess < 100:
                    print "Your guess is too low, try again!"
                elif name_guess > number and name_guess > 0 and name_guess < 100:
                    print "Your guess it too high, try again!"
                elif name_guess > 100 or name_guess < 1:
                    print "That guess is not in range, try again"

        if name_guess == number:
            times = times + 1
            print "You're right! You guessed it in %i amount of tries." % (times)
            if times < best_score or best_score == 0:
                best_score = times
                print "Congratulations! You have the highest score!"
            elif times > best_score:
                print "Keep trying to get the best score!"
            times = 0
            play = raw_input("would you like to play again? yes or no?")
            number = random.randint(1, 100)
            print "shhhh --- the number is %i" % number
            continue


