import random

random_number = random.randrange(10) + 1

print "Let's play a game!"
print "I've chosen a number between 1-10. Guess what it is!"

human_guess = -1
while human_guess != random_number:
    human_guess = int(raw_input("Your guess: "))
    if human_guess > random_number:
        print "Nope, it's lower..."
    elif human_guess < random_number:
        print "Nope, it's higher..."

print "You got it!"


# CHALLENGE 1
# Before starting the game, ask the user what their name is. Then change the line
#    that prints "Let's play a game!" to print out their name "Let's play a game, <name>!"

# CHALLENGE 2
# Instead of picking a number 1-10, have the game be a number 1-100.

# CHALLENGE 2
# Keep track of how many guesses the person made, and when they finally
#    guess the correct number, print out how many tries it took!