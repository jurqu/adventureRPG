#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Sun Room',
                  'item'  : 'key'
                },

            'Sun Room':{
                  'east'  : 'Hall',
            },

            

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  # sunroom contains a secret item
  if currentRoom == 'Sun Room' and 'key' in inventory:
    book_prompt = input("You see a bookcase in the room, would you like to take a book?: yes or no: ")
    if book_prompt == 'yes' :
        key_prompt = input("You remove a dusty book and notice it has a lock on it. Would you like to insert a key?: yes or no: ")
        if key_prompt == 'yes':
          print("You insert the key and remove the lock. You open the book and notice it was really a small safe with a Glock inside, which you take. ")
          inventory.append('Glock')
          inventory.remove('key')
    elif book_prompt == "no":
      print("You left the bookcase alone.")



  ## Define how a player can win
  if currentRoom == 'Garden' and 'coin pouch' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

 ## Player can defeat the monster if hes the magic Glock and retrieve the coin pouch
  if currentRoom == 'Kitchen' and 'Glock' in inventory:
    print("You yelled at the monster to stop resisting then shot 16 rounds into it. Safe to assume the monster is dead.")
    coin_input = input("You notice a coin pouch on the monster. Take it?: yes or no?: ")
    if coin_input == 'yes':
        print("You took the coin pouch from the dead monster.")
        inventory.append('Coin pouch')
        inventory.remove('Glock')
    elif coin_input == 'no':
      print("You decide to not go near the dead monster.")
      
   ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break

