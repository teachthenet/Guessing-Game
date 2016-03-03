import random

print "You choose a number 1-10, and I will guess it."
print

print "Type in 'l' and hit enter if I guess too low."
print "Type in 'h' and hit enter if I guess too high."
print "Type in 'y' if I guessed your number!"
print

human_response = raw_input("Is your number 5? ")
if human_response == "l":
    human_response = raw_input("Is your number 7? ")
    if human_response == "l":
        human_response = raw_input("Is your number 9? ")
        #...
    elif human_response == "h":
        human_response = raw_input("Is your number 6? ")
elif human_response == "h":
    human_response = raw_input("Is your number 2? ")
    #...
        
if human_response == "y":
    print "Hooray!" 
else:
    print "Sorry, I got confused."
            
    
#Challenge 1
#   The above script has two sections of code missing, denoted by the #...
#   Fix those missing sections of code.