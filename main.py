import random

def guessingGame():
	print("This is the guessing game.")

def RPS():
	print("This is rock paper scissors.")
	print("1. Rock")
	print("2. Paper")
	print("3. Scissors")

	cpu = random.randint(1,3)
	userChoice = input("So, rock, paper, or scissors? 1, 2, or 3?")

	if(cpu == 1):
		if(userChoice == 1):
			print("TIE! ROCK AND ROCK ARE AT AN IMPASSE")
		if(userChoice == 2):
			print("YOU WIN! PAPER BEATS ROCK!")
		if(userChoice == 3):
			print("AWWW. ROCK BEATS SCISSORS. BETTER LUCK NEXT TIME.")
	
	if(cpu == 2):
		if(userChoice == 1):
			print("AWW. PAPER BEATS ROCK. BETTER LUCK NEXT TIME.")
		if(userChoice == 2):
			print("TIE! PAPER AND PAPER ARE AT A STANDSTILL!")
		if(userChoice == 3):
			print("CONGRAGULATIONS FOR BEATING THE FOUL PAPER CAPTAIN SCISSORS!")

	if(cpu == 3):
		if(userChoice == 1):
			print("YAY! ROCK BEATS SCISSORS")
		if(userChoice == 2):
			print("DAM IT (<-- PJO REFERENCE IN CASE YOU'RE DENSE)! SCISSORS BEAT PAPER!")
		if(userChoice == 3):
			print("YOU TIED! PAPER V PAPER")


def diceRoll():
	print("This is the dice roll.")
	dR = random.randint(1,6)
	userDice = (input("Which dice face do you think will roll? "))
	if(userDice == dR):
		print("Congrats! You nailed it!")
		main()
	else:
		print("Sorry! The number was " + str(dR) + ". Better luck next time.")
		main()

def fortuneTeller():
	print("This is the fortune teller.")
	fortuneList = ("Things that were valuable were rarely lost forever. Especially when everyone knew exactly where they were. - The Toll", "Today is a new day. Do something new. Befriend old enemies. Clenase yourself of old sins best forgotten.", "Believe in miracles and they'll never cease", "There's always a silver lining. Find it and revel in the small things.", "Enjoy the moment because who knows when they will ever happen again.", "If you ever feel forgotten, write down your stories. They'll become valuable one day.")

	print(fortuneList[random.randint(0,len(fortuneList)-1)])
#'main function'
#This is where we define how we want our program to run.

def main():
	print("This is the main function")

	#Tell the user their game options.
	#Ask user to choose one.
	#Call the correct function based on user input.

	print("1. Guessing Game") 
	print("2. Rock Paper Scissors")
	print("3. Dice Roll")
	print("4. Fortune Teller")
	userInput = int(input("Which would you like to play? Please enter the corresponding number: "))

	if(userInput == 1):
		guessingGame()
	elif(userInput == 2):
		RPS()
	elif(userInput == 3):
		diceRoll()
	elif(userInput == 4):
		fortuneTeller()
	else:
		print("Unfortunatly, that is not an option.")
		main()

#This controls the execution of our code

if __name__ == "__main__":
	main()