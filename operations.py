#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calculations
import sys
import math

def registerUser(connection):
  # Prompts for desired username and updates the database for the new user
  username = input('Please enter a username \n')
  currentUser = ''
  cur = connection.cursor()
  cur.execute("INSERT INTO user(name) VALUES ({}});".format(username))
  cur.close()

  # Stores the most recent user_id for that username.
  # (This was done because there might be duplicate usernames)
  cur2 = connection.cursor()
  cur2.execute("SELECT user_id FROM user WHERE name = {} ORDER BY id DESC LIMIT 1;".format(username))
  row = cur2.fetchone()
  key = row["user_id"]
  cur2.close()

  # Prints out username and user_id for reference.
  print("Your username is {} and your user_id is {}".format(username, key))
  currentUser = key
  return currentUser

def loginUser(connection):
  # Username and user_id both needed to login.
  username = input('Welcome back! Please enter your username \n')
  key = input('Please enter your user_id \n')
  currentUser = ''

  # Compares username and user_id to pairings in the user table.
  cur = connection.cursor()
  cur.execute("SELECT name FROM user where user_id = {}".format(key))
  row = cur.fetchone()
  if (row["name"] == username):
    currentUser = key
    print("Login successful.")
  else:
    print("Username and user_id do not match. Please log in again \n")
    return
  cur.close()
  return currentUser

def createCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  currentCharacter = input('Enter a name for your character: \n')
  char_race = input('Select a race: \n Dwarf / Elf / Halfling / Human / Dragonborn'
  ' / Gnome / Half-Elf / Half-Orc / Tiefling ') 
  if (char_race == "Dwarf"):
    char_subrace = input('Select a subrace: \n Hill Dwarf / Mountain Dwarf')
  elif (char_race == "Elf" ):
    char_subrace = input('Select a subrace: \n High Elf / Wood Elf / Dark Elf')
  elif (char_race == "Halfing"):
    char_subrace = input('Select a subrace: \n Lightfoot / Stout')
  elif (char_race == "Human"):
    char_subrace = 'None'  
  elif (char_race == "Dragonborn"):
    char_subrace = input('Select an ancestry: \n Black / Blue / Brass / Bronze / Copper'
    'Gold / Green / Red / Silver / White')
  elif (char_race == "Gnome"):
    char_subrace = input('Select a subrace: \n Forest Gnome / Rock Gnome')  
  elif (char_race == "Half-Elf"):
    char_subrace = 'None'
  elif (char_race == "Half-Orc"):
    char_subrace = 'None'
  elif (char_race == "Tiefling"):
    char_subrace = 'None'
  else:
    print("Invalid race. Please try again")
    return
    
  char_class = input('Select a class: \n Barbarian / Bard / Cleric / Druid / Fighter / Monk'
  '\n Paladin / Ranger / Rogue / Sorcerer / Warlock / Wizard')
  char_level = input('Starting level of your character \n Lv. ')
  
  # If level is high enough, assign subclass or prompt if multiple paths
  if (char_class == 'Barbarian' and char_level >= 3):
    char_subclass = 'Berserker'
  elif (char_class == 'Bard' and char_level >= 3):
    char_subclass = 'Lore'
  elif (char_class == 'Cleric'):
    char_subclass = input('Please select a divine domain: \n Knowledge / Life / Light / Nature / Tempest / Trickery / War')
  elif (char_class == 'Druid' and char_level >= 2):
    char_subclass = input('Please select a circle of the druids: \n Land / Moon')
  elif (char_class == 'Druid' and char_level >= 3):
    char_subclass = 'Champion'
  elif (char_class == 'Monk' and char_level >= 3):
    char_subclass = input('Please select a monastic tradition: \n Open Hand / Shadow / Four Elements')
  elif (char_class == 'Paladin' and char_level >= 3):
    char_subclass = input('Please select a sacred oath: \n Devotion / Ancients / Vengeance')
  elif (char_class == 'Ranger' and char_level >= 3):
    char_subclass = input('Please select a ranger archetype: \n Hunter / Beast Master')
  elif (char_class == 'Rogue' and char_level >= 3):
    char_subclass = 'Thief'
  elif (char_class == 'Sorcerer'):
    char_subclass = 'Draconic Bloodline'
  elif (char_class == 'Warlock'):
    char_subclass = 'Fiend' 
  elif (char_class == 'Wizard'):
    char_subclass = 'Evocation' 
  else:
    char_subclass = 'None'

  print('Write a background for your character (ctrl + d upon finish): ')
  char_background = sys.stdin.read()

  char_strength = input('Enter rolled strength for your character \n')
  char_dexterity = input('Enter rolled dexterity for your character \n')
  char_constitution = input('Enter rolled constitution for your character \n')
  char_charisma = input('Enter rolled charisma for your character \n')
  char_intelligence = input('Enter rolled intelligence for your character \n')
  char_wisdom = input('Enter rolled wisdom for your character \n')

  if (char_level == 1):
    proficiency = 2
  else:
    proficiency = 2 + math.floor((char_level - 1) / 4) 

  # INSERT ALL VALUES INTO CHARACTER TABLE
  cur = connection.cursor()
  cur.execute("INSERT INTO character (ch_name, ch_level, strength, dexterity, constitution, charisma, intelligence, wisdom, proficiency_bonus, "
  "user, class, subclass, race, subrace, background) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(
  currentCharacter, char_level, char_strength, char_dexterity, char_constitution, char_charisma, char_intelligence, char_wisdom, proficiency,
  currentUser, char_class, char_subclass, char_race, char_subrace, char_background))
  cur.close()
  return currentCharacter

def loadCharacter(currentUser, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # LIST ALL CHARACTERS TO CHOOSE FROM
  cur = connection.cursor()
  cur.execute("SELECT ch_name, ch_level FROM character WHERE ch_id = {}".format(currentUser))
  for row in cur.fetchall():
    print(row["ch_name"] + " Lv. " + row["ch_level"] + "\n")
  cur.close()
  currentCharacter = input('Select a character to load: \n')

  #LIST ALL MODIFIABLE ATTRIBUTES OF SELECTED CHARACTER
  cur2 = connection.cursor()
  cur2.execute("SELECT * FROM character WHERE ch_id = {} and ch_name = {}".format(currentUser, currentCharacter))
  for row in cur2.fetchall():
    print(row["ch_name"] + " Lv. " + row["ch_level"]
    + "\n Strength: " + row["strength"] + "\n Dexterity: " + row["dexterity"]
    + "\n Constitution: " + row["constitution"] + "\n Charisma: " + row["charisma"]
    + "\n Intelligence: " + row["intelligence"] + "\n Wisdom: " + row["wisdom"])
  cur2.close()
  return currentCharacter

def modifyCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return

  print("Parameters: name, strength, dexterity, constitution, charisma, intelligence, wisdom. \n"
  "Please enter \'quit\' when you are finished modifying. \n")
  while True:
    n = input('Ready to modify... \n')
    if (n == 'quit'):
      break
    elif (n == 'name'):
      change = input("Enter a new name.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET ch_name = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'level'):
      change = input("Enter a new level.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET ch_level = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'strength'):
      change = input("Enter a value for STR.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET strength = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'dexterity'):
      change = input("Enter a new value for DEX.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET dexterity = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'constitution'):
      change = input("Enter a new value for CON.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET constitution = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'charisma'):
      change = input("Enter a new value for CHA.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET charisma = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'intelligence'):
      change = input("Enter a new value for INT.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET intelligence = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    elif (n == 'wisdom'):
      change = input("Enter a new value for WIS.")
      cur = connection.cursor()
      cur.execute("UPDATE character SET wisdom = {} WHERE ch_name = {} and ch_id = {}".format(change, currentCharacter, currentUser))
      cur.close()
    else:
      print("Unrecognizable command. Please try again.")

def exportCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return

  cur = connection.cursor()
  cur.execute("SELECT * FROM character WHERE ch_id = {} and ch_name = {}".format(currentUser, currentCharacter))
  row = cur.fetchone()
    
  output = row["ch_name"] + " Lv. " + row["ch_level"] + calculations.hitpoints(row["ch_class"], row["ch_level"], row["constitution"])
  + "\n Class: " + row["class"] + ", Subclass: " + row["subclass"]
  + "\n Race: " + row["race"] + ", Subrace: " + row["subrace"]
  + "\n STR: " + row["strength"] + " [" + calculations.abilityscore(row["strength"]) + "]"
  + "\n DEX: " + row["dexterity"] + " [" + calculations.abilityscore(row["dexterity"]) + "]"
  + "\n CON: " + row["constitution"] + " [" + calculations.abilityscore(row["constitution"]) + "]"
  + "\n CHA: " + row["charisma"] + " [" + calculations.abilityscore(row["charisma"]) + "]"
  + "\n INT: " + row["intelligence"] + " [" + calculations.abilityscore(row["intelligence"]) + "]"
  + "\n WIS: " + row["wisdom"] + " [" + calculations.abilityscore(row["wisdom"]) + "]"
  + "\n Background: \n" + row["background"]
  cur.close()

  # Exports character sheet as a text file
  # with open("CharacterSheet.txt", "w") as text_file:
    # print("Session Character Sheet \n \n {}".format(output), file=text_file)
  print(output)

def deleteCharacter(currentUser, currentCharacter, connection):
  # Checks if the command is called before the user has registered or logged in.
  if (currentUser == ''):
    print('Please login or register. \n')
    return

  # Checks if the command is called before the user has loaded a character
  if (currentCharacter == ''):
    print('No character has been selected. \n')
    return
    
  #DELETES CURRENT CHARACTER
  cur = connection.cursor()
  cur.execute("DELETE FROM characters WHERE ch_name = {} and ch_id = {}".format(currentCharacter, currentUser)) 
  cur.close()

def parseInput(connection):
  currentUser = ''
  currentCharacter = ''
  while True:
    n = input('Ready for input... \n')
    if (n == 'quit'):
      break
    elif (n == 'register'):
      currentUser = registerUser(connection)
    elif (n == 'login'):
      currentUser = loginUser(connection)
    elif (n == 'new character'):
      currentCharacter = createCharacter(currentUser, connection)
    elif (n == 'load character'):
      currentCharacter = loadCharacter(currentUser, connection)
    elif (n == 'modify character'):
      modifyCharacter(currentUser, currentCharacter, connection)
    elif (n == 'export character'):
      exportCharacter(currentUser, currentCharacter, connection)
    elif (n == 'delete character'):
      deleteCharacter(currentUser, currentCharacter, connection)
    else:
      print("Unrecognizable command. Please try again.")