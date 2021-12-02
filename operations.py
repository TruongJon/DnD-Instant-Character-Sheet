#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Create a random number to be used as a userID, compare it to an existing userID table on the database 
# to make sure no number is reused
def registerUser(connection):
  username = input('Please enter a username \n')
  currentUser = ''
  cur = connection.cursor()
  cur.execute("") #SELECT STATEMENT - FILL IN USER TABLE USING USERNAME VALUE
  #currentUser = key
  cur.close()
  return currentUser

def loginUser(connection):
  username = input('Welcome back! Please enter your username \n')
  currentUser = ''
  cur = connection.cursor()
  cur.execute("") #SELECT STATEMENT - CHECK CREDENTIALS
  #currentUser = key
  cur.close()
  return currentUser

def createCharacter(currentUser, connection):
  if (currentUser == ''):
    print('Please login or register. \n')
    return
  currentCharacter = input('Enter a name for your character: \n')
  char_race = input('Select a race: \n Dwarf / Elf / Halfling / Human / Dragonborn'
  ' / Gnome / Half-Elf / Half-Orc / Tiefling / ')
  char_subrace = input('Select a subrace: \n')
  char_class = input('Select a class: \n ')
  char_sub_class = input('Select a subclass: \n')
  print('Write a background for your character (ctrl + d upon finish): ')
  char_background = sys.stdin.read()
  char_level = input('Starting level of your character \n Lv. ')
  print('Add your proficiencies (ctrl + d upon finish): ')
  char_proficiency = sys.stdin.read()
  cur = connection.cursor()
  cur.execute("") #SELECT STATEMENT - FILL IN TABLES WITH APPROPRIATE INFORMATION
  cur.close()
  return currentCharacter

def loadCharacter(currentUser, connection):
  if (currentUser == ''):
    print('Please login or register. \n')
    return
  cur = connection.cursor()
  cur.execute("") #SELECT STATEMENT - LIST ALL CHARACTER NAMES
  for row in cur.fetchall():
    print(row)
  cur.close()
  currentCharacter = input('Select a character to load: \n')
  cur2 = connection.cursor()
  cur2.execute("") #SELECT STATEMENT - LIST ALL CHARACTER ATTRIBUTES
  for row in cur2.fetchall():
    print(row)
  cur2.close()
  return currentCharacter

def modifyCharacter(currentUser, currentCharacter, connection):
  if (currentUser == ''):
    print('Please login or register. \n')
    return

def exportCharacter(currentUser, currentCharacter, connection):
  if (currentUser == ''):
    print('Please login or register. \n')
    return
  cur = connection.cursor()
  cur.execute("") #SELECT STATEMENT - LIST ALL CHARACTER ATTRIBUTES
  for row in cur.fetchall():
    print(row)
  cur.close()

def deleteCharacter(currentUser, currentCharacter, connection):
  if (currentUser == ''):
    print('Please login or register. \n')
    return
  cur = connection.cursor()
  cur.execute("") #DELETE STATEMENT
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