import array
import math

toons = 0
boss = 0
suit = 0
print ("Welcome! Enter the number of Toons.")
toonstring = str(input()) #number of toons entering
if not toonstring.isnumeric():
    print("Invalid number of Toons detected! Setting to default value of 4.") #invalid input string for toons, defaults to 4
    toons = 4
else:
    toons = int(toonstring)

if not toons in range (1, 9):
    print("Invalid number of Toons detected! Setting to default value of 4.") #invalid integer for toons, defaults to 4
    toons = 4
    
print("\nWhat boss are you facing? (1 for VP, 2 for CFO, 3 for CLO, 4 for CEO)")
bossstring = str(input()) #boss selection
if not bossstring.isnumeric():
    print("Invalid boss entry detected! Setting to default value of 1 (VP).") #invalid input string for boss, defaults to vp
    boss = 1
else:
    boss = int(bossstring)

if not boss in range (1, 5):
    print("Invalid boss entry detected! Setting to default value of 1 (VP).") #invalid integer for boss, defaults to vp
    boss = 1
    
            
print("\nSUIT VALUE GUIDE: Tier 1 = 1, Tier 2 = 2, ... Tier 8 = 8")
print ("Please enter suit values for each Toon.")

suitarray=array.array('i') #used to store suit values for all toons
total = 0
for i in range (0, toons):
    suitstring = str(input())
    if suitstring.isnumeric():
        suit = int(suitstring)
    else: #invalid string, sets to default value of 8 
        print("Invalid suit value detected! Setting to default value of 8.")
        suit = 8
        suitarray.append(suit)
    if suit in range (1, 9):
        suitarray.append(suit) #entering suit values into array
        print("Entered.")
    else: #invalid value, sets to default value of 8 
        print("Invalid suit value detected! Setting to default value of 8.")
        suit = 8
        suitarray.append(suit)
for i in range (0,toons):
  total += suitarray[i] #used for total combined suit values
average = total/toons
rounded = math.ceil(total/toons)

if boss == 1: #VP
    print ("\nVP difficulty/reward: \nTier 1 (1 SOS card, Cogs up to Level 11, 60 Pies): 1-3 \nTier 2 (2 SOS cards, Cogs up to Level 12, 45 Pies): 4-6 \nTier 3 (3 SOS Cards, Cogs up to Level 13, 30 pies): 7-8")
if boss == 2: #CFO
    print ("\nCFO difficulty/reward: \nTier 1 (1 Unite, Cogs up to Level 13, 500HP): 1-3 \nTier 2 (2 Unites, Cogs up to Level 14, 100HP): 4-6 \nTier 3 (3 Unites, Cogs up to Level 15, 1500HP): 7-8")
if boss == 3: #CLO
    print ("\nCLO difficulty/reward: \nTier 1 (4 C&D, Cogs up to Level 15, 40 sound gags, Level 8 max in final round, 1000HP): 1-3 \nTier 2 (6 C&D, Cogs up to Level 16, 35 sound gags, Level 9 max in final round, 1250HP): 4-6 \nTier 3 (8 C&D, Cogs up to Level 17, 30 sound gags, Level 10 max in final round, 1500HP): 7-8")
if boss == 4: #CEO
    print("\nCEO difficulty/reward: \nTier 1 (5 fires, Cogs up to Level 17 in first round, Level 10 v2.0 Tier 6 Cogs in feeding round, 600HP): 1-3 \nTier 2 (7 fires, Cogs up to Level 18 in first round, Level 12 v2.0 Tier 7 Cogs in feeding round, 800HP): 4-6 \nTier 3 (9 fires, Cogs up to Level 19 in first round, Level 14 v2.0 Tier 8 Cogs in feeding round, 1000HP): 7-8")
print("\nSuit average:", average) #average before rounding
print ("Rounded average:", rounded) #prints average rounded, this is used for boss tiers 
if rounded < 4:
    print ("Tier: 1")
elif rounded < 7:
    print("Tier: 2")
elif rounded > 6:
    print("Tier: 3")
print("\nNote that suit average will round up if there is a decimal value (i.e. average of 5.1 will become 6). Rounded average is used to determine tier.")