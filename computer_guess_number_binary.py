import random
#random.seed(616)

print "You choose a number 1-1000, and I will guess it."
print

print "Type in 'l' and hit enter if I guess too low."
print "Type in 'h' and hit enter if I guess too high."
print "Type in 'y' if I guessed your number!"
print

high = 1000
low = 1
human_response = ""
while human_response != "y":
    guess = (high + low) / 2
    human_response = raw_input("Is your number "+str(guess)+"? ")
    if human_response == "l":
        low = guess + 1
    elif human_response == "h":
        high = guess - 1
            
print "Hooray!"

#Challenge 1
#   The above script has a section of code missing, denoted by the #...
#   Fix the missing section of code.

#Challenge 2
#   Edit this script to guess for numbers 1-100

#Challenge 3
#   What about 1-1000?