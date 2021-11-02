from OSRSBytes import Hiscores
from OSRSBytes import Items
import sys, random, argparse
from tabulate import tabulate
from icrawler.builtin import GoogleImageCrawler
import os



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
parser.add_argument('--morelevels',dest='moreLevels',action='store_true')

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
    print("Use -h to see a list of arguments.")

#checks if item argument was given
if args.item != None:
    from os.path import exists 
    file_exists = exists('out.txt')
    if file_exists == True:
        os.remove('out.txt') #checks if "out.txt" exists and if it does deletes it

    sys.stdout = open(os.devnull, "w") # these two lines basically "turn off" the console so it doesnt clutter with information from the crawler
    sys.stderr = open(os.devnull, "w")
    from icrawler.builtin import GoogleImageCrawler
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'images'})
    google_Crawler.crawl(keyword = chosenItem + 'osrs', max_num = 1)
    sys.stdout = sys.__stdout__ # these two lines "turn on" the console again
    sys.stderr = sys.__stderr__

    mylist = os.listdir('images')#makes a list of all the files in folder 'images'

    # Python code to convert an image to ASCII image.
    import sys, random, argparse
    import numpy as np
    import math
    from PIL import Image
     
    # gray scale level values from:
    
    # 70 levels of gray
    gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
     
    # 10 levels of gray
    gscale2 = '@%#*+=-:. '
     
    def getAverageL(image):     
        """
        Given PIL Image, return average value of grayscale value
        """
        # get image as numpy array
        im = np.array(image)
     
        # get shape
        w,h = im.shape
     
        # get average
        return np.average(im.reshape(w*h))
     
    def covertImageToAscii(fileName, cols, scale, moreLevels):
        """
        Given Image and dims (rows, cols) returns an m*n list of Images
        """
        # declare globals
        global gscale1, gscale2
     
        # open image and convert to grayscale
        image = Image.open(fileName).convert('L')
     
        # store dimensions
        W, H = image.size[0], image.size[1]     
        # compute width of tile
        w = W/cols/1
     
        # compute tile height based on aspect ratio and scale
        h = w/scale/0.8
     
        # compute number of rows
        rows = int(H/h)
     
        # check if image size is too small
        if cols > W or rows > H:
            print("Image too small for specified cols!")
            exit(0)
     
        # ascii image is a list of character strings
        aimg = []
        # generate list of dimensions
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)
     
            # correct last tile
            if j == rows-1:
                y2 = H
     
            # append an empty string
            aimg.append("")
     
            for i in range(cols):
     
                # crop image to tile
                x1 = int(i*w)
                x2 = int((i+1)*w)
     
                # correct last tile
                if i == cols-1:
                    x2 = W
     
                # crop image to extract tile
                img = image.crop((x1, y1, x2, y2))
     
                # get average luminance
                avg = int(getAverageL(img))
     
                # look up ascii char
                if moreLevels:
                    gsval = gscale1[int((avg*69)/255)]
                else:
                    gsval = gscale2[int((avg*9)/255)]
     
                # append ascii char to string
                aimg[j] += gsval
         
        # return txt image
        return aimg
     
    # main() function
    def main():
        # create parser
        descStr = "This program converts an image into ASCII art."
        parser = argparse.ArgumentParser(description=descStr)
        
        imgFile = 'images/' + mylist[0]
     
        # set output file
        outFile = 'out.txt'
     
        # set scale default as 0.43 which suits
        # a Courier font
        scale = 0.43
     
        # set cols
        cols = 80

        # convert image to ascii txt
        aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)
     
        # open file
        f = open(outFile, 'w')
     
        # write to file
        for row in aimg:
            f.write(row + '\n')
     
        # cleanup
        f.close()
     
    # call main
    if __name__ == '__main__':
        main()

    dir = 'images'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f)) #deletes all files in 'images'

    file_exists = exists('pywhatkit_dbs.txt')
    if file_exists == True:
        os.remove('pywhatkit_dbs.txt') #deletes unecessary file 'pywhatkit_dbs.txt'

    file = open("out.txt") #opens 'out.txt' for editing
    conv_string = file.read().replace("\n", " ") #make 'out.txt' into a usable string
    file.close()

    test_str = conv_string

    #gets most repeated character in string in order to remove it
    all_freq = {}
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    rep = max(all_freq, key = all_freq.get) 
    
    import fileinput
    with fileinput.FileInput('out.txt', inplace=True) as file:
        for line in file:
            print(line.replace(rep, ' '), end='') #replaces the most repeated character with a space

    f = open('out.txt', 'r')
    file_contents = f.read()
    print(' ')
    if items.getSellAverage(chosenItem) == 0:
        print("Grand Exchange Prices not available! Sorry!")
        print('Buy Limit:',    items.getBuyLimit(chosenItem))
        print('Shop Price:',    items.getShopPrice(chosenItem))
        print('High Alch Value:', items.getHighAlchValue(chosenItem))
        print('Low Alch Value:',  items.getLowAlchValue(chosenItem))
        print(file_contents) #prints the image, now converted to text
        f.close()
    else:
        print('Sell Average:',  items.getSellAverage(chosenItem)) #gets prices of item
        print('Sell Quantity:', items.getSellQuantity(chosenItem))
        print('Buy Average:',  items.getBuyAverage(chosenItem))
        print('Buy Quantity:', items.getBuyQuantity(chosenItem))
        print('Buy Limit:',    items.getBuyLimit(chosenItem))
        print('Shop Price:',    items.getShopPrice(chosenItem))
        print('High Alch Value:', items.getHighAlchValue(chosenItem))
        print('Low Alch Value:',  items.getLowAlchValue(chosenItem))
        print(file_contents) #prints the image, now converted to text
        f.close()

#if all settings for user argument are false, print a table with all stats
if args.attack==False and args.defense==False and args.strength==False and args.hitpoints==False and args.ranged==False and args.prayer==False and args.magic==False and args.cooking==False and args.woodcutting==False and args.fletching==False and args.fishing==False and args.firemaking==False and args.crafting==False and args.smithing==False and args.mining==False and args.herblore==False and args.agility==False and args.thieving==False and args.slayer==False and args.farming==False and args.runecrafting==False and args.hunter==False and args.construction==False:
    if args.user != None:
        table = [['Skill', 'Level'], [skills[0].capitalize(), user.skill(skills[0], 'level')], [skills[1].capitalize(), user.skill(skills[1], 'level')], [skills[2].capitalize(), user.skill(skills[2], 'level')], [skills[3].capitalize(), user.skill(skills[3], 'level')], [skills[4].capitalize(), user.skill(skills[4], 'level')], [skills[5].capitalize(), user.skill(skills[5], 'level')], [skills[6].capitalize(), user.skill(skills[6], 'level')], [skills[7].capitalize(), user.skill(skills[7].capitalize(), 'level')], [skills[8].capitalize(), user.skill(skills[8], 'level')], [skills[9].capitalize(), user.skill(skills[9], 'level')], [skills[10].capitalize(), user.skill(skills[10], 'level')], [skills[11].capitalize(), user.skill(skills[11], 'level')], [skills[12].capitalize(), user.skill(skills[12], 'level')], [skills[13].capitalize(), user.skill(skills[13], 'level')], [skills[14].capitalize(), user.skill(skills[14], 'level')], [skills[15].capitalize(), user.skill(skills[15], 'level')], [skills[16].capitalize(), user.skill(skills[16], 'level')], [skills[17].capitalize(), user.skill(skills[17], 'level')], [skills[18].capitalize(), user.skill(skills[18], 'level')], [skills[19].capitalize(), user.skill(skills[19], 'level')], [skills[20].capitalize(), user.skill(skills[20], 'level')], [skills[21].capitalize(), user.skill(skills[21], 'level')], [skills[22].capitalize(), user.skill(skills[22], 'level')]]
        print(" ")
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        print(" ")

#check for presence of each argument and print them accordingly (really wish there was a better way to do this, but python doesn't have something like C has & [adress of operator])
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
