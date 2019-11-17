import random as r
import time as t
import os


#creating a function that controls HP (hit or miss)

def hit(HP):
	HP -= 1
	print(start + "You just got hit!" + end)
	print()
	print("Press 'Enter' to reveal your current status:")
	input()
	print(start + "HP: " + str(HP) + end)
	print(start + "ATP: " + str(ATP) + end)

	return HP

def miss(HP):
	HP = HP
	print(start + "You just avoided a hit!" + end)
	print()
	print("Press 'Enter' to reveal your current status:")
	input()
	print(start + "HP: " + str(HP) + end)
	print(start + "ATP: " + str(ATP) + end)
	

	return HP

#defining a function that rolls a dice and tells the player what features were unlocked

def rollDice():
	diceResults = [1, 2, 3, 4, 5, 6]
	result = r.choice(diceResults)
	print(start + "You just rolled a: " + str(result) + end)
	print()
	
	if result == 1:
		print(start + "You can only see the virus's lifeSpan." + end)
		print()
	elif result == 2:
		print(start + "You can only see the virus's lifeSpan and size." + end)
		print()
	elif result == 3:
		print(start + "You can randomly see two of the virus's: lifeSpan, size, and texture." + end)
		print()
	elif result == 4:
		print(start + "You can randomly see two of the virus's: lifeSpan, size, texture, and color." + end)
		print()
	elif result == 5:
		print(start + "You can randomly see two of the virus's: lifeSpan, size, texture, color, and shape." + end)
		print()
	else:
		print()

	return result

#defining the function that allows the player to add "1" to the roll's result

def incrementRoll(ATP, result):
	ATP -= 5
	result += 1
	print("You just added 1 to the result of the dice's roll in exchange for 5 ATP.")
	print()
	print("Now, you rolled a: ", result)
	print("ATP: ", ATP)

	return ATP, result

#defining the function that allows the player to subtract "1" to the roll's result

def reduceRoll(ATP, result):
	ATP += 1
	result -= 1
	print("You just subtracted 1 from the result of the dice's roll and gained 1 ATP.")
	print()
	print("Now, you rolled a: ", result)
	print("ATP: ", ATP)

	return ATP, result

#Draw random card(s)

def draw():
	if result == 1:
		print(start + "One of the virus's attributes is: " + str(attributes[0]) + end)
	if result == 2:
		print(start + "One of the virus's attributes is: " + str(attributes[0]) + end)
		print(start + "And the other is: " + str(attributes[1]) + end)
	if result == 3:
		threeRoll = []
		threeRoll.append(attributes[0])
		threeRoll.append(attributes[1])
		threeRoll.append(attributes[2])
		third = r.sample(threeRoll, 2)
		print(start + "One of the virus's attributes is: " + str(third[0]) + end)
		print(start + "And the other is: " + str(third[1]) + end)
	if result == 4:
		fourRoll = []
		fourRoll.append(attributes[0])
		fourRoll.append(attributes[1])
		fourRoll.append(attributes[2])
		fourRoll.append(attributes[3])
		fourth = r.sample(fourRoll, 2)
		print(start + "One of the virus's attributes is: " + str(fourth[0]) + end)
		print(start + "And the other is: " + str(fourth[1]) + end)
	if result == 5:
		fiveRoll = []
		fiveRoll.append(attributes[0])
		fiveRoll.append(attributes[1])
		fiveRoll.append(attributes[2])
		fiveRoll.append(attributes[3])
		fiveRoll.append(attributes[4])
		fifth = r.sample(fiveRoll, 2)
		print(start + "One of the virus's attributes is: " + str(fifth[0]) + end)
		print(start + "And the other is: " + str(fifth[1]) + end)
	if result == 6:
		sixRoll = []
		print("Two of the following features:")
		print("lifeSpan")
		print("size")
		print("texture")
		print("color")
		print("shape")
		print()

		sixth1 = input()
		if sixth1 == "lifeSpan":
			sixRoll.append(attributes[0])
		if sixth1 == "size":
			sixRoll.append(attributes[1])
		if sixth1 == "texture":
			sixRoll.append(attributes[2])
		if sixth1 == "color":
			sixRoll.append(attributes[3])
		if sixth1 == "shape":
			sixRoll.append(attributes[4])

		sixth2 = input()
		if sixth2 == "lifeSpan":
			sixRoll.append(attributes[0])
		if sixth2 == "size":
			sixRoll.append(attributes[1])
		if sixth2 == "texture":
			sixRoll.append(attributes[2])
		if sixth2 == "color":
			sixRoll.append(attributes[3])
		if sixth2 == "shape":
			sixRoll.append(attributes[4])

		sixth = r.sample(sixRoll, 2)
		print(start + "One of the virus's attributes is: " + str(sixth[0]) + end)
		print(start + "And the other is: " + str(sixth[1]) + end)

#swap immunities at the end of each turn

def swapImmunity(ATP):
	print("Your current immunities are: ", immunities)

	#naming the three immunities

	firstImmunity = immunities[0]
	secondImmunity = immunities[1]
	thirdImmunity = immunities[2]

	remove = input("What immunity would you like to remove? ")

	if remove == firstImmunity:
		immunities.remove(immunities[0])
	if remove == secondImmunity:
		immunities.remove(immunities[1])
	if remove == thirdImmunity:
		immunities.remove(immunities[2])

	add = input("What immunity would you like to add? ")

	if add in lifeSpan:
		ATP -= 1
	if add in size:
		ATP -= 1
	if add in texture:
		ATP -= 2
	if add in color:
		ATP -= 3
	if add in shape:
		ATP -= 4
	
	immunities.append(add)
	
	print(start + "Your current immunities are: " + str(immunities[0]) + ", " + str(immunities[1]) + ", and " + str(immunities[2]) + end)
	print(start + "ATP: " + str(ATP) + end)
	return ATP

#function that reveals a randomly generated combination of cells that were destroyed by the virus because they didn't have a combination of all three constant attributes

def virusPast(ATP):
	pastCells = int(input("There are many cells that could not stand up to this virus, " + start + "how many of them would you like to see? " + end))
	print(start + "The immunities for the past cells are: " + end)
	for i in range(pastCells):
		while True:
			firstFeature = r.choice(features)

			secondFeature = r.choice(features)
			while True:
				if(secondFeature == firstFeature):
					secondFeature = r.choice(features)
				else:
					secondFeature = secondFeature
					break

			thirdFeature = r.choice(features)
			while True:
				if(thirdFeature == firstFeature or thirdFeature == secondFeature):
					thirdFeature = r.choice(features)
				else:
					thirdFeature = thirdFeature
					break
			firstImmunity = r.choice(firstFeature)
			secondImmunity = r.choice(secondFeature)
			thirdImmunity = r.choice(thirdFeature)
			pastImmunity = [firstImmunity, secondImmunity, thirdImmunity]

			if set(pastImmunity) != set(constants):
				print("		-" + start + str(pastImmunity[0]) + ", " + str(pastImmunity[1]) + ", and " + str(pastImmunity[2]) + end)
				break

	ATP -= pastCells

	print(start + "ATP: " + str(ATP) + end)
	return ATP

#function that reveals a feature of the player's choice for 10 ATP

def revealFeature(ATP):
	print()
	reveal = input("Which feature would you like to see in exchange for 10 ATP? ")

	if reveal == "lifeSpan":
		revealed = attributes[0]
	if reveal == "size":
		revealed = attributes[1]
	if reveal == "texture":
		revealed = attributes[2]
	if reveal == "color":
		revealed = attributes[3]
	if reveal == "shape":
		revealed = attributes[4]

	print("The attribute of " + str(reveal) + " that the virus has is " + start + str(revealed) + end)
	ATP -= 10
	print(start + "ATP: " + str(ATP) + end)

	return ATP

#defining a function that mutates the two changeable attributes of the virus while keeping the constants

def mutate(attributes):

	if attributes[0] not in constants:
		attributes[0] = r.choice(lifeSpan)

	if attributes[1] not in constants:
		attributes[1] = r.choice(size)

	if attributes[2] not in constants:
		attributes[2] = r.choice(texture)

	if attributes[3] not in constants:
		attributes[3] = r.choice(color)

	if attributes[4] not in constants:
		attributes[4] = r.choice(shape)

	return attributes

#defining a function that sorts the attributes every turn

def sort(attributes):

	sortedAttributes = []

	for att1 in attributes:
		if att1 in lifeSpan:
			sortedAttributes.append(att1)
			break

	for att2 in attributes:
		if att2 in size:
			sortedAttributes.append(att2)
			break

	for att3 in attributes:
		if att3 in texture:
			sortedAttributes.append(att3)
			break

	for att4 in attributes:
		if att4 in color:
			sortedAttributes.append(att4)
			break

	for att5 in attributes:
		if att5 in shape:
			sortedAttributes.append(att5)
			break

	attributes = sortedAttributes

	return attributes












































#These are all the cards in the game

lifeSpan = ["oneDay", "twoDays", "threeDays", "fourDays", "fiveDays"]
size = ["tiny", "small", "medium", "large", "humongous"]
texture = ["lumpy", "hard", "rough", "gritty", "soft"]
color = ["red", "green", "blue", "black", "white"]
shape = ["spherical", "linear", "spiral", "bullet", "wavy"]

features = [lifeSpan, size, texture, color, shape]

#pregame stage

#virus's attributes are randomized

attributes = []

att1 = r.choice(lifeSpan)
att2 = r.choice(size)
att3 = r.choice(texture)
att4 = r.choice(color)
att5 = r.choice(shape)

attributes.append(att1)
attributes.append(att2)
attributes.append(att3)
attributes.append(att4)
attributes.append(att5)

#print("The virus's attributes are: ", attributes)

#virus's constants are randomized

constants = r.sample(attributes, 3)

print("constants: ", constants)

#beginning statement

#for bold text

start = "\033[1m"
end = "\033[0;0m"

input(start + "Press 'Enter' to start..." + end)
print()

os.system("clear")

print(start + "Welcome to Go Viral!" + end)
print()


#adding a dice roll for picking initial immunities

dice = [1, 2, 3, 4, 5, 6]

diceValues = r.sample(dice, 3)

print("Roll the dice three times to determine the features from which your initial three immunities will be randomized from:")
print()
print("Dice values will unlock the features as follows:")

print("Rolling a 1 => Life Span")
print("Rolling a 2 => Size")
print("Rolling a 3 => Texture")
print("Rolling a 4 => Color")
print("Rolling a 5 => Shape")
print("Rolling a 6 => A feature of your choice")
print()
input("Press 'Enter' to roll the first dice...")
print()
print(start + "You just rolled a: ", str(diceValues[0]) + end)
print()
input("Press 'Enter' to roll the second dice...")
print()
print(start + "You just rolled a: ", str(diceValues[1]) + end)
print()
input("Press 'Enter' to roll the third dice...")
print()
print(start + "You just rolled a: ", str(diceValues[2]) + end)
print()
print("The results of the dice rolls are: ", diceValues)
print()

#checking which features the cell draws its immunities from using the results of the dice rolls

immunities = []

if dice[0] in diceValues:
	immunities.append(r.choice(lifeSpan))
if dice[1] in diceValues:
	immunities.append(r.choice(size))
if dice[2] in diceValues:
	immunities.append(r.choice(texture))
if dice[3] in diceValues:
	immunities.append(r.choice(color))
if dice[4] in diceValues:
	immunities.append(r.choice(shape))
if dice[5] in diceValues:
	print("Because you rolled a '6', enter the feature that you wish to select an immunity from at random from the following choices: ")
	print()
	if dice[0] not in diceValues:
		print("lifeSpan")
	if dice[1] not in diceValues:
		print("size")
	if dice[2] not in diceValues:
		print("texture")
	if dice[3] not in diceValues:
		print("color")
	if dice[4] not in diceValues:
		print("shape")
	print()
	chosenImmunity = input()
	print()

	#chosenImmunity = input("Enter the feature that you wish to select an immunity from at random: ")

	if chosenImmunity == "lifeSpan":
		immunities.append(r.choice(lifeSpan))
	elif chosenImmunity == "size":
		immunities.append(r.choice(size))
	elif chosenImmunity == "texture":
		immunities.append(r.choice(texture))
	elif chosenImmunity == "color":
		immunities.append(r.choice(color))
	else:
		immunities.append(r.choice(shape))

input("Press 'Enter' to reveal your initial immunites...")
print()
print(start + "The cell's initial immunities are: " + str(immunities[0]) + ", " + str(immunities[1]) + ", and " + str(immunities[2]) + end)
print()
print("This is the end of the pregame stage.")
print()
input(start + "Press 'Enter' to start the first round..." + end)

os.system("clear")

#ingame stage

#setting the health points and energy points

HP = 10

ATP = 20

print(start + "HP" + end + " are health points. You lose one HP every round if you fail to match your immunities with the virus's constant attributes.")
input()
print(start + "ATP" + end + " are energy points. There are ways to gain and lose ATP based on your purchases and actions during the game.")
input()
print("You " + start + "win" + end + " the game by matching your immunities with the virus's constant attributes.")

print("You " + start + "lose" + end + " the game if you run out of HP or ATP, whichever happens first.")
print()
input("Press 'Enter' to see your initial status...")

os.system("clear")

print(start + "Starting HP: " + str(HP) + end)

print(start + "Starting ATP: " + str(ATP) + end)
print()
input("Press 'Enter' to continue...")

#checking if the cell's immunities already match the virus's attributes

while HP > 0 and ATP > 0 and set(immunities) != set(constants):
	
	os.system("clear")
	print(start + "There is a virus that is approaching!" + end + " Watch out!!! If you have the correct combination of immunites, you will defeat it. Otherwise, you will gradually lose HP until it defeats you.")
	print()
	input("Press 'Enter' to find out whether you got hit by the virus or not...")
	print()

	if set(immunities) == constants:
		HP = miss(HP)

	elif set(immunities) in attributes:
		HP = miss(HP)

	else:
		HP = hit(HP)

	print()

	#calling the dice roll funtion

	input()
	print("In order to see the virus's attribute(s), roll the dice to see the virus's features from which an immunity will be drawn from, as follow:")
	print("Rolling a 1 => only Life Span")
	print("Rolling a 2 => Life Span & Size")
	print("Rolling a 3 => two of Life Span, Size, & Texture at random")
	print("Rolling a 4 => two of Life Span, Size, Texture, & Color at random")
	print("Rolling a 5 => two of Life Span, Size, Texture, Color, & Shape at random")
	print("Rolling a 6 => Any two features of your choice at random")
	
	print()

	print("Press 'Enter' to roll the dice...")
	input()
	result = rollDice()

	print("Press 'Enter' to decide on what you would like to do with the result of the dice roll...")
	input()
	print("You can either:") 
	print(start + "1- " + end + "Continue the round with the previous roll, or") 
	print(start + "2- " + end + "Add '1' to the roll in exchange for 5 ATP, or")
	print(start + "3- " + end + "Subtract '1' from the roll and gain 1 ATP")
	print()

	#calling the increment function

	changeRoll = input("Enter the number corresponding to the action you would like to take with the result of the dice roll: ")
	if changeRoll == "2":
		ATP, result = incrementRoll(ATP, result)
	elif changeRoll == "3":
		ATP, result = reduceRoll(ATP, result)
	else:
		pass

	#drawing attributes at random to feed the cell with information

	print()
	print("Based on your roll, you can now see: ")
	print()
	attributes = sort(attributes)
	draw()
	attributes = sort(attributes)

	#player's actions in round

	menu = True

	while menu == True:
		print()
		print("What would you like to do now?")
		print()
		print(start + "1- " + end + "Swap an immunity: " + start + "1-4 ATPs" + end)
		print("		-Swapping for Life Span: " + start + "1 ATP" + end)
		print("		-Swapping for Size: " + start + "1 ATP" + end)
		print("		-Swapping for Texture: " + start + "2 ATPs" + end)
		print("		-Swapping for Color: " + start + "3 ATPs" + end)
		print("		-Swapping for Shape: " + start + "4 ATPs" + end)
		print(start + "		*Your current immunities are: " + str(immunities[0]) + ", " + str(immunities[1]) + ", and " + str(immunities[2]) + end)
		print(start + "2- " + end + "Reveal virus past: " + start + "1 ATP / cell" + end)
		print(start + "3- " + end + "Reveal certain feature: " + start + "10 ATP" + end)
		print(start + "4- " + end + "Go to next round")
		print()
		action = input(start + "Enter the number " + end + "that corresponds to the action you would like to do. ")

		#calling the swap immunity function to allow the player to make changes

		if action == "1":
			ATP = swapImmunity(ATP)

		#calling the function that reveals randomly generated sets of combinations of cells with immunities that could not protect them against the virus

		if action == "2":
			ATP = virusPast(ATP)

		#calling the function that reveals a certain function, perhaps the most expensive purchase of the game

		if action == "3":
			ATP = revealFeature(ATP)

		if action == "4":
			menu = False

	os.system("clear")

	#calling the function that sorts the attributes as follows: lifeSpan, size, texture, color, and shape

	attributes = sort(attributes)

	#calling the mutating function that randomizes the nonconstant attributes of the virus

	attributes = mutate(attributes)

	#calling the function that sorts the attributes after mutation as follows: lifeSpan, size, texture, color, and shape

	attributes = sort(attributes)

if set(immunities) == set(constants):
	os.system("clear")
	print("Congratulations! You win the game!")
	score = (HP*10) + (ATP*10)
	print("Final Score: ", score)
else:
	os.system("clear")
	print("You lose :(")
	print("The constant attributes were: ", constants)
	print("Better luck next time...")