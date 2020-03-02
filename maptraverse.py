from player import Player
import time 

player=Player('testuser', 0)
player.init()



traversalPath = []
#-----------
copy={}
rooms={}
reverse=[]
#-----------
while len(copy) < 500:
  print("----------------------COPY------------------------------------", copy)
  print("----------------------ROOMS------------------------------------", rooms)
  print("----------------------Current room in while loop----------------", player.currentRoom)
  print("-------------------------COPY LENGTH-------------------------------", len(copy))
  curCooldown=player.currentRoom['cooldown']
  time.sleep(curCooldown)
  if len(player.currentRoom['items']) > 0 and player.info['items'] < 10:
    player.take()
    time.sleep(8)
  time.sleep(2)
  player.status()
  time.sleep(2)
  curRoom=player.currentRoom['room_id']
  if curRoom not in copy:
    copy[curRoom]=curRoom 
    curExits={}
  
    for exit in player.currentRoom['exits']:
      curExits[exit]="unknown"

    copy[curRoom]=curExits
  
  curExits=copy[curRoom]

  if curRoom not in rooms:
      rooms[curRoom]=curRoom
      roomObj=player.currentRoom
      rooms[curRoom]=roomObj

  if "Shop" in player.currentRoom['title'] and player.info['encumbrance'] > 0:
    player.sell()

  if "Changer" in player.currentRoom['title'] and player.info['gold'] >= 1000: 
    player.name_change()

  if player.name == "[Jon-Solari]" and player.currentRoom['title'] == "Wishing Well":
    player.examine()
    break

  # if player.status['bodywear'] > 0:
  #   player.wear_clothes()

  # if player.status['footwear'] > 0:
  #   player.wear_shoes()

  if 'n' in copy[curRoom] and curExits['n'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['n']=='unknown':
      time.sleep(curCooldown)
      player.travel("n")
      traversalPath.append("n")
      newRoom=player.currentRoom['room_id']
      curExits['n']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['s']=curRoom
      reverse.append('s')

  elif 's' in copy[curRoom] and curExits['s'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['s']=='unknown':
      time.sleep(curCooldown)
      player.travel("s")
      traversalPath.append("s")
      newRoom=player.currentRoom['room_id']
      curExits['s']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['n']=curRoom
      reverse.append('n')

  elif 'e' in copy[curRoom] and curExits['e'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['e']=='unknown':
      time.sleep(curCooldown)
      player.travel("e")
      traversalPath.append("e")
      newRoom=player.currentRoom['room_id']
      curExits['e']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['w']=curRoom
      reverse.append('w')

  elif 'w' in copy[curRoom] and curExits['w'] == 'unknown':
    print(copy[curRoom], "Currently")
    if curExits['w']=='unknown':
      time.sleep(curCooldown)
      player.travel("w")
      traversalPath.append("w")
      newRoom=player.currentRoom['room_id']
      curExits['w']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['e']=curRoom
      reverse.append('e')

  else: 
    reversal=reverse.pop()
    time.sleep(curCooldown)
    player.travel(reversal)
    traversalPath.append(reversal)
