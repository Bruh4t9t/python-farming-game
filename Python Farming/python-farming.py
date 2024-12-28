# Game variables
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
}

seed_list = ['LET', 'POT', 'CAU']
seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}


position = [ [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, 'X', None, None],
         [None, None, None, None, None],
         [None, None, None, None, None] ]
plant_list = [[None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None]  ]
time_list = [[None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, None, None, None]  ]
# Even though 3 lists is inefficient it is easier to manipulate 

#-----------------------------------------------------------------------
# in_town(game_vars)
#
#    Shows the menu of Albatross Town and returns the player's choice
#    Players can
#      1) Visit the shop to buy seeds
#      2) Visit the farm to plant seeds and harvest crops
#      3) End the day, resetting Energy to 10 and allowing crops to grow
#
#      9) Save the game to file
#      0) Exit the game (without saving)
#-----------------------------------------------------------------------
def in_town(game_vars):
    print("+--------------------------------------------------+")
    print("| Day {:<2}          Energy: {:<2}         Money: ${:<6}|".format(game_vars["day"],game_vars["energy"],game_vars["money"])) 
    # Prints the day number, energy and money
    if len(game_vars["bag"]) == 0:
        print("| {:<49}|".format("You have no seeds")) # Print You have no  seeds if bag is empty
    else:
        for key,value in game_vars["bag"].items():
                print("|      {:<16}{:<28}|".format(("{:}:".format(key)),value)) # Prints the seed that the player has as well as the quantity they have
            
    print("+--------------------------------------------------+")
    print("1} Visit the shop to buy seeds")
    print("2) Visit the farm to plant seeds and harvest crops")
    print("3) End the day, resetting Energy to 10 and allowing crops to grow")
    print()
    print("9) Save the game to file")
    print("0) Exit the game (without saving)")
    print("-------------------")
    choice = input("Your choice?")
    while choice not in ["1","2","3","9","0"]:# validates whether the choice is 1,2,3,9 or 0 else requires them to input again
        print("Invalid Input")
        choice = input("Your choice? ")
    return choice # Returns choice
#---------------------------------------------------------------------
# in_shop(game_vars)
#
#    Shows the menu of the seed shop, and allows players to buy seeds
#    Seeds can be bought if player has enough money
#    Ends when player selects to leave the shop
#----------------------------------------------------------------------
def in_shop(game_vars):
    shopchoice = ""
    print("Welcome to Pierce's Seed Shop!")
    while shopchoice != 0:# While the choice in the shop is not 0
        
        
        print("+--------------------------------------------------+")
        print("| Day {:<2}          Energy: {:<2}         Money: ${:<6}|".format(game_vars["day"],game_vars["energy"],game_vars["money"]))# Prints the day number, energy and money
        if len(game_vars["bag"]) == 0:
            print("| {:<49}|".format("You have no seeds"))# Print You have no  seeds if bag is empty
        else:
            for key,value in game_vars["bag"].items():# iterates thorugh the game_vars["bag"] dictionary to output the key and value of the dictionary
                print("|      {:<16}{:<28}|".format(("{:}:".format(key)),value))# Prints the seed that the player has as well as the quantity they have
            
                
        print("+--------------------------------------------------+")
        print("What do you wish to buy")
        print("{:<20}{:<10}{:<15}{:<10}".format("Seed","Price","Days to Grow","Crop Price"))
        print("--------------------------------------------------------")
        for i in range(len(seeds)):
            print("{}) {:<19}{:<12}{:<15}{:<10}".format(i+1,seeds[seed_list[i]]["name"],seeds[seed_list[i]]["price"],seeds[seed_list[i]]["growth_time"],seeds[seed_list[i]]["crop_price"]))# Prints the seeds name, their price, growth time as well as how much they sell for
        print()
        print("0) Leave")
        print("--------------------------------------------------------")
        total = 0
        for key,value in game_vars["bag"].items():# iterates throught the game_vars["bag"] to find the number of seeds the player has
            total += value
        
        if total < 10:# Calculates whether the player has more than 10 seeds and if they do then the program doesnt allow them to buy more seeds
            
            shopchoice = int(input("Your Choice? "))# Takes input for the choice of which seed the player want to buy
            if shopchoice == 0:# Exits the shop menu and goes back to the town menu
                break
            seed_length = []# List where number of seeds are inputted one in a numberical order, e.g. if there are 2 seeds, then the only shopchoice options would be 1 and 2 hence the seed_length list would be ["1","2"], in this case there are 3 choice for the seeds hence the list would be ["1","2","3"]
            for i in range(len(seed_list)):# iterates through seed_list to how may seeds there are
                seed_length += str(i+1)# updates the list based on the number of seeds
            while str(shopchoice) not in seed_length: # If the input given is not within the options given, e.g. 1, 2 or 3 then it tells them that it is an invalid input
                print("Invalid Input")
                shopchoice = int(input("Your Choice? "))

                
                    
            print("You have ${}".format(game_vars["money"]))
            buy = input("How many do you wish to buy?")# Takes input of how many seeds player wants to buy
            while str(buy).isdigit() == False:# If buy is not a integer then it would 
                print("Invalid Input")
                buy = input("How many do you wish to buy?")
            while int(buy) + total > 10:# If input plus the calculated total is greater than 10 then the user cannot buy the seeds
                print("You cant buy that many seeds")
                buy = input("How many do you wish to buy?")
            if buy == "0":# If they input 0 then the loops breaks
                break
            if seeds[seed_list[shopchoice-1]]["name"] in game_vars["bag"] and (seeds[seed_list[shopchoice-1]]["price"] * int(buy)) <= game_vars["money"]:# Checks whether players has enough money to pay for the seeds and if the seed is already in the bag
                print("You bought {} {} seeds".format(int(buy),seeds[seed_list[shopchoice-1]]["name"]))# Outputs which seed the player bought and how many
                game_vars["money"] = game_vars["money"] - (seeds[seed_list[shopchoice-1]]["price"] * int(buy)) # Minuses money that was used to pay for the seeds
                game_vars["bag"][seeds[seed_list[shopchoice-1]]["name"]] += int(buy)  # Adds number of seeds bought to the seed name in the bag
            
            elif (seeds[seed_list[shopchoice-1]]["price"] * int(buy)) <= game_vars["money"]:# Runs is the seed name in not in the bag
                print("You bought {} {} seeds".format(int(buy),seeds[seed_list[shopchoice-1]]["name"]))#  Outputs which seed the player bought and how many
                game_vars["money"] = game_vars["money"] - (seeds[seed_list[shopchoice-1]]["price"] * int(buy))# Minuses money that was used to pay for the seeds
                game_vars["bag"][seeds[seed_list[shopchoice-1]]["name"]] = int(buy) # Adds seed name and amount bought into game_vars["bag"]
            else:# Happens if players doesnt have enought money to buy the seeds spcified
                print("You can't afford that!")
        else:# Runs if player already has 10 seeds in the bag
            print("You have too many seeds")
            break


    
#---------------------------------------------------------------------
# draw_farm(farmer_row, farmer_col)
#
#    Draws the farm
#    Each space on the farm has 3 rows:
#      TOP ROW:
#        - If a seed is planted there, shows the crop's abbreviation
#        - If it is the house at (2,2), shows 'HSE'
#        - Blank otherwise
#      MIDDLE ROW:
#        - If the player is there, shows X
#        - Blank otherwise
#      BOTTOM ROW:
#        - If a seed is planted there, shows the number of turns before
#          it can be harvested
#        - Blank otherwise
#----------------------------------------------------------------------
def draw_farm(farmer_row, farmer_col):
    
    for i in range(farmer_row):# Prints map
        print("+-----+-----+-----+-----+-----+")
        for r in range(farmer_row):# First loop which prints top row
            if i == 2 and r == 2:# If the cursor is the middle, then it prints "| HSE "
                print("| HSE ",end="")
            elif plant_list[i][r] == "LET" or plant_list[i][r] == "POT" or plant_list[i][r] == "CAU":# If there is a plant at that position on the list then it prints the plant instead of a space
                print("| {} ".format(plant_list[i][r]),end="")
                
            else:
                print("|     ",end="")
        print("|")

        for g in range(farmer_row):# Second loop which prints middle row
            if position[i][g] == "X":# If X is at a specific position then it prints X instead of an empty space
                print("|  X  ",end="")
            else: 
                print("|     ",end="")
        print("|")
        
        for f in range(farmer_row):# Last loop which prints Bottom row
            if time_list[i][f] is None:
                print("|     ",end="")
            else:
                print("|  {}  ".format(time_list[i][f]),end="")# Prints the days left for a plant to mature if there is a plant at that specific postion
            
        print("|")
    print("+-----+-----+-----+-----+-----+")
#----------------------------------------------------------------------
# in_farm(game_vars))
#
#    Handles the actions on the farm. Player starts at (2,2), at the
#      farmhouse.
#
#    Possible actions:
#    W, A, S, D - Moves the player
#      - Will show error message if attempting to move off the edge
#      - If move is successful, Energy is reduced by 1
#
#    P - Plant a crop
#      - Option will only appear if on an empty space
#      - Shows error message if there are no seeds in the bag
#      - If successful, Energy is reduced by 1
#
#    H - Harvests a crop
#      - Option will only appear if crop can be harvested, i.e., turns
#        left to grow is 0
#      - Option shows the money gained after harvesting
#      - If successful, Energy is reduced by 1
#
#    R - Return to town
#      - Does not cost energy
#----------------------------------------------------------------------
def in_farm(game_vars):
    days_to_grow = []# List that stores the days a plant takes to grow
    crop_price = []# List that stores the crop price of the plants planted
    seed_plant_list = []# List that stores the plants planted
    directionchoice = ""
    while game_vars["energy"]+1 > 0:# Runs while energy is not 0
        print("Energy: {}".format(game_vars["energy"]))# Prints energy
        print("[WASD] Move")
        print("P)lant seed ") 
        index_now,j = find_x() # Finds current position of X              
        if time_list[index_now][j] == "0":
            print("H) Harvest {} for ${}".format(seeds[plant_list[index_now][j]]["name"],seeds[plant_list[index_now][j]]["crop_price"])) # If plant is ready to harvest then this will be printed
        print("R)eturn to Town ")

        directionchoice = input("\nEnter your choice of direction: ")# Takes input of what the user want to do on the farm
        while directionchoice.upper() not in ["R","W","A","S","D","P","H","B"]:# Check whether the inputted directionchoice is within "R","W","A","S","D","P","H","B"
            print("Invalid Input")
            directionchoice = input("\nEnter your choice of direction: ")# Allows player to input option again
        if directionchoice.upper() == "R":# If the choice is R then it will return back to main menu
            index_now,j = find_x()
            position[index_now][j] = None
            position[2][2] = "X"# Resets X back to House with this line and above line
            
            break
        for i in range(len(position)):
            
            if directionchoice.upper() == "S" and "X" not in position[-1]:# Checks whether X is not in the bottom list of the postion list 
                for r in range(len(position[i])):
                    if position[r][i] == "X":
                        position[r][i] = None # Makes X move down by replacing the list position directly below X to X and the current postion of X gets set to None
                        position[r+1][i] = "X"
                        break
            elif directionchoice.upper() == "W" and "X" not in position[0]:# Checks whether X is not in the top list of the postion list 
                for r in range(len(position[i])):
                    if position[i][r] == "X":
                        position[i][r] = None # Makes X move up by replacing the list position directly above X to X and the current postion of X gets set to None
                        position[i-1][r] = "X"
                        break
            elif directionchoice.upper() == "A" and position[i][0] != "X":# Checks whether X is not in the most left part of the postion list 
                for r in range(len(position[i])):
                    if position[r][i] == "X":
                        position[r][i] = None # Makes X move left by replacing the list position left of X to X and the current postion of X gets set to None
                        position[r][i-1] = "X"
                        break
            elif directionchoice.upper() == "D" and position[i][-1] != "X":# Checks whether X is not in the most right part of the postion list 
                for r in range(len(position[i])):
                    if position[i][r] == "X":
                        position[i][r] = None # Makes X move right by replacing the list position directly right of X to X and the current postion of X gets set to None
                        position[i][r+1] = "X"
                        
                        break
            elif directionchoice.upper() == "P":
                planted = False # boolean for checking whether there is a plant at that postion already
                if planted == False:
                    for r in range(len(position)):
                        for g in range(len(position[i])):
                            if position[r][g] == "X" and plant_list[r][g] != None:# Checks whether there is a plant at that postion
                                print("You cannot plant here")
                                planted = True
                            if position[r][g] == "X" and r == 2 and g == 2:# Check whether the player postion is at the house
                                print("You cannot plant here")
                                planted = True
                            else:
                                if position[r][g] == "X":
                                    positionx = r
                                    positiony = g
                if planted == True:# If there is a plant or the postion of X is at the House then it breaks the loop
                    break
                if planted == False:
                    print("What do you wish to plant?")
                    print("-----------------------------------------------------")
                    print("{:15}{:15}{:15}{:15}".format("Seed","Days to grow","Crop price","Available"))
                    print("-----------------------------------------------------")
                    if len(game_vars["bag"]) !=  0:
                        for index,(seed,avaliable) in enumerate(game_vars["bag"].items()):# iterates through game_vars["bag"] as long as it length is not 0
                            
                            if seed not in seed_plant_list:
                                seed_plant_list.append(seed)# Adds the seed to the seed_plant_list if  it is inside the bag
                                
                            
                                for i in range(len(seed_list)):
                                    if seeds[seed_list[i]]["name"] == seed:
                                        days_to_grow += str(seeds[seed_list[i]]["growth_time"])# Also adds the days that it takes for the plant to mature if the plant is in the seeds_plant_list
                                        crop_price += str(seeds[seed_list[i]]["crop_price"])# Also adds the price the plant would sell for if the plant is in the seeds_plant_list
                            print("{}){:<17}{:<15}{:<15}{:<15}".format(index+1,seed_plant_list[index],days_to_grow[index],crop_price[index],avaliable)) # prints the seed name, the days it takes to grow as well as the selling price of the plant if they are in the bag as well as how many seeds are in the bag by seed name
                        plantchoice = int(input("Enter the number of the plant you want to plant: "))# Takes input on the number of the plant that the player want to plant
                        plant_list_lenght = []# List to track how many seeds are in the bag andd then makes a list of it in numerical order, e.g. if the player bought 2 seeds the list would be ["1","2"]
                        for i in range(len(game_vars["bag"])):# iterates through game_vars["bag"] and adds the number to plant_list_length
                            plant_list_lenght += str(i+1)
                        while str(plantchoice) not in plant_list_lenght:# Check if the input is within plant_list length and if not then it ask the player to input their choice again
                            print("Invalid Input")
                            plantchoice = int(input("Enter the number of the plant you want to plant: "))
                        game_vars["bag"][seed_plant_list[plantchoice-1]] -= 1 # Reduces the number of seeds for the paticular seed planted by 1
                        for i in range(len(seed_list)):
                            if len(game_vars["bag"]) == 0:# if there is no seeds in the dictionary then the loop breaks
                                break
                            if seeds[seed_list[i]]["name"] == seed_plant_list[plantchoice-1]:#Checks plant name with the seeds list 
                                
                                plant_list[positionx][positiony] = str(seed_list[i]) # the postion where X is in the plant_list changes from None to the plant planted
                                
                                time_list[positionx][positiony] = str(days_to_grow[plantchoice-1]) # the postion where X is in the time_list changes from None to the days left for the plant to mature
                                
                                break
                        for r in range(len(seed_list)):
                            if seeds[seed_list[r]]["name"] == seed_plant_list[plantchoice-1]:
                                if game_vars["bag"][seeds[seed_list[r]]["name"]] == 0:# Only runs if there are no more seeds available    
                                    index_seed = seed_plant_list.index(seeds[seed_list[r]]["name"])
                                    seed_plant_list.remove(seeds[seed_list[r]]["name"])# removes the seed from the seed_plant_list
                                    days_to_grow.pop(index_seed)# removes the days to grow elemtent from the list if the seed was removed from the seed_plant_list
                                    crop_price.pop(index_seed)# removes the crop price elemtent from the list if the seed was removed from the seed_plant_list
                                    game_vars["bag"].pop(seeds[seed_list[r]]["name"])# Removes seed from game_vars["bag"] if there is no more availble
                                break
                        break
                    else:
                        print("You have no seeds")
                        break
            elif directionchoice.upper() == "H":# Runs if the player want to harvest a plant
                    index_now,j = find_x()
                    
                    if time_list[index_now][j] is None:
                        print("You have no plant here")
                        break
                    # Code above finds postion of X with index_now and j to see whether a plant is in the postion in the first place
                    elif time_list[index_now][j] != "0":# If the days to grow is not 0 then this will execute
                    
                        print("Your Plant is not ready to be harvested")
                        break
                    else: # Harvest the plant and tells player how much they earned from harvesting the plant
                        print("You Harvested the {} and sold it for ${}!".format(seeds[plant_list[index_now][j]]["name"],seeds[plant_list[index_now][j]]["crop_price"]))
                        game_vars["money"] += seeds[plant_list[index_now][j]]["crop_price"]# Increases the players money by the crop price of the crop hervested
                        print("You now have ${}!".format(game_vars["money"]))

                        plant_list[index_now][j] = None # Removes the plant from the plant_list
                        time_list[index_now][j] = None # Removes the days that the plant takes to grow from the time_list
                        break
            elif directionchoice.upper() == "B":# If players wants to harvest using the giant crops method
                    index_now,j = find_x()
                    # Resets X back to House with this line and above line
                        # Above code finds postion of X with index_now and j
                    if index_now == 4 or j == 4:
                        print("Unable to perform giant harvest")
                        break
                    # If positon of player is at the bottom row or most left rom then they cannot perform giant harvest
                    if time_list[index_now][j] is None:
                        print("You have no plant here")
                        break
                    elif time_list[index_now][j] == time_list[index_now+1][j] and time_list[index_now][j] == time_list[index_now][j+1] and time_list[index_now][j] == time_list[index_now+1][j+1] and plant_list[index_now][j] == plant_list[index_now+1][j] and plant_list[index_now][j] == plant_list[index_now][j+1] and plant_list[index_now][j] == plant_list[index_now+1][j+1] and time_list[index_now][j] == "0":
                        game_vars["money"] += (seeds[plant_list[index_now][j]]["crop_price"] * 4)
                        # Checks whether plants in the 2x2 grid are of same type and all have 0 days left to mature
                        print("Giant Harvest performed")

                        plant_list[index_now][j] = None
                        time_list[index_now][j] = None
                        plant_list[index_now+1][j] = None
                        time_list[index_now+1][j] = None 
                        plant_list[index_now][j+1] = None
                        time_list[index_now][j+1] = None 
                        plant_list[index_now+1][j+1] = None
                        time_list[index_now+1][j+1] = None
                        break      
                        # Above code ensures that from where the plants were harvested were all switched to None as well as the elements in the time_list
                    else:
                        print("Unable to perform giant harvest")
                    
            #elif directionchoice in ["W","A","S","D"]:# If the player selected one of the direction choice that would move them off the gird then this line runs
                #print("You cant move here")
                #break
        game_vars["energy"] -= 1# reduces player energy by 1
        draw_farm(5,5)  # performs draw_farm 
        if game_vars["energy"] == 0:# runs if player's energy is 0
            
            index_now,j = find_x()
            position[index_now][j] = None
            position[2][2] = "X"# Resets X back to House with this line and above line
                    # Above code finds postion of X and sets it back to the postion of House
            print("You're too tired. You should get back to town. ")
            break
        
    pass

#----------------------------------------------------------------------
# end_day(game_vars)
#
#    Ends the day
#      - The day number increases by 1
#      - Energy is reset to 10
#      - Every planted crop has their growth time reduced by 1, to a
#        minimum of 0
#----------------------------------------------------------------------
def end_day(game_vars):
    game_vars["day"] += 1# Adds 1 the days
    
    game_vars["energy"] = 10 # resets energy to 10
    for i in range(len(time_list)):
        for r in range(len(time_list)):
            if time_list[i][r] is not None:# Runs if there is a number in the time_list
                if int(time_list[i][r]) > 0:
                    time_list[i][r] = str(int(time_list[i][r]) - 1)# minuses the days to mature by 1 only if it is above 0
    if game_vars["day"] > 20 and game_vars["money"] < 100:# If player reaches day 20 with less than a 100 dollars then this runs
        
        return "loss"
    elif game_vars["day"] > 20 and game_vars["money"] >= 100:# If player reaches day 20 with more than or equal 100 dollars then this runs
        print("You have ${} after 20 days".format(game_vars["money"]))
        print("You paid off your debt of $100 and made a profit of ${}".format(game_vars["money"]-100)) 
        return "win"
#----------------------------------------------------------------------
# save_file(game_vars, method)
#
#    Saves the game into the file "savegame.txt"
#----------------------------------------------------------------------
def save_file(listneeded,method):
    with open("savegame.txt",method) as gamefile:# opens the file savegame.txt where method decides whether to append or write
        for px in range(len(listneeded)):# iterates throught the inputted list
            
            for py in range(len(listneeded)):
                if listneeded[px][py] is None:
                    gamefile.write("None,")# write None to file if the position is not filled by anything
                else:
                    gamefile.write(listneeded[px][py] + ",")# else writes the element at that postion to the file
        gamefile.write("\n")
        
    pass

def save_game(game_vars,method):
    with open("savegame.txt",method) as gamefile:# opens the file savegame.txt where method decides whether to append or write
        
        for i in game_vars:
            if i == "bag":
                for key,value in game_vars["bag"].items():
                    gamefile.write("{},{}".format(key,value))# If i is at bag then the gamefile writes both the key and value
                    gamefile.write("\n")
                    
            else:
                gamefile.write(str(game_vars[i]))# writes the elements of game_vars to savegame.txt
                gamefile.write("\n")



#----------------------------------------------------------------------
# load_game(game_vars, listneeded,line)
#
#    Loads the saved game by reading the file "savegame.txt"
#----------------------------------------------------------------------
def load_game(game_vars,listneeded,line):
    with open("C:\\Users\\pg200\\Downloads\\savegame.txt","r") as gamefile:# opens savegame.txt in the reading mode
        info = gamefile.readlines()
        for i in range(2):
            info[i] = info[i].strip().split(",")# takes the 2 lists in the savegame.txt file 
        
        info[line].pop()
        bagtemp = []# temporary list for storing components in the bag
        game_vars["day"] = int(info[2].strip())# saves day into game_var["day"]
        game_vars["energy"] = int(info[3].strip())# saves energy into game_var["day"]
        game_vars["money"] = int(info[4].strip())# saves money into game_var["day"]
        for i in range(5,len(info)):
            bagtemp += [info[i].strip().split(",")]
        
        for i in range(len(bagtemp)):
            game_vars["bag"][bagtemp[i][0]] = int(bagtemp[i][1])
            #sets the name of the seed in the file to the amount of seeds in it from the file

        temp = []# temporary file to store components of the list in fives
        
        for i in range(0,25,5):
            temp.append([info[line][i],info[line][i+1],info[line][i+2],info[line][i+3],info[line][i+4]])# appens the temporary list with 5 elements in the file
        
        for g in range(len(temp)):
            for r in range(len(temp[g])):
                if temp[g][r] == "None":
                    listneeded[g][r] = None # if the temporary file has None in it then the list inputted has the value None at that specific postion
                else:
                    listneeded[g][r] = temp[g][r] #Else if the temporary file has something besides None then that is saves at the specific postion
    pass

#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------

print("----------------------------------------------------------")
print("Welcome to Sundrop Farm!")
print()
print("You took out a loan to buy a small farm in Albatross Town.")
print("You have 20 days to pay off your debt of $100.")
print("You might even be able to make a little profit.")
print("How successful will you be?")
print("----------------------------------------------------------")
print("1) Start a new game")
print("2) Load your saved game")
print()
print("0) Exit Game")
choice = input("Your Choice? ")
# Write your main game loop here
def loop_flow(twochoice):# function for the game loop
    if twochoice == "1":# If 1 is chosen in_shop performs
        in_shop(game_vars)
    elif twochoice == "2":# If 2 is chosen draw_farm and in_farm performs
        draw_farm(5,5)
        in_farm(game_vars)
        
    elif twochoice == "3":# If 3 is chosen end_day performs
        check = end_day(game_vars)
        if check == "loss":
            print("You lose as you did not pay back you loan of $100 in time")
            return "end"
        elif check == "win":
            return "end"
        
        
    elif twochoice == "9":# If 9 is chosen then the game is saved
        save_file(time_list,"w")# List is specified for each of the functions
        save_file(plant_list,"a")
        save_game(game_vars,"a")
        print("Game Saved.")
    elif twochoice == "0":# If 0 is chosen then player exits game
        print("Goodbye!")
def find_x():#finds position of X
    for i in range(len(position)):# Loop that check where the player is currently
        j = 0
        index_now = 0
        if "X" in position[i]:
            j = position[i].index("X") # Finds position of the of "X" inside postion[index_now]
            if position[i][j] == "X":
                index_now = i # finds postion of the list "X" is in in the list position
                return index_now,j

loaded = True # specifies whether game has been loaded or not
while choice not in ["0","1","2"]:# If choice is not 0,1 or 2 then this will ask for input again until players get the right input
    print("Invalid Input")
    choice = input("Your Choice? ")  
while choice != "0":
    
    if choice == "1":
        
        twochoice = in_town(game_vars)# runs the function in_town
        while twochoice not in ["0","1","2","3","9"]:# validates that the choice from in_town is 0,1,2,3 or 9 and if not prompts user to input the value again
            print("Invalid Input")
            twochoice = in_town(game_vars)
        
        if twochoice == "0":# Exits game
            print("Goodbye!")
            break
        if loop_flow(twochoice) == "end":# Signifies game has ended already
            break
    elif choice == "2":
        if loaded == True:
            load_game(game_vars,time_list,0) # Loads game with time_list as specified list
            load_game(game_vars,plant_list,1) # Loads game with plant_list as specified list
            loaded = False
        
        twochoice = in_town(game_vars)# runs the function in_town
        while twochoice not in ["0","1","2","3","9"]:# validates that the choice from in_town is 0,1,2,3 or 9 and if not prompts user to input the value again
            print("Invalid Input")
            twochoice = in_town(game_vars)
        if loop_flow(twochoice) == "end":# Signifies game has ended already
            break
        if twochoice == "0":# Exits game
            print("Goodbye!")
            break

    
        
        
