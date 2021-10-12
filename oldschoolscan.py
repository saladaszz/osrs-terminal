from OSRSBytes import Hiscores
from OSRSBytes import Items
import argparse
import sys
from tabulate import tabulate


allSkillMsg = False

items=Items()


parser = argparse.ArgumentParser()

#array with names of all skills
skills = [ 'attack', 'defense', 'strength', 'hitpoints', 'ranged',
			  'prayer', 'magic', 'cooking', 'woodcutting',
			  'fletching', 'fishing', 'firemaking',
			  'crafting', 'smithing', 'mining', 'herblore',
			  'agility', 'thieving', 'slayer', 'farming',
			  'runecrafting', 'hunter', 'construction' ]

#adds arguments (both optional)
parser.add_argument("-user", help="Displays the levels of a player's specified skills.")
parser.add_argument("-item", help="Displays prices of specified item.")

#adds individual arguments for each skill (if you want to display only one or a couple)
for x in skills:
    parser.add_argument("-" + x, help="Displays user's " + x + " skill level." , action="store_true")

args = parser.parse_args()

#If user argument has been given, set it as user to lookup stats
if args.user != None:
    user = Hiscores(args.user)

#sets given item from argument as item to lookup
chosenItem = args.item

#if no arguments given, print a helpful line
if args.user == None and args.item == None:
    print("Use osrsbytes -h to see a list of arguments.")

#prints item prices
if args.item != None:
    print('Sell Average:',  items.getSellAverage(chosenItem))
    print('Sell Quantity:', items.getSellQuantity(chosenItem))
    print('Buy Average:',  items.getBuyAverage(chosenItem))
    print('Buy Quantity:', items.getBuyQuantity(chosenItem))
    print('Buy Limit:',    items.getBuyLimit(chosenItem))
    print('Shop Price:',      items.getShopPrice(chosenItem))
    print('High Alch Value:', items.getHighAlchValue(chosenItem))
    print('Low Alch Value:',  items.getLowAlchValue(chosenItem))

#if all settings for user argument are false, print a table with all stats
if args.attack==False and args.defense==False and args.strength==False and args.hitpoints==False and args.ranged==False and args.prayer==False and args.magic==False and args.cooking==False and args.woodcutting==False and args.fletching==False and args.fishing==False and args.firemaking==False and args.crafting==False and args.smithing==False and args.mining==False and args.herblore==False and args.agility==False and args.thieving==False and args.slayer==False and args.farming==False and args.runecrafting==False and args.hunter==False and args.construction==False:
    if args.user != None:
        table = [['Skill', 'Level'], [skills[0].capitalize(), user.skill(skills[0], 'level')], [skills[1].capitalize(), user.skill(skills[1], 'level')], [skills[2].capitalize(), user.skill(skills[2], 'level')], [skills[3].capitalize(), user.skill(skills[3], 'level')], [skills[4].capitalize(), user.skill(skills[4], 'level')], [skills[5].capitalize(), user.skill(skills[5], 'level')], [skills[6].capitalize(), user.skill(skills[6], 'level')], [skills[7].capitalize(), user.skill(skills[7].capitalize(), 'level')], [skills[8].capitalize(), user.skill(skills[8], 'level')], [skills[9].capitalize(), user.skill(skills[9], 'level')], [skills[10].capitalize(), user.skill(skills[10], 'level')], [skills[11].capitalize(), user.skill(skills[11], 'level')], [skills[12].capitalize(), user.skill(skills[12], 'level')], [skills[13].capitalize(), user.skill(skills[13], 'level')], [skills[14].capitalize(), user.skill(skills[14], 'level')], [skills[15].capitalize(), user.skill(skills[15], 'level')], [skills[16].capitalize(), user.skill(skills[16], 'level')], [skills[17].capitalize(), user.skill(skills[17], 'level')], [skills[18].capitalize(), user.skill(skills[18], 'level')], [skills[19].capitalize(), user.skill(skills[19], 'level')], [skills[20].capitalize(), user.skill(skills[20], 'level')], [skills[21].capitalize(), user.skill(skills[21], 'level')], [skills[22].capitalize(), user.skill(skills[22], 'level')]]
        print(" ")
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        print(" ")

#check for presense of each argument and print them accordingly (really wish there was a better way to do this, but python doesn't have something like C has & [adress of operator])
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

