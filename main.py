# copyright Kendrew Shen 2022
import random

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
# about this project
# def about():
 # print("This Projected was created by Kendrew")
 # print("ⓒKendrew All rights reserved")
  

# Functions

def village():
  print("you are in the village square")
  print("Where would you like to go?")
  print("A-Go to the local pub")
  print("B-sleep at the local inn")
  print("C-Continue your journey")
  print("please enter your choice:")




############################################
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
 #if Menu == "M":
   #print("Menu")
  


C = "Press enter to continue"
print("Welcome to the Grass is always greener")
# Possible Bar Charaters
BC = ['Johnny','Jacob','Alfred']


input(C)
NAME = input("What is your name?:")

if NAME == "Kendrew":

  input("Press any key to continue")

print("Choose 1 of the following options")
print("A-Start your adventure")
print("B-About this project")
print("C-Dev Menu")\

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
if NS == "S":
  print("you have gone south of the village")


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
if Choice == "A":
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
choice2 = input()

if choice2 == '1':
  print("Has joined your pary")
  Party.append("Jeff")
elif choice2 == '2':
  print("You try to start a fight, but you got knocked out,out of pain you runaway -50 health points")
health - fifty
print(health)
print(Party)
village()




