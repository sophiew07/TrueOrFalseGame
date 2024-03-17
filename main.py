#-----------------------------------------------------------------------------
# Name:        True or False?
# Purpose:     Entertain and educate the user
#
# Author:      Sophie Wong
# Created:     6-Jun-2023
# Updated:     19-Jun-2023
#-----------------------------------------------------------------------------


# Imports go at the top
from microbit import *

import random

# List of true and false questions
questions = {True:
                [
                "Sea otters have a favorite rock they use to break open food.",
                "It takes a sloth two weeks to digest a meal.",
                "Greenland is the largest island in the world.",
                "Alaska has the most active volcanoes of any state in the United States.",
                "The average human sneeze can be clocked at 100 miles an hour.",
                "Infants have more bones than adults.",
                "Hawaiian pizza comes from Canada.",
                "Santa Claus has his own postal code.",
                "An astronaut has played golf on the moon.",
                "The letter “J” is the only letter in the alphabet not included in the periodic table.",
                "Dr. Pepper is the oldest soft drink in America.",
                "Punxsutawney Phil is just a nickname for the famous groundhog.",
                "Pepperoni is the most popular pizza topping in the US."
                ],

             False:
                 [
                "An ant can lift 1,000 times its body weight.",
                "The goat is the national animal of Scotland.",
                "The Atlantic Ocean is the biggest ocean on Earth.",
                "Most of the human brain is made of muscle.",
                "Taste buds can only be found on the tongue.",
                "Vanilla is the world’s most expensive spice.",
                "The tradition of dyeing Easter eggs started in the United States.",
                "Every golf ball has the same number of dimples.",
                "Pepsi was the first soft drink to be enjoyed in outer space.",
                "People who have chiclephobia are afraid of cats.",
                "John Glenn became the oldest astronaut when he traveled to space at the age of 53.",
                "Fortune cookies were invented in China.",
                "The official color of the Golden Gate Bridge in California is 'Tennessee Orange'."
                ]
            }


# Introduction + seeing if user wants to play
play = input("Welcome to True or False. Would you like to play? - ")
play = play.lower()
if play in "no":
    print("See you next time!")
while play not in ["yes","no"]:
    play = input("Please put 'yes' or 'no'. - ")
while play in "yes":
    # Finding how many rounds the user wants to play
    userRounds = int(input("How many rounds would you like to play? - "))
    while userRounds < 0 or userRounds > 26:
       # Supposedly, playing 26 rounds means each question will only appear once (26 questions total)
        userRounds = int(input("Please put a number between 1 to 26. - "))

    # Game explanation
    print("Press button A when you believe the answer is true, and press button B if you think the answer is false. For each question, you have 3 seconds to answer. Let's start!")
    sleep(8000)

    # Giving values to variables
    trueQuestion = ''
    falseQuestion = ''
    playerPoints = 0

    # Each round
    for gameQuestions in range(userRounds):
        # Randomizing true and false questions
        trueQuestion = random.choice(questions[True])
        falseQuestion = random.choice(questions[False])
        
        # Choosing to display either true question or false question
        userQuestion = random.choice([trueQuestion,falseQuestion])
        print()
        print("True or False? - " + str(userQuestion))
        
        if userQuestion == trueQuestion:
            sleep(3000)
            # Checks for presses
            for press in range(10):
                sleep(100)
            if button_a.was_pressed():
                # Correct
                display.show(Image.YES)
                playerPoints += 1
            elif button_b.was_pressed():
                # Incorrect
                display.show(Image.NO)
                playerPoints -= 1
            else:
                # No button is pressed (no response)
                display.show(Image('00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '90909'))
        elif userQuestion == falseQuestion:
            sleep(3000)
            # Checks for presses
            for presses in range(10):
                sleep(100)
            if button_b.was_pressed():
                # Correct
                display.show(Image.YES)
                playerPoints += 1
            elif button_a.was_pressed():
                # Incorrect
                display.show(Image.NO)
                playerPoints -= 1
            else:
                # No button is pressed (no response)
                display.show(Image('00000:'
                                   '00000:'
                                   '00000:'
                                   '00000:'
                                   '90909'))
        
        # User score
        print("Score: " + str(playerPoints))
    
    # End of game/play again
    if playerPoints >= 5:
        play = input("Decent score! Would you like to play again? - ")
    elif playerPoints >= 1 and playerPoints <= 4:
        play = input("Your score was quite low... Would you like to play again? - ")
    else:
        play = input("Wow, that's a pretty bad score... Would you like to try again? - ")
    