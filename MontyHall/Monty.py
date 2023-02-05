#Imports and variables are declared
import random
A = "A"
B = "B"
C = "C"
doors = ["A", "B", "C"]
x = 0
switchWins = 0
noSwitchWins = 0
wins = 0
switchDefeats = 0
noSwitchDefeats = 0
defeats = 0

#The program begins while 'x' is lower than 10
while x < 7:
    prize = random.choice(doors)
    print("Welcome to the Monty Hall Game! I hope you have a great prize tonight!")
    choice = input("Please, choose a door between A, B or C: ")

    #The program checks if the selected door is where the car is
    if choice == prize:
        remainingDoors = list(set(doors) - set(prize))
        openDoor = random.choice(list(set(doors) - set(random.choice(remainingDoors))))
        alternateDoor = random.choice(list(set(doors) - set(openDoor) - set(prize)))
    else:
        openDoor = random.choice(list(set(doors) - set(choice) - set(prize)))
        alternateDoor = random.choice(list(set(doors) - set(openDoor) - set(choice)))
    
    #The program chooses to open the OpenDoor where there is a goat
    print("Ok then, I'll open the " + openDoor + " door! Wow, there is a goat here!")

    secondChoice = input("Alright then, would you like to open the remaining door? (Yes/No): ")

    if secondChoice == "y" or secondChoice == "Yes" or secondChoice == "yes" or secondChoice == "Y":
        print("The door you will open is the " + alternateDoor + " door.")
        if alternateDoor == prize:
            print("You win! The car was in the " + alternateDoor + " door!")
            x+=1
            switchWins +=1
            wins += 1
        else:
            print("I'm sorry, but the car was in the " + choice + " door.")
            switchDefeats +=1
            defeats +=1
            x+=1
    elif secondChoice == "n" or secondChoice == "No" or secondChoice == "no" or secondChoice == "N":
        if alternateDoor != prize:
            print("You win! The car was in the " + choice + " door!")
            x+=1
            noSwitchWins +=1
            wins +=1
        else:
            print("I'm sorry, but the car was in the " + alternateDoor + " door.")
            noSwitchDefeats +=1
            defeats +=1
            x+=1
            
#The results are given and the program ends
print("Number of wins: " + str(wins) + ".")
print("Number of switching wins: " + str(switchWins) + ".")
print("Number of non switching wins: " + str(noSwitchWins) + ".")
print("Percentage of switching wins: " + str((100*switchWins)/wins) + "%.")
print("Percentage of non switching wins: " + str((100*noSwitchWins)/wins) + "%.")
print("Number of defeats: " + str(defeats) + ".")
print("Number of switching defeats: " + str(switchDefeats) + ".")
print("Number of non switching defeats: " + str(noSwitchDefeats) + ".")
print("Percentage of switching defeats: " + str((100*switchDefeats)/defeats) + "%.")
print("Percentage of non switching defeats: " + str((100*noSwitchDefeats)/defeats) + "%.")