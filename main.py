# copyright Kendrew Shen 2022
import random
# Version 1.0.1 Alpha






# Important variables
Money = '1000'
HEALTH = '100'
health = 100
ATCK = [10,50,20,9]
Magic = [25,12,23,40,10]
Charisma = [10,15,20,25,30]
Null = '0'
Alive = 100 < 1
Party = []
fifty = 50
Monsters = ['Goblin','Dragon']
Dragonhp = 200
damage = [40,10,30,25]
XP = 0
Level = 1

String = "text"


# godmode





#######################
# creature health



# about this project
# def about():
 # print("This Projected was created by Kendrew")
 # print("ⓒKendrew All rights reserved")
  

# Functions
def lvlup():
  print(Level + 1)
  print("you leveled up!")
  
  

def village():
  Village = """you are in the village square
 Where would you like to go?
 A-Go to the local pub
 B-sleep at the local inn
 C-Continue your journey
 please enter your choice:""" 

  print(Village)
  
 
  
##########################################
def pub():
  
   if Choice == "R":
    print("You go to the local pub")
    print("Choose an option")
    print("1-Talk to others")
    print("2-return to village square")
    Choice1 = input()
    if Choice1 == '2':
     village()
   elif Choice1 == '1':
    print("you encounter another fellow traveler")
    input("Hey there,whats your name?")
    input("Oh cool, nice to meet you"+ NAME)
    input("Ask a question")
    print("1-Invite them to join your party")
    print("2-start a bar fight")
    print("3-walk away")
     
def combat():
  print(health)
  print(Party)
  print("F-fight the monster")
  print("R-Run")
  combat = input("what do you do")
  if combat == "F":
    print("possible attacks")
    print("A-Fire spell")
    attack = input("Chose an attack")
    if attack == 'A':
     print(random.choice-(Dragonhp))
  




      
###########################################
def northpath():
  print("you head north of the village")
  input()
  lvlup()

#print("A wild appears")
  #print(random.choice(Monsters))
  #combat()
###############################################################  
def southpath():
  print("you head south of the village")


###############################################################
def devm():
  print("Welcome to the dev menu")
  print("Here you can set your health to pretty much anything")
  print("or just leave this menu")

def mainroad():
  print("you have encountered a 2 way cross road")
  input(C)
  print("N to go north of starting village")
  print("S to go south of the starting village")
  print("R to return to village")
  print("please enter your choice:")
  choice3 = input()
  if choice3 == "N":
   northpath()
  elif choice3 == "S":
    southpath()  
  elif choice3 == "R":
    village()
  
  
 #if Menu == "M":
   #print("Menu")
  

# start
C = "Press enter to continue"
print("Welcome to the Grass is always greener")
# Possible Bar Charaters
BC = ['Johnny','Jacob','Alfred']


input("Press enter to begin your journey")
NAME = input("What is your name?:")
input("Press any key to continue")
print("Choose 1 of the following options")
print("A-Start your adventure")
print("B-About this project")
OPTION = input()
if OPTION == "A":
  print("You are:" + NAME)
  input("Press any key to continue")
  print("Choose your class")
  print("Mage")
  print("Paladin")
  Party.append(NAME)
CLASS = input()
if CLASS == "Paladin":
     print("you have chosen Paldain class")
if CLASS == "Mage":
  print("You have chosen mage class")
print("Health:" + HEALTH)
input(C)

  

# first possible adventure
mainroad()
NS = input()
if NS == "N":
  print("you have gone North of the village")
  northpath()
if NS == "S":
  print("you have gone south of the village")
if NS == "R":
  village()
Choice = input()
if Choice == "C":
  
   
 print(health)
print(Party)
input(C)

print("you are in the village square")
print("Where would you like to go?")
print("A-Go to the local pub")
print("B-sleep at the local inn")
print("C-Continue your journey")
print("please enter your choice:")
Choice = input()
if Choice == "C":
  print("you have encountered a 2 way cross road")
  input(C)
  print("N to go north of starting village")
  print("S to go south of the starting village")
  print("R to return to village")
  print("please enter your choice:")
  choice3 = input()
  if choice3 == "N":
   northpath()
  elif choice3 == "S":
    southpath()  
    

  



