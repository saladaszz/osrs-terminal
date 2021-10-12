from OSRSBytes import Hiscores
from OSRSBytes import Items
import argparse
import sys
from tabulate import tabulate


# In addition, all items can be called by Item ID as well
allSkillMsg = False

items=Items()


parser = argparse.ArgumentParser()

skills = [ 'attack', 'defense', 'strength', 'hitpoints', 'ranged',
			  'prayer', 'magic', 'cooking', 'woodcutting',
			  'fletching', 'fishing', 'firemaking',
			  'crafting', 'smithing', 'mining', 'herblore',
			  'agility', 'thieving', 'slayer', 'farming',
			  'runecrafting', 'hunter', 'construction' ]

displaySkills = [ 'Attack', 'Defense', 'Strength', 'Hitpoints', 'Ranged',
			  'Prayer', 'Magic', 'Cooking', 'Woodcutting',
			  'Fletching', 'Fishing', 'Firemaking',
			  'Crafting', 'Smithing', 'Mining', 'Herblore',
			  'Agility', 'Thieving', 'Slayer', 'Farming',
			  'Runecrafting', 'Hunter', 'Construction' ]

argTitles = [ 'args.attack', 'args.defense', 'args.strength', 'args.hitpoints', 'args.ranged',
			  'args.prayer', 'args.magic', 'args.cooking', 'args.woodcutting',
			  'args.fletching', 'args.fishing', 'args.firemaking',
			  'args.crafting', 'args.smithing', 'args.mining', 'args.herblore',
			  'args.agility', 'args.thieving', 'args.slayer', 'args.farming',
			  'args.runecrafting', 'args.hunter', 'args.construction' ]

adress = []




#required user argument
parser.add_argument("-user", help="Displays the levels of a player's specified skills.")
parser.add_argument("-item", help="Displays prices of specified item.")

#adds all optional arguments for skills
for x in skills:
    parser.add_argument("-" + x, help="Displays user's " + x + " skill level." , action="store_true")

args = parser.parse_args()

#sets user as username given in argument
if args.user != None:
    user = Hiscores(args.user)
chosenItem = args.item

if args.user == None and args.item == None:
    print("Use osrsbytes -h to see a list of arguments.")

if args.item != None:
    print('Sell Average:',  items.getSellAverage(chosenItem))
    print('Sell Quantity:', items.getSellQuantity(chosenItem))
    print('Buy Average:',  items.getBuyAverage(chosenItem))
    print('Buy Quantity:', items.getBuyQuantity(chosenItem))
    print('Buy Limit:',    items.getBuyLimit(chosenItem))
    print('Shop Price:',      items.getShopPrice(chosenItem))
    print('High Alch Value:', items.getHighAlchValue(chosenItem))
    print('Low Alch Value:',  items.getLowAlchValue(chosenItem))
    
for k in range(0,23):
    adress += [k]
    adress[k] = id(argTitles[k])
    
if args.attack==False and args.defense==False and args.strength==False and args.hitpoints==False and args.ranged==False and args.prayer==False and args.magic==False and args.cooking==False and args.woodcutting==False and args.fletching==False and args.fishing==False and args.firemaking==False and args.crafting==False and args.smithing==False and args.mining==False and args.herblore==False and args.agility==False and args.thieving==False and args.slayer==False and args.farming==False and args.runecrafting==False and args.hunter==False and args.construction==False:
    if args.user != None:
        table = [['Skill', 'Level'], [skills[0], user.skill(skills[0], 'level')], [skills[1], user.skill(skills[1], 'level')], [skills[2], user.skill(skills[2], 'level')], [skills[3], user.skill(skills[3], 'level')], [skills[4], user.skill(skills[4], 'level')], [skills[5], user.skill(skills[5], 'level')], [skills[6], user.skill(skills[6], 'level')], [skills[7], user.skill(skills[7], 'level')], [skills[8], user.skill(skills[8], 'level')], [skills[9], user.skill(skills[9], 'level')], [skills[10], user.skill(skills[10], 'level')], [skills[11], user.skill(skills[11], 'level')], [skills[12], user.skill(skills[12], 'level')], [skills[13], user.skill(skills[13], 'level')], [skills[14], user.skill(skills[14], 'level')], [skills[15], user.skill(skills[15], 'level')], [skills[16], user.skill(skills[16], 'level')], [skills[17], user.skill(skills[17], 'level')], [skills[18], user.skill(skills[18], 'level')], [skills[19], user.skill(skills[19], 'level')], [skills[20], user.skill(skills[20], 'level')], [skills[21], user.skill(skills[21], 'level')], [skills[22], user.skill(skills[22], 'level')]]
        print(" ")
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        print(" ")

x=0
if args.attack == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.defense == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.strength == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.hitpoints == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.ranged == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))        
x+=1

if args.prayer == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.magic == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.cooking == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.woodcutting == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.fletching == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.fishing == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.firemaking == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.crafting == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.smithing == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.mining == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.herblore == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.agility == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.thieving == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.slayer == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.farming == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.runecrafting == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.hunter == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))
x+=1

if args.construction == True:
    print("Current " + displaySkills[x] + " level:", user.skill(skills[x], 'level'))

