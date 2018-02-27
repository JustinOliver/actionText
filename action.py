#!python3
# action.py - A text adventure action game

import random
import sys
from time import sleep

# Define some hero classes for player to choose from

class Hero(object):
	def __init__(self, health, attack, ranged, defense, magic, gold, name):
		self.health = health
		self.attack = attack
		self.ranged = ranged
		self.defense = defense
		self.magic = magic
		self.gold = gold
		self.name = name

	'''def get_health(self):
		return self.health
	def get_attack(self):
		return self.attack
	def get_ranged(self):
		return self.ranged
	def get_defense(self):
		return self.defense
	def get_magic(self):
		return self.magic
	def get_gold(self):
		return self.gold
	def get_name(self):
		return self.name
	def set_health(self, newhealth):
		self.health = newhealth
	def set_attack(self, newattack):
		self.attack = newattack
	def set_ranged(self, newranged):
		self.ranged = newranged
	def set_defense(self, newdefense):
		self.defense = newdefense
	def set_magic(self, newmagic):
		self.magic = newmagic
	def set_gold(self, newgold):
		self.gold = newgold
	def set_name(self, newname=""):
		self.name = newname*'''


	#def __str__(self):
		#return"<"+str(self.health) + "," +str(self.attack) + "," + str(self.ranged) + "," + str(self.defense) + "," + str(self.magic) + "," + str(self.gold) + "," + str(self.name) + ">"






# Enemy Classes, villains the hero will fight

class Villain(object):
	def __init__(self, health, defense, attack, rarity, intro, name):
		self.health = health
		self.defense = defense
		self.attack = attack
		self.rarity = rarity
		self.intro = intro
		self.name = name


	'''def get_health(self):
		return self.health
	def get_attack(self):
		return self.attack
	def get_defense(self):
		return self.defense
	def get_rarity(self):
		return self.rarity
	def get_intro(self):
		return self.intro
	def get_name(self):
		return self.name
	def set_health(self, newhealth):
		self.health = newhealth
	def set_attack(self, newattack):
		self.attack = newattack
	def set_defense(self, newdefense):
		self.defense = newdefense
	def set_rarity(self, newrarity):
		self.rarity = newrarity
	def set_intro(self, newintro=""):
		self.intro = newintro
	def set_name(self, newname=""):
		self.name = newname'''

	#def __str__(self):
		#return"<"+str(self.health) + "," +str(self.defense) + "," + str(self.attack) + "," + str(self.rarity) + "," + str(self.intro) + "," + str(self.name) + ">"


class Loot(object):
	def __init__(self, health, defense, attack, ranged, score):
		self.health = health
		self.defense = defense
		self.attack = attack
		self.ranged = ranged
		self.score = score


# Characters

warrior = Hero(150, 50, 10, 100, 0, 0, "Warrior")
archer = Hero(125, 40, 50, 80, 0, 0, "Archer")
wizard = Hero(100, 30, 20, 70, 100, 0, "Wizard")

characters = [warrior, archer, wizard]


# Loot objects
rarity0 = Loot('health potion', 'wooden shield', 'wooden sword', 'simple bow', 10)
rarity1 = Loot('mega health potion', 'bronze shield', 'bronze axe', 'ranger bow', 20)
rarity2 = Loot('super mega health potion', 'chainmail', 'mace', 'trebuchet', 30)
rarity3 = Loot('diamond potion', 'invisibility cloak', 'diamond sword', 'pet alligator', 100)

#items =


# Villains
goblin = Villain(10, 10, 5, 0, 'I\'m not a ghoul!', 'goblin')
ghost = Villain(10, 12, 6, 1, 'BOOOOOO!!!', 'ghost')
dragon = Villain(10, 15, 10, 2, 'Where is Khallisi?', 'dragon')
demonDog = Villain(10, 2, 2, 3, 'Woof woof!', 'demonDog')

villains = [goblin, ghost, dragon, demonDog]


# Define variables to be used during game.

inventory = []
enemyKills = 0

def chooseCharacter():
	while True:
		try:
			choice = int(input("1. Warrior\n2. Wizard\n3. Archer\nEnter the number of your choice now!:"))
			if choice == 1:
				character = warrior

			elif choice == 2:
				character = wizard

			elif choice == 3:
				character = archer
			else:
				continue

		except ValueError:
			continue
		else:
			break
	sleep(.2)
	print("Good choice my friend, you are a ", character.name)
	return character



def inventoryShow():
	if len(inventory) == 0:
		sleep(.2)
		print("Your inventory is empty")
		return
	else:
		sleep(.2)
		print("You have the following in your inventory..." + str(inventory))
		return


def lootCheck(loot):
	if loot in inventory:
		sleep(.2)
		print("You already have this item, so you leave it for another adventurer!")
		return
	else:
		inventory.append(loot)
		return

def useItem():
	y = rarity0.health
	sleep(.2)
	x = input("Are you sure you want to use " + y + "? Enter yes or no:\n")
	sleep(.2)
	if x.lower() == "yes":
		if y in inventory:
			print("You have increased your " + y + " by " + str(rarity0.score) + " points!")
			character.health += rarity0.score
			inventory.remove(y)
		else:
			print("You don't have " + y + "in your inventory silly pants!")
			return

	elif x.lower() == "no":
		print("Okay, we won't use that.")
		return
	else:
		print("I didn't understand your input, so we are going  to put that item away. Carry on my wayward son!")
		return



def loot(enemy):
	x= random.randint(1, 4)
	#if x == 0:
	loot = rarity0.health
	#elif x == 1:
	#	loot = rarity + str(enemy.rarity) + '.defense'
	#elif x == 2:
	#	loot = rarity + str(enemy.rarity) + '.attack'
	#elif x == 3:
	#	loot = 'rarity' + str(enemy.rarity) + '.ranged'
	#else:
	#	print("no loot for you, something happened")
	#	return
	#loot1 = loot
	sleep(.2)
	print("The enemy has dropped a...", loot)
	lootCheck(loot)

def decision():
	while True:

		try:
			sleep(.2)
			print("You have 2 choices of what you can do (actually 4)")
			sleep(.2)
			decision = int(input("1. Attack\n2. Check Inventory\n3. Run\n4. Use Item\nEnter the number of your choice:"))
			if decision == 1:
				return("attack")
			elif decision == 2:
				inventoryShow()
				continue
			elif decision == 3:
				return("run")
			elif decision == 4:
				useItem()
				continue
			else:
				sleep(.2)
				print("I didn't get that, lets try again. Push ctrl+c to exit the game at anytime")
				continue
		except ValueError:
			continue
		else:
			break

#def run():
	#print

def attack():
	sleep(.2)
	attackMethod = int(input("1. Sword\n2. Magic\n3. Ranged\n What weapon would you like to attack with?: "))
	if attackMethod == 1:
		sleep(.2)
		print("Lets attack with the sword!")
		return "sword"
	elif attackMethod == 2:
		sleep(.2)
		print("Alright Harry, let's use some magic")
		return "magic"
	elif attackMethod == 3:
		sleep(.2)
		print("Lets use a ranged attack!")
		return "ranged"
	else:
		sleep(.2)
		print("I didn't get that, lets try again. Push ctrl+c to exit the game at anytime")
		attack()





def battlestate():
	global enemyKills
	while True:
		battleState = 1
		enemy = villains[random.randint(0, 3)]
		attackList = [character.attack, character.magic, character.ranged]
		sleep(.2)
		print("You see an enemy coming from a distance...")
		sleep(.2)
		print("It's a ", enemy.name, "!!!")
		sleep(.2)
		print(enemy.intro)
		sleep(.2)
		print("Get ready to fight!!!")
		result = decision()

		if result == "run":
			sleep(.2)
			print("You ran away, nice job!")
			sys.exit()
		if result == "attack":
			sleep(.2)
			print("You have 3 attack options...\n")
			attackMethod = attack()

		while battleState == 1:
			miss = random.randint(0,10)
			if miss > 8:
				sleep(.2)
				print("Your attack missed!")
				sleep(.2)
				print("the enemy attacks!")
				sleep(.2)
				print("The", enemy.name, " takes a swipe")
				sleep(.2)
				damage = round(enemy.attack/character.defense, 2)
				character.health = character.health - damage
				sleep(.2)
				print("The remaining health is...", character.health)
				sleep(.2)
				if character.health < 1:
					sleep(.2)
					print("The hero has died!!!!")
					sys.exit()

			else:
				if attackMethod == "sword":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You swing your sword and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)

					if enemy.health <1:
						sleep(.2)
						print("you have defeated the", enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()

				elif attackMethod == "magic":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You swing your magic and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)


					if enemy.health < 1:
						sleep(.2)
						print("you have defeated the" + enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()

				elif attackMethod == "ranged":
					damage = round(attackList[0] / enemy.defense, 2)
					sleep(.2)
					print("You use your ranged and do...", damage, "damage")
					enemy.health = enemy.health - damage
					sleep(.2)
					print("Enemy health remaining:", enemy.health)

					if enemy.health < 1:
						sleep(.2)
						print("you have defeated the", enemy.name)
						sleep(1)
						enemy.health = 100
						battleState = 0
						loot(enemy)

					else:
						decision()
		enemyKills += 1
		if enemyKills == 10:
			sleep(.5)
			print("You win!")
			sys.exit()
		else:
			continue

print("You are challenged to defeat 10 monsters!")
sleep(.5)
print("But first who are you?....")
sleep(.5)
character = chooseCharacter()
sleep(.5)
battlestate()



