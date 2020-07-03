import random
import textwrap
import cmd
import sys
import os
import time
import json

#######################################################################################################################
playerhp = 100
guardhp = 30

#######################################################################################################################

# these are the different stored lists that will help save the information and progression to a file
decided = []
importantdecide = []
room = []
roomdecided = []
iteminv = []

# this is the players inventory, which is given to the user once they have looked around in their cell
inv = [
    {"name": "shiv", "damage": 5},
    {"name": "lock-pick", "description": "Unlocks door"},
]

# these are the items the user will be able to pick up throughout the game
items = [
    {"name": "hand-gun", "damage": 12},
    {"name": "knife", "damage": 8},
    {"name": "gas-bomb", "damage": 5},
    {"name": "Keys", "description": "Used to open exit"},
    {"name": "Map", "description": "Can be used to find the easiest way to get away from the camp"},
    {"name": "Rope", "description": "Can be used to climb down walls"},
    {"name": "Jacket", "description": "Can be used to pretend to be a guard"},
]

# this will be the player's name
playerinfo = ""
# Part F ###############################################################################################################

# this is the saving function. it will gather all the important information and decisions
# etc the user has made and places them into a file
def saves():
    time.sleep(2)
    print("--Saving The Game--")
    time.sleep(1)
    # this is reading th user's file
    with open('user.txt', 'r') as cf:
        # this is writing into the user's file
        with open('user.txt', 'w') as uf:
            json.dump("Player Information:", uf)
            uf.write("\n")
            json.dump(playerinfo, uf)
            uf.write("\n")
            json.dump("Player Score:", uf)
            uf.write("\n")
            playerscore = playerhp * 100
            json.dump(playerscore, uf)
            uf.write("\n")
            json.dump("Player Health:", uf)
            uf.write("\n")
            json.dump(playerhp, uf)
            uf.write("\n")
            json.dump("Important Decisions:", uf)
            uf.write("\n")
            json.dump(importantdecide, uf)
            uf.write("\n")
            json.dump("Rooms Covered", uf)
            uf.write("\n")
            json.dump(room, uf)
            uf.write("\n")
            json.dump(roomdecided, uf)
            uf.write("\n")
            json.dump("Player Inventory", uf)
            uf.write("\n")
            json.dump(inv, uf)
            json.dump(iteminv, uf)
            uf.write("\n")
            json.dump("Player Additional Decisions:", uf)
            uf.write("\n")
            json.dump(decided, uf)
        con = cf.read()
        print(con)
    time.sleep(2)
    print()
    print("Saved")
    sys.exit()


# Part E ###############################################################################################################

# these are the three different escape scenes fot the player
def escapeA():
    room.append("escapeA()")
    print("--Exit Scene--")
    global playerhp
    print()
    time.sleep(2)
    print("--Yard--")
    print()
    time.sleep(2)
    # these are the important decisions needed
    # if the player leaves with a friend and when they leave
    finala = importantdecide[0] # friend
    finalb = importantdecide[1]
    # if it is either the day time
    if finalb == "a" or finalb == "b":
        # decide to leave with frank
        if finala == "yes" or finala == "y":
            time.sleep(2)
            print("You and Frank look around")
            print()
            time.sleep(2)
            print("You see an exit")
            time.sleep(3)
            print("But there are guards everywhere...")
            finald = input("Do you A)Make a run for it or B)Hide under a car ").lower()
            # decision on escape route
            if finald == "a" or finald == "run":
                # decision on what you may want to do grab a metal plate or not
                print("You can grab a tin plate to help when you run")
                grab = input("Yes or No ").lower()
                if grab == "y" or grab == "yes":
                    print("You pick up the tin plate")
                    decided.append(finald)
                    # chance of being seen
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("Obergruppenfuhrer Blazgowitz sees you")
                        print("")
                        time.sleep(2)
                        print("I'm sorry but this is not your lucky day")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You and Frank get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            # random instance determining whether the player dies
                            z = random.randint(0, 9)
                            if z <= 4:
                                print("You deflect some of the bullets with the tin plate")
                                print()
                                time.sleep(2)
                                print("You get hit by one of the bullets")
                                time.sleep(1)
                                # player getting hit by a shot
                                playerhp -= 20
                                if z <= 2:
                                    print("You have died")
                                    m = playerhp * 100
                                    print("Your score is", m)
                                    time.sleep(2)
                                    sys.exit()
                                else:
                                    print("--Health--")
                                    print("Current hp ", playerhp)
                            else:
                                # player dies
                                print("The tin plate didn't stop the bullets")
                                time.sleep(2)
                                playerhp -= 20
                                print("You have died")
                                # player hp is turned into a score
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                sys.exit()
                        else:
                            # another random instance where frank can get killed
                            y = random.randint(0, 9)
                            if y <= 4:
                                print("Frank had been shot in the head")
                                time.sleep(2)
                                print()
                                print("You keep running")
                            else:
                                print()
                            print("You escape as the shots have missed you")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            # send the player to the next function to save the game and show player progression
                            saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                # if player decides not to grab the tin plate
                elif grab == "no" or grab == "n":
                    print("You decide to not grab the tin plate")
                    print("It might slow you down")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("Obergruppenfuhrer Blazgowitz sees you")
                        print("")
                        time.sleep(2)
                        print("I'm sorry but this is not your lucky day")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You and Frank get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You have died")
                            # player hp is turned into a score
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            y = random.randint(0, 9)
                            if y <= 4:
                                print("Frank had been shot in the head")
                                time.sleep(2)
                                print()
                                print("You keep running")
                            else:
                                print()
                            print("You escape as the shots have missed you")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "escape" or grab == "esc":
                    print("You decided to exit the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please enter Yes or No")
                    time.sleep(2)
                    escapeA()
            elif finald == "b" or finald == "hide":
                decided.append(finald)
                print("You both hide behind a large tree")
                print()
                time.sleep(2)
                print("You run under a car and hide ")
                z = random.randint(0, 9)
                if z <= 4:
                    print("You and frank fall off of the car too early")
                    time.sleep(2)
                    playerhp -= 25
                    print("You both get killed on the spot")
                    print()
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    print()
                    sys.exit()
                else:
                    print()
                    print("You then drop off as soon as the car")
                    print("Leaves the camp")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            elif finald == "esc" or finald == "escape":
                print("You decided to exit the game")
                saves()
            else:
                print("--Help--")
                print("Please select either to A)Run or B)Hide")
                escapeA()
        # decide to leave alone
        elif finala == "no" or finala == "n":
            time.sleep(2)
            print("You look around")
            print()
            time.sleep(2)
            print("You see an exit")
            time.sleep(3)
            print("But there are guards everywhere...")
            finald = input("Do you A)Make a run for it or B)Hide under a car ").lower()
            if finald == "a" or finald == "run":
                print("You can grab a tin plate to help when you run ")
                grab = input("Yes or No ").lower()
                if grab == "y" or grab == "yes":
                    print("You pick up the tin plate")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("Obergruppenfuhrer Blazgowitz sees you")
                        print("")
                        time.sleep(2)
                        print("I'm sorry but this is not your lucky day")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            z = random.randint(0, 9)
                            if z <= 4:
                                print("You deflect some of the bullets with the tin plate")
                                print()
                                time.sleep(2)
                                print("You get hit one of the bullets")
                                time.sleep(1)
                                playerhp -= 20
                                if z <= 2:
                                    print("You have died")
                                    m = playerhp * 100
                                    print("Your score is", m)
                                    time.sleep(2)
                                    sys.exit()
                                else:
                                    print("--Health--")
                                    print("Current hp ", playerhp)
                            else:
                                print("The tin plate didn't stop the bullets")
                                time.sleep(2)
                                playerhp -= 20
                                print("You have died")
                                print()
                                # player hp is turned into a score
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                sys.exit()
                        else:
                            y = random.randint(0, 9)
                            if y <= 4:
                                print("You keep running")
                            else:
                                print()
                        print("You escape as the shots have missed you")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "no" or grab == "n":
                    print("You decide to not grab the tin plate")
                    print("It might slow you down")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("Obergruppenfuhrer Blazgowitz sees you")
                        print("")
                        time.sleep(2)
                        print("I'm sorry but this is not your lucky day")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You have died")
                            print()
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            print("You keep running")
                            print("You escape as the shots have missed you")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "escape" or grab == "esc":
                    print("You decided to exit the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please enter Yes or No")
                    time.sleep(2)
                    escapeA()
            elif finald == "b" or finald == "hide":
                decided.append(finald)
                print("You hide behind a large tree")
                print()
                time.sleep(2)
                print("You run under a car and hide ")
                z = random.randint(0, 9)
                if z <= 4:
                    print("You fall off of the car too early")
                    time.sleep(2)
                    playerhp -= 20
                    print("You get killed on the spot")
                    print()
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print()
                    print("You then drop off as soon as the car")
                    print("Leaves the camp")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            elif finald == "esc" or finald == "escape":
                print("You decided to exit the game")
                saves()
            else:
                print("--Help--")
                print("Please select either to A)Run or B)Hide")
                escapeA()
    # or if it is midnight
    elif finalb == "c":
        if finala == "yes" or finala == "y":
            time.sleep(2)
            print("You and Frank look around")
            print()
            time.sleep(2)
            print("You see an exit")
            time.sleep(3)
            print("But there is one guard...")
            finald = input("Do you A)Make a run for it or B)Hide under a car ").lower()
            if finald == "a" or finald == "run":
                print("You can grab a tin plate to help when you run")
                grab = input("Yes or No ").lower()
                if grab == "y" or grab == "yes":
                    print("You pick up the tin plate")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("Obergruppenfuhrer Blazgowitz sees you")
                        print("")
                        time.sleep(2)
                        print("I'm sorry but this is not your lucky day")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You and Frank get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            z = random.randint(0, 9)
                            if z <= 4:
                                print("You deflect some of the bullets with the tin plate")
                                print()
                                time.sleep(2)
                                print("You get hit one of the bullets")
                                time.sleep(1)
                                playerhp -= 20
                                if z <= 0:
                                    print("You have died")
                                    m = playerhp * 100
                                    print("Your score is", m)
                                    time.sleep(2)
                                    sys.exit()
                                else:
                                    print("--Health--")
                                    print("Current hp ", playerhp)
                            else:
                                print("The tin plate didn't stop the bullets")
                                time.sleep(2)
                                playerhp -= 20
                                print("You have died")
                                print()
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                sys.exit()
                        else:
                            y = random.randint(0, 9)
                            if y <= 4:
                                print("Frank had been shot in the head")
                                time.sleep(2)
                                print()
                                print("You keep running")
                            else:
                                print()
                        print("You escape as the shots have missed you")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "no" or grab == "n":
                    print("You decide to not grab the tin plate")
                    print("It might slow you down")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("The guard sees you")
                        print("")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You and Frank get shot at")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You have died")
                            print()
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            y = random.randint(0, 9)
                            if y <= 4:
                                print("Frank had been shot in the head")
                                time.sleep(2)
                                print()
                                print("You keep running")
                            print("You escape as the shots have missed you")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                elif grab == "escape" or grab == "esc":
                    print("You decided to exit the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please enter Yes or No")
                    time.sleep(2)
                    escapeA()
            elif finald == "b" or finald == "hide":
                decided.append(finald)
                print("You hide behind a large tree")
                print()
                time.sleep(2)
                print("You run under a car and hide ")
                z = random.randint(0, 9)
                if z <= 4:
                    print("You and frank fall off of the car too early")
                    time.sleep(2)
                    playerhp -= 20
                    print("You both get killed on the spot")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print()
                    print("You then drop off as soon as the car")
                    print("Leaves the camp")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            elif finald == "esc" or finald == "escape":
                print("You decided to exit the game")
                saves()
            else:
                print("--Help--")
                print("Please select either to A)Run or B)Hide")
                escapeA()
        elif finala == "no" or finala == "n":
            time.sleep(2)
            print("You look around")
            print()
            time.sleep(2)
            print("You see an exit")
            time.sleep(3)
            print("But there are guards...")
            finald = input("Do you A)Make a run for it or B)Hide under a car ").lower()
            if finald == "a" or finald == "run":
                print("You can grab a tin plate to help when you run")
                grab = input("Yes or No ").lower()
                if grab == "y" or grab == "yes":
                    print("You pick up the tin plate")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("The guard sees you")
                        print("")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You get shot at by several guards people at once")
                            print()
                            time.sleep(2)
                            z = random.randint(0, 9)
                            if z <= 4:
                                print("You deflect some of the bullets with the tin plate")
                                print()
                                time.sleep(2)
                                print("You get hit one of the bullets")
                                time.sleep(1)
                                playerhp -= 20
                                if z <= 0:
                                    print("You have died")
                                    m = playerhp * 100
                                    print("Your score is", m)
                                    time.sleep(2)
                                    sys.exit()
                                else:
                                    print("--Health--")
                                    print("Current hp ", playerhp)
                            else:
                                print("The tin plate didn't stop the bullets")
                                time.sleep(2)
                                playerhp -= 20
                                print("You have died")
                                print()
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                sys.exit()
                        else:
                            print("You keep running")
                        print("You escape as the shots have missed you")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "no" or grab == "n":
                    print("You decide to not grab the tin plate")
                    print("It might slow you down")
                    decided.append(finald)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("The guard sees you")
                        print("")
                        time.sleep(2)
                        x = random.randint(0, 9)
                        if x <= 4:
                            print("You get shot at")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You have died")
                            print()
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            print("You keep running")
                            print("You escape as the shots have missed you")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                    else:
                        print("You escape easily")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                elif grab == "escape" or grab == "esc":
                    print("You decided to exit the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please enter Yes or No")
                    time.sleep(2)
                    escapeA()
            elif finald == "b" or finald == "hide":
                decided.append(finald)
                print("You hide behind a large tree")
                print()
                time.sleep(2)
                print("You run under a car and hide ")
                z = random.randint(0, 9)
                if z <= 4:
                    print("You fall off of the car too early")
                    time.sleep(2)
                    playerhp -= 20
                    print("You get killed on the spot")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print()
                    print("You then drop off as soon as the car")
                    print("Leaves the camp")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            elif finald == "esc" or finald == "escape":
                print("You decided to exit the game")
                saves()
            else:
                print("--Help--")
                print("Please select either to A)Run or B)Hide")
                escapeA()


# this is the second option for the player
def escapeB():
    room.append("escapeB()")
    print("--Exit Scene--")
    global playerhp
    print()
    time.sleep(2)
    print("--Camp Field--")
    print()
    time.sleep(2)
    finala = importantdecide[0] # friend
    finalb = importantdecide[1]
    if finalb == "a" or finalb == "b":
        if finala == "yes" or finala == "y":
            print("You and Frank see a shed")
            time.sleep(2)
            print("Do you want to open it?")
            op = input("Yes or No ").lower()
            # looks at the shed
            if op == "yes" or op == "y":
                print("You use the lock picks to open the shed")
                time.sleep(2)
                print("And it opens")
                print()
                time.sleep(2)
                print("Inside there is a family of rats eating way in the trash")
                y = random.randint(0, 9)
                # box may be inside of the shed
                if y <= 4:
                    print("There is a box under the trash")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    # a map may be inside of the box
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing in the trash worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the shed")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                escapeB()
            m = random.randint(0, 9)
            if m <= 4:
                print("Several guards see you both")
                print("")
                time.sleep(2)
                print("They start to shoot at you ")
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You both get shot at by several guards at once")
                    print()
                    time.sleep(2)
                    print("You see a wall and a table")
                    print()
                    time.sleep(1)
                    print("You both run up to the table and start to climb over it")
                    print()
                    time.sleep(2)
                    print("One of the tower guards has seen you")
                    print()
                    time.sleep(2)
                    playerhp -= 20
                    print("You have been killed")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You both get shot at by several guards at once")
                    print()
                    time.sleep(2)
                    print("Frank gets shot and killed")
                    print()
                    time.sleep(2)
                    print("You keep running and find a wall and table")
                    time.sleep(3)
                    print()
                    print("You manage to land and make a run for the forest")
                    print()
                    print("You have completed the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            else:
                print("You both start to climb a wall")
                print()
                time.sleep(2)
                print("You jump over")
                print()
                print("You then run for the forest ")
                print("")
                time.sleep(2)
                print("You finished the game")
                time.sleep(2)
                m = playerhp * 100
                print("Your score is", m)
                time.sleep(2)
                saves()
        elif finala == "no" or finala == "n":
                print("You see a shed")
                time.sleep(2)
                print("Do you want to open it?")
                op = input("Yes or No ").lower()
                if op == "yes" or op == "y":
                    print("You use the lock picks to open the shed")
                    time.sleep(2)
                    print("And it opens")
                    print()
                    time.sleep(2)
                    print("Inside there is a family of rats eating way in the trash")
                    y = random.randint(0, 9)
                    if y <= 4:
                        print("There is a box under the trash")
                        time.sleep(2)
                        z = random.randint(0, 9)
                        if z <= 4:
                            print("A map is inside the box")
                            for objects in items:
                                if objects['name'] == "Map":
                                    iteminv.append(objects)
                                    print("--You have", inv, iteminv, "in your inventory--")
                                    print()
                                    time.sleep(2)
                                    break
                        else:
                            print("There is nothing inside")
                            print()
                            time.sleep(2)
                    else:
                        print("There is nothing in the trash worth while")
                        print()
                        time.sleep(2)
                elif op == "no" or op == "n":
                    print("You decided to not look at the shed")
                    time.sleep(2)
                elif op == "esc" or op == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    escapeB()
                m = random.randint(0, 9)
                if m <= 4:
                    print("Several guards see you")
                    print("")
                    time.sleep(2)
                    print("They start to shoot at you ")
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You get shot at by several guards at once")
                        print()
                        print("You see a wall and a table")
                        print()
                        time.sleep(1)
                        print("You run up to the table and start to climb over it")
                        print()
                        time.sleep(2)
                        print("One of the tower guards has seen you")
                        print()
                        time.sleep(2)
                        playerhp -= 25
                        print("You have been killed")
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        sys.exit()
                    else:
                        print("You get shot at by several guards at once")
                        print()
                        time.sleep(2)
                        print("You keep running and find a wall and table")
                        time.sleep(3)
                        print()
                        print("You manage to land and make a run for the forest")
                        print()
                        print("You have completed the game")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                else:
                    print("You start to climb a wall")
                    print()
                    time.sleep(2)
                    print("You jump over")
                    print()
                    print("You then run for the forest ")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
    elif finalb == "c":
        if finala == "yes" or finala == "y":
            print("You and Frank see a shed in the dark")
            time.sleep(2)
            print("Do you want to open it?")
            op = input("Yes or No ").lower()
            if op == "yes" or op == "y":
                print("You use the lock picks to open the shed")
                time.sleep(2)
                print("And it opens")
                print()
                time.sleep(2)
                print("Inside there is a family of rats sleeping in the trash")
                y = random.randint(0, 9)
                if y <= 4:
                    print("There is a box under the trash")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing in the trash worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the shed")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                escapeB()
            m = random.randint(0, 9)
            if m <= 4:
                print("A guard sees you both")
                print("")
                time.sleep(2)
                print("He starts to shoot at you ")
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You both get shot at by the guard")
                    print()
                    time.sleep(2)
                    print("You see a wall and a table")
                    print()
                    time.sleep(1)
                    print("You both run up to the table ant start to climb over it")
                    print()
                    time.sleep(2)
                    print("One of the tower guards has seen you")
                    print()
                    time.sleep(2)
                    playerhp -= 20
                    print("You have been killed")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You both get shot at by several guards at once")
                    print()
                    time.sleep(2)
                    print("Frank gets shot and killed")
                    print()
                    time.sleep(2)
                    print("You keep running and find a wall and table")
                    time.sleep(3)
                    print()
                    print("You manage to land and make a run for the dark forest")
                    print()
                    print("You have completed the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
            else:
                print("You both start to climb a wall")
                print()
                time.sleep(2)
                print("You jump over")
                print()
                print("You then run for the dark forest ")
                print("")
                time.sleep(2)
                print("You finished the game")
                time.sleep(2)
                m = playerhp * 100
                print("Your score is", m)
                time.sleep(2)
                saves()
        elif finala == "no" or finala == "n":
                print("You see a shed in the dark")
                time.sleep(2)
                print("Do you want to open it?")
                op = input("Yes or No ").lower()
                if op == "yes" or op == "y":
                    print("You use the lock picks to open the shed")
                    time.sleep(2)
                    print("And it opens")
                    print()
                    time.sleep(2)
                    print("Inside there is a family of rats sleeping in the trash")
                    y = random.randint(0, 9)
                    if y <= 4:
                        print("There is a box under the trash")
                        time.sleep(2)
                        z = random.randint(0, 9)
                        if z <= 4:
                            print("A map is inside the box")
                            for objects in items:
                                if objects['name'] == "Map":
                                    iteminv.append(objects)
                                    print("--You have", inv, iteminv, "in your inventory--")
                                    print()
                                    time.sleep(2)
                                    break
                        else:
                            print("There is nothing inside")
                            print()
                            time.sleep(2)
                    else:
                        print("There is nothing in the trash worth while")
                        print()
                        time.sleep(2)
                elif op == "no" or op == "n":
                    print("You decided to not look at the shed")
                    time.sleep(2)
                elif op == "esc" or op == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    escapeB()
                m = random.randint(0, 9)
                if m <= 4:
                    print("A guard see you")
                    print("")
                    time.sleep(2)
                    print("They start to shoot at you ")
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You see a wall and a table")
                        print()
                        time.sleep(1)
                        print("You run up to the table ant start to climb over it")
                        print()
                        time.sleep(2)
                        print("One of the tower guards has seen you")
                        print()
                        time.sleep(2)
                        playerhp -= 20
                        print("You have been killed")
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        sys.exit()
                    else:
                        print("You get shot at by several guards at once")
                        print()
                        time.sleep(2)
                        print("You keep running and find a wall and table")
                        time.sleep(3)
                        print()
                        print("You manage to land and make a run for the dark forest")
                        print()
                        print("You have completed the game")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
                else:
                    print("You start to climb a wall")
                    print()
                    time.sleep(2)
                    print("You jump over")
                    print()
                    print("You then run for the dark forest ")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()


def escapeC():
    room.append("escapeC()")
    print("--Exit Scene--")
    global playerhp
    print()
    time.sleep(2)
    print("--Guards Tower--")
    print()
    time.sleep(2)
    finala = importantdecide[0] # friend
    finalb = importantdecide[1]
    if finalb == "a" or finalb == "b":
        if finala == "yes" or finala == "y":
            print("You both see the guards tower")
            time.sleep(2)
            # decide to open the crate
            print("Do you want to open the crate in front of the tower?")
            op = input("Yes or No ").lower()
            if op == "yes" or op == "y":
                print("You use the lock picks to open the box")
                time.sleep(2)
                print("Inside there is a pile of ropes, and german jackets")
                time.sleep(2)
                print()
                print("What do you grab?")
                print("A)The Ropes")
                print("B)The Jackets")
                print("C)Both")
                # player decides on the items they want
                box = input("Please choose and option: ").lower()
                if box == "a" or box == "the rope" or box == "rope" or box == "r":
                    print("The rope is added into your inventory")
                    # saved into the user's inventory
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "b" or box == "the jacket" or box == "jacket" or box == "j":
                    print("You decided to leave the rope and take the jacket")
                    time.sleep(2)
                    print("You both put on the jacket")
                    for objects in items:
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "c" or box == "both" or box == "jacket and rope" or box == "b" or box == "rope and jacket":
                    print("You chose to take both items")
                    time.sleep(2)
                    print("You both put on the jacket and hold the rope")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "esc" or box == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    print("Then decide on what items you want to pick up")
                    escapeC()
                y = random.randint(0, 9)
                if y <= 4:
                    print("There is a box underneath")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing else worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the crate")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                print("Then decide on what items you want to pick up if so")
                escapeC()
            x = random.randint(0, 9)
            if x <= 4:
                print("The tower guards see you")
                print()
                time.sleep(2)
                print("They both start to shoot at you ")
                print()
                time.sleep(2)
                print("Frank runs and beats up one of the guards")
                print("He kills him as the other guard shoots Frank")
                print()
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You get shot in close ranges by a sniper rifle")
                    print()
                    time.sleep(2)
                    playerhp -= 30
                    print("You have died")
                    print()
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You see a shot-gun")
                    print()
                    time.sleep(1)
                    print("You quickly grab it")
                    print()
                    time.sleep(2)
                    print("You kill one guard")
                    print()
                    time.sleep(2)
                    print("The other guard gets closer as he attempts to hit you")
                    print()
                    time.sleep(2)
                    print("You shot the guard in the face with the shot gun")
                    print()
                    time.sleep(2)
                    print("He falls onto the ground covered in a pool of blood")
                    print()
                    time.sleep(2)
                    for objects in iteminv:
                        if objects['name'] == "Jacket":
                            x = random.randint(0, 9)
                            if x <= 4:
                                print("You get noticed by a guard")
                                print()
                                time.sleep(2)
                                print("You are not Arno")
                                print()
                                time.sleep(2)
                                print("He shoots you")
                                playerhp -= 20
                                print("You died")
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                sys.exit()
                            else:
                                print("You leave by walking through the main exit")
                                time.sleep(2)
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                saves()
                    print("You put on his uniform")
                    print()
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You get noticed by a guard")
                        print()
                        time.sleep(2)
                        print("You are not Arno")
                        print()
                        time.sleep(2)
                        print("He shoots you")
                        playerhp -= 20
                        print("You died")
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        sys.exit()
                    else:
                        print("You leave by walking through the main exit")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
            else:
                for objects in iteminv:
                    if objects['name'] == "Rope":
                        print("You use the rope to start climbing down the wall")
                        x = random.randint(0, 9)
                        if x <= 4:
                            time.sleep(2)
                            print("You slip and fall to your death")
                            sys.exit()
                        else:
                            print("You make it down safely")
                            print("You both then run for the forest")
                            print("")
                            time.sleep(2)
                            print("You finished the game")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                print("You climb up the tower and then climb down the other side of the wall")
                print()
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    playerhp -= 20
                    print("You slip and fall to your death")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You make it down safely")
                    time.sleep(2)
                    print()
                    print("But Frank...")
                    print("He fell and broke his neck")
                    time.sleep(2)
                    print()
                    print("You then run for the forest")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
        elif finala == "no" or finala == "n":
            print("You see the guards tower")
            time.sleep(2)
            print("Do you want to open the crate in front of the tower?")
            op = input("Yes or No ").lower()
            if op == "yes" or op == "y":
                print("You use the lock picks to open the box")
                time.sleep(2)
                print("Inside there is a pile of ropes, and german jackets")
                time.sleep(2)
                print()
                print("What do you grab?")
                print("A)The Rope")
                print("B)The jacket")
                print("C)Both")
                box = input("Please choose and option: ").lower()
                if box == "a" or box == "the rope" or box == "rope" or box == "r":
                    print("The rope is added into your inventory")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "b" or box == "the jacket" or box == "jacket" or box == "j":
                    print("You decided to leave the rope and take the jacket")
                    time.sleep(2)
                    print("You put on the jacket")
                    for objects in items:
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "c" or box == "both" or box == "jacket and rope" or box == "b" or box == "rope and jacket":
                    print("You chose to take both items")
                    time.sleep(2)
                    print("You put on the jacket and hold the rope")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "esc" or box == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    print("Then decide on what items you want to pick up")
                    escapeC()
                y = random.randint(0, 9)
                if y <= 4:
                    print("There is a box underneath")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing else worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the box")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                print("Then decide on what items you want to pick up")
                escapeC()
            x = random.randint(0, 9)
            if x <= 4:
                print("The tower guards see you")
                print()
                time.sleep(2)
                print("They both start to shoot at you ")
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You get shot in close ranges by a sniper rifle")
                    print()
                    time.sleep(2)
                    playerhp -= 20
                    print("You have died")
                    print()
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You see a shot-gun")
                    print()
                    time.sleep(1)
                    print("You quickly grab it")
                    print()
                    time.sleep(2)
                    print("You kill one guard")
                    print()
                    time.sleep(2)
                    print("The other guard gets closer as he attempts to hit you")
                    print()
                    time.sleep(2)
                    print("You shot the guard in the face with the shot gun")
                    print()
                    time.sleep(2)
                    print("He falls onto the ground covered in a pool of blood")
                    print()
                    time.sleep(2)
                    for objects in iteminv:
                        if objects['name'] == "Jacket":
                            x = random.randint(0, 9)
                            if x <= 4:
                                print("You get noticed by a guard")
                                print()
                                time.sleep(2)
                                print("You are not Arno")
                                print()
                                time.sleep(2)
                                playerhp -= 25
                                print("He shoots you")
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                print("You died")
                                sys.exit()
                            else:
                                print("You leave by walking through the main exit")
                                time.sleep(2)
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                saves()
                    print("You put on his uniform")
                    print()
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You get noticed by a guard")
                        print()
                        time.sleep(2)
                        playerhp -= 25
                        print("You are not Arno")
                        print()
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        print("He shoots you")
                        print("You died")
                        sys.exit()
                    else:
                        print("You leave by walking through the main exit")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
            else:
                for objects in iteminv:
                    if objects['name'] == "Rope":
                        print("You use the rope to start climbing down the wall")
                        x = random.randint(0, 9)
                        if x <= 4:
                            time.sleep(2)
                            playerhp -= 20
                            print("You slip and fall to your death")
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            print("You make it down safely")
                            print("You then run for the forest")
                            print("")
                            time.sleep(2)
                            print("You finished the game")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                print("You climb up the tower and then climb down the other side of the wall")
                print()
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    playerhp -= 20
                    print("You slip and fall to your death")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You make it down safely")
                    print("You then run for the forest")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
    elif finalb == "c":
        if finala == "yes" or finala == "y":
            print("You both see the guards tower")
            time.sleep(2)
            print("Do you want to open the crate in front of the tower?")
            op = input("Yes or No ").lower()
            if op == "yes" or op == "y":
                print("You use the lock picks to open the box")
                time.sleep(2)
                print("Frank: Well done, you are really good at that")
                print("Inside there is a pile of ropes, and german jackets")
                time.sleep(2)
                print()
                print("What do you both grab?")
                print("A)The Rope")
                print("B)The jackets")
                print("C)Both")
                box = input("Please choose and option: ").lower()
                if box == "a" or box == "the rope" or box == "rope" or box == "r":
                    print("The rope is added into your inventory")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "b" or box == "the jacket" or box == "jacket" or box == "j":
                    print("You decided to leave the rope and take the jacket")
                    time.sleep(2)
                    print("You and Frank put on the jacket")
                    for objects in items:
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "c" or box == "both" or box == "jacket and rope" or box == "b" or box == "rope and jacket":
                    print("You chose to take both items")
                    time.sleep(2)
                    print("You and Frank put on the jacket and hold the rope")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "esc" or box == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    print("Then decide on what items you want to pick up")
                    escapeC()
                y = random.randint(0, 9)
                if y <= 4:
                    print("There is a box underneath")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing else worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the box")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                print("Then decide on what items you want to pick up")
                escapeC()
            x = random.randint(0, 9)
            if x <= 4:
                print("You both walk into the tower")
                time.sleep(2)
                print()
                print("The tower guard see you")
                print("")
                time.sleep(2)
                print("He starts to shoot at you")
                time.sleep(2)
                print("Frank jumps in front of the bullet")
                print("as Frank yells: Go!")
                x = random.randint(0, 9)
                if x <= 4:
                    print("You get shot in close ranges by a sniper rifle")
                    print()
                    time.sleep(2)
                    playerhp -= 30
                    print("You have died")
                    print()
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You see a shot-gun")
                    print()
                    time.sleep(1)
                    print("You quickly grab it")
                    print()
                    time.sleep(2)
                    print("The guard gets closer as he attempts to hit you")
                    print()
                    time.sleep(2)
                    print("You shot the guard in the face with the shot gun")
                    print()
                    time.sleep(2)
                    print("He falls onto the ground covered in a pool of blood")
                    print()
                    time.sleep(2)
                    for objects in iteminv:
                        if objects['name'] == "Jacket":
                            x = random.randint(0, 9)
                            if x <= 4:
                                print("You get noticed by a guard")
                                print()
                                time.sleep(2)
                                playerhp -= 25
                                print("You are not Arno")
                                print()
                                time.sleep(2)
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                print("He shoots you")
                                print("You died")
                                sys.exit()
                            else:
                                print("You leave by walking through the main exit")
                                print("Into the dark...")
                                time.sleep(2)
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                saves()
                    print("You put on his uniform")
                    print()
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You get noticed by a guard")
                        print("in the dark distance")
                        print()
                        time.sleep(2)
                        playerhp -= 25
                        print("You are not Arno")
                        print()
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        print("He shoots you")
                        print("You died")
                        sys.exit()
                    else:
                        print("You leave by walking through the main exit")
                        print("Into the dark...")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
            else:
                for objects in iteminv:
                    if objects['name'] == "Rope":
                        print("You both use the ropes to start climbing down the wall")
                        x = random.randint(0, 9)
                        if x <= 4:
                            time.sleep(2)
                            print("You cannot see very well in the dark")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You slip and fall to your death")
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            print("You both make it down safely")
                            print("You then run for the dark forest")
                            print("")
                            time.sleep(2)
                            print("You finished the game")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                print("You climb up the tower and then climb down the other side of the wall")
                print()
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You cannot see very well in the dark")
                    print()
                    time.sleep(2)
                    playerhp -= 20
                    print("You slip and fall to your death")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You make it down safely")
                    time.sleep(2)
                    print("But Frank fell down ...")
                    time.sleep(2)
                    print("And died")
                    print()
                    time.sleep(2)
                    print("You then run for the dark forest")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()
        elif finala == "no" or finala == "n":
            print("You see the guards tower")
            time.sleep(2)
            print("Do you want to open the crate in front of the tower?")
            op = input("Yes or No ").lower()
            if op == "yes" or op == "y":
                print("You use the lock picks to open the box")
                time.sleep(2)
                print("Inside there is a pile of ropes, and german jackets")
                time.sleep(2)
                print()
                print("What do you grab?")
                print("A)The Rope")
                print("B)The jacket")
                print("C)Both")
                box = input("Please choose and option: ").lower()
                if box == "a" or box == "the rope" or box == "rope" or box == "r":
                    print("The rope is added into your inventory")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "b" or box == "the jacket" or box == "jacket" or box == "j":
                    print("You decided to leave the rope and take the jacket")
                    time.sleep(2)
                    print("You put on the jacket")
                    for objects in items:
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "c" or box == "both" or box == "jacket and rope" or box == "b" or box == "rope and jacket":
                    print("You chose to take both items")
                    time.sleep(2)
                    print("You put on the jacket and hold the rope")
                    for objects in items:
                        if objects['name'] == "Rope":
                            iteminv.append(objects)
                        if objects['name'] == "Jacket":
                            iteminv.append(objects)
                            print("--You have", inv, iteminv, "in your inventory--")
                            print()
                            time.sleep(2)
                            break
                elif box == "esc" or box == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("--Help--")
                    print("Please type Yes or No")
                    print("Then decide on what items you want to pick up")
                    escapeC()
                y = random.randint(0, 9)
                if y <= 4:
                    print("There is a box underneath")
                    time.sleep(2)
                    z = random.randint(0, 9)
                    if z <= 4:
                        print("A map is inside the box")
                        for objects in items:
                            if objects['name'] == "Map":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                    else:
                        print("There is nothing inside")
                        print()
                        time.sleep(2)
                else:
                    print("There is nothing else worth while")
                    print()
                    time.sleep(2)
            elif op == "no" or op == "n":
                print("You decided to not look at the box")
                time.sleep(2)
            elif op == "esc" or op == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("--Help--")
                print("Please type Yes or No")
                print("Then decide on what items you want to pick up")
                escapeC()
            x = random.randint(0, 9)
            if x <= 4:
                print("You walk into the tower")
                time.sleep(2)
                print()
                print("The tower guard see you")
                print("")
                time.sleep(2)
                print("He starts to shoot at you ")
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You get shot in close ranges by a sniper rifle")
                    print()
                    time.sleep(2)
                    playerhp -= 30
                    print("You have died")
                    print()
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You see a shot-gun")
                    print()
                    time.sleep(1)
                    print("You quickly grab it")
                    print()
                    time.sleep(2)
                    print("The guard gets closer as he attempts to hit you")
                    print()
                    time.sleep(2)
                    print("You shot the guard in the face with the shot gun")
                    print()
                    time.sleep(2)
                    print("He falls onto the ground covered in a pool of blood")
                    print()
                    time.sleep(2)
                    for objects in iteminv:
                        if objects['name'] == "Jacket":
                            x = random.randint(0, 9)
                            if x <= 4:
                                print("You get noticed by a guard")
                                print()
                                time.sleep(2)
                                playerhp -= 25
                                print("You are not Arno")
                                print()
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                print("He shoots you")
                                print("You died")
                                sys.exit()
                            else:
                                print("You leave by walking through the main exit")
                                print("Into the dark...")
                                time.sleep(2)
                                m = playerhp * 100
                                print("Your score is", m)
                                time.sleep(2)
                                saves()
                    print("You put on his uniform")
                    print()
                    time.sleep(2)
                    x = random.randint(0, 9)
                    if x <= 4:
                        print("You get noticed by a guard")
                        print("in the dark distance")
                        print()
                        time.sleep(2)
                        playerhp -= 20
                        print("You are not Arno")
                        print()
                        time.sleep(2)
                        print("He shoots you")
                        print("You died")
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        sys.exit()
                    else:
                        print("You leave by walking through the main exit")
                        print("Into the dark...")
                        time.sleep(2)
                        m = playerhp * 100
                        print("Your score is", m)
                        time.sleep(2)
                        saves()
            else:
                for objects in iteminv:
                    if objects['name'] == "Rope":
                        print("You use the rope to start climbing down the wall")
                        x = random.randint(0, 9)
                        if x <= 4:
                            time.sleep(2)
                            print("You cannot see very well in the dark")
                            print()
                            time.sleep(2)
                            playerhp -= 20
                            print("You slip and fall to your death")
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            sys.exit()
                        else:
                            print("You make it down safely")
                            print("You then run for the dark forest")
                            print("")
                            time.sleep(2)
                            print("You finished the game")
                            time.sleep(2)
                            m = playerhp * 100
                            print("Your score is", m)
                            time.sleep(2)
                            saves()
                print("You climb up the tower and then climb down the other side of the wall")
                print()
                time.sleep(2)
                x = random.randint(0, 9)
                if x <= 4:
                    print("You cannot see very well in the dark")
                    print()
                    time.sleep(2)
                    playerhp -= 20
                    print("You slip and fall to your death")
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    sys.exit()
                else:
                    print("You make it down safely")
                    print("You then run for the dark forest")
                    print("")
                    time.sleep(2)
                    print("You finished the game")
                    time.sleep(2)
                    m = playerhp * 100
                    print("Your score is", m)
                    time.sleep(2)
                    saves()


# here the player decides the way they want to escape
def Escape():
    room.append("escape()")
    print("You get to the door")
    print()
    time.sleep(2)
    h_key = False
    # check and see if the player has the keys
    for objects in iteminv:
        if objects['name'] == "Keys":
            h_key = True
    if h_key == True:
        print("You open the door")
        # choose a path to leave
        print("Do you head left, right or straight")
        x = input("A, B or C ").lower()
        if x == "a" or x == "left":
            decided.append(x)
            escapeA()
        elif x == "b" or x == "right":
            decided.append(x)
            escapeB()
        elif x == "c" or x == "straight":
            decided.append(x)
            escapeC()
        elif x == "esc" or x == "escape":
            print("You decided to exit the game")
            saves()
        else:
            print("--Help--")
            print("Please decide on the path you want to go")
            Escape()
    else:
        # player has to gather the keys
        print("You don't have the keys, it's locked")
        time.sleep(2)
        print("--Decision--")
        print()
        time.sleep(2)
        print("Where do you want to go?")
        print()
        print("Do you want to:")
        print("A)Guards office")
        print("B)Armoury")
        d = input().lower()
        if d == "a":
            decided.append(d)
            guardsofficecheck()
        elif d == "b":
            decided.append(d)
            armouryCheck()
        elif d == "esc" or d == "escape":
            print("You decided to exit the game")
            saves()
        else:
            print("--Help--")
            print("Please enter A or B")
            time.sleep(2)
            Escape()

# Part D ###############################################################################################################
# these are the rooms and scenes within the inside of the building
# they allow the user to gather items and fight guards depending on the random instance
def interrogation():
    room.append("interrogation()")
    print("---Interrogation-Room---")
    time.sleep(2)
    print("You get to the interrogation room")
    # x is the time of day decided by the user
    x = importantdecide[1]
    print()
    time.sleep(2)
    # these elements are needed to allow for the guard's and player's heath do decrease
    global guardhp
    global playerhp
    # these are made so that i can declare them as true later on if the user has used an item
    h_gun = False
    h_knife = False
    h_bomb = False
    h_shiv = False
    if x == "a" or x == "b":
        # random instance where a guard might see player
        x = random.randint(0, 9)
        if x <= 4:
            print("A guard is in the room")
            time.sleep(2)
            print("He sees you!")
            print()
            time.sleep(2)
            # depending on the item within the player inventory the weapon used will be declared true
            for objects in inv:
                if objects['name'] == "hand-gun":
                    h_gun = True
                else:
                    if objects['name'] == "knife":
                        h_knife = True
                    else:
                        if objects['name'] == "gas-bomb":
                            h_bomb = True
                        else:
                            h_shiv = True
            if h_gun == True:
                # the while loop allows for the guard and character to fight
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    # if the player is killed then the game is lost
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        break
                    else:
                        # based on the weapon the user may have more or less damage eg a gun has 12 damage
                        # all guards have 5 damage to make the game easier for the player
                        playerhp -= 5
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use your gun")
                        print("You shoot the guard")
                        print()
                        guardhp -= 12
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_knife == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        break
                    else:
                        playerhp -= 5
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You stab the guard")
                        print()
                        guardhp -= 8
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_bomb == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        break
                    else:
                        playerhp -= 2
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use the gas bomb")
                        print("You throw it to the guard")
                        print()
                        guardhp -= 5
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_shiv == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        break
                    else:
                        playerhp -= 2
                        print("you get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use your shiv")
                        print("You stab the guard")
                        print()
                        guardhp -= 5
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            # check if they have a weapon if not then use shiv else use the weapon
        else:
            print("No one is guarding")
            print()
            time.sleep(2)
            print("You look inside and there is a prisoner inside tied up")
            print()
            time.sleep(2)
            print("He is clearly dying, and the door is locked")
            print()
            time.sleep(3)
            print("You notice there is a door on the other side of the room")
            print()
            time.sleep(4)
    elif x == "c":
        print("No one is guarding the room")
        print()
        time.sleep(2)
        print("You look inside and there is a prisoner inside tied up")
        print()
        time.sleep(2)
        print("He is clearly dying, and the door is locked")
        print()
        time.sleep(3)
        print("There is nothing you can do")
        print()
        time.sleep(2)
    # decision to look around
    print("Do you look around?")
    # the player is able to look around
    look = input("A)Yes or B)No ").lower()
    decided.append(look)
    if look == "a" or look == "yes" or look == "y":
        print("There is a desk on the corner of the room")
        print("alongside the other side of the room is a dying prisoner")
        time.sleep(2)
        print("He has no energy to move and is dying")
        time.sleep(2)
        print()
        print("Do you look at the desk?")
        desk = input("A)yes or B)no ").lower()
        decided.append(desk)
        if desk == "a" or desk == "yes" or desk == "y":
            x = random.randint(0, 9)
            if x <= 4:
                # the player is able to find a health pack is choosing to loo around
                print("You find a health pack")
                time.sleep(2)
                print("You use the health pack and it increases health by 10")
                print("--Health--")
                # additional health is given to the player
                playerhp += 10
                print("--", playerhp, "--")
            else:
                print("There are documents in the desk")
                print("on top of the desk there is a note")
                time.sleep(2)
                print("It has several names and a paragraph written in german")
                time.sleep(2)
                print("It states that this is a list of people being executed within the next week")
                time.sleep(3)
                print("You are on the list")
                time.sleep(2)
        elif desk == "b" or desk == "no" or desk == "n":
            print("You look at the prisoner on the floor")
            time.sleep(2)
            print("You cannot tell if the man is dead or just weak")
            time.sleep(2)
            print("Do you head over to him?")
            looking = input("A)Yes or B)No ").lower()
            decided.append(looking)
            if looking == "a" or looking == "yes" or looking == "y":
                print("You head over and inspect, the man is clearly about to die")
                time.sleep(2)
            else:
                print("You decided not to bother, he is dead either way")
        # if the player decides to leave the game all his progress wis saved in a file
        elif desk == "esc" or desk == "escape":
            print("You decided to exit the game")
            saves()
        elif desk == "h" or desk == "help":
            print("--Help--")
            print("Please decide on looking at the desk or not")
            hdesk = input("A)Yes or B)No ").lower()
            if hdesk == "a" or hdesk == "yes" or hdesk == "y":
                # this is a random instance where the user might find a health pack to increase health
                x = random.randint(0, 9)
                if x <= 4:
                    print("You find a health pack")
                    time.sleep(2)
                    print("You use the health pack and it increases health by 10")
                    print("--Health--")
                    playerhp += 10
                    print("--", playerhp, "--")
                else:
                    print("There is a pile of documents in the desk")
                    print("on top of the desk there is a note")
                    time.sleep(2)
                    print("It has several names and a paragraph written in german")
                    time.sleep(2)
                    print("It states that this is a list of people being executed within the next week")
                    time.sleep(3)
                    print("You are on the list")
                    time.sleep(2)
            elif hdesk == "b" or hdesk == "no" or hdesk == "n":
                print("You look at the prisoner on the floor")
                time.sleep(2)
                print("You cannot tell if the man is dead or just weak")
                print()
                time.sleep(2)
                print("Do you head over to him?")
                looking = input("A)Yes or B)No ").lower()
                decided.append(looking)
                if looking == "a" or desk == "yes" or desk == "y":
                    print("You head over and inspect, the man is clearly about to die")
                    time.sleep(2)
                else:
                    print("You decided not to bother, he is dead either way")
            elif hdesk == "esc" or hdesk == "escape":
                print("You decided to exit the game")
                saves()
            else:
                interrogation()
    # the guard hp is placed back to original so that there can be other fights occuring in other rooms
    if guardhp <= 0:
        guardhp += 30
    elif look == "escape" or look == "esc":
        print("You decided to exit the game")
        saves()
    else:
        pass
    # once this room has been completed the player is given an option of rooms to visit again
    print("--Decision--")
    print("Where do you want to go?")
    print()
    print("Do you go:")
    print("A)Guards office")
    print("B)Armoury")
    print("C)The door")
    # user enters the place decided on
    d = input().lower()
    if d == "a" or d == "guards office":
        decided.append(d)
        guardsofficecheck()
    elif d == "b" or d == "armoury":
        decided.append(d)
        armouryCheck()
    elif d == "c" or d == "door":
        decided.append(d)
        Escape()
    elif d == "esc" or d == "escape":
        print("You decided to exit the game")
        saves()
    else:
        # if the user enters an incorrect key here, they will be give help
        print("--Help--")
        print("Please choose where you want to go")
        nd = input("A)Guards office B)Armoury C)Door ").lower()
        # if the choice is a then send the user to guards office etc
        if nd == "a" or nd == "guards office":
            # decisions are saved
            decided.append(nd)
            # sent to the next room
            guardsofficecheck()
        elif nd == "b" or nd == "armoury":
            decided.append(nd)
            armouryCheck()
        elif nd == "c" or nd == "door":
            decided.append(nd)
            Escape()
        elif nd == "esc" or nd == "escape":
            print("You decided to exit the game")
            saves()
        else:
            # if the user has not decided they re-do the room
            interrogation()


# the guards office has a checking function to check if there is a key in the player's inventory
def guardsofficecheck():
    room.append("guardsofficecheck()")
    # here check for the key
    ch_Keys = False
    for objects in iteminv:
        if objects['name'] == "Keys":
            ch_Keys = True
    # if there is a key
    if ch_Keys == True:
        print("You get to the guards office")
        time.sleep(2)
        print("You already have the keys in your inventory")
        print()
        time.sleep(2)
        print("--Decision--")
        print("Do you go:")
        print("A)Armoury room")
        print("B)Interrogation room")
        d = input().lower()
        if d == "a" or d == "armoury":
            decided.append(d)
            armouryCheck()
        elif d == "b" or d == "interrogation":
            decided.append(d)
            interrogation()
        elif d == "escape" or d == "esc":
            print("You decided to leave the game")
            saves()
        else:
            print("--Help--")
            print("Do you want to go to the armoury or the interrogation room")
            print("Type out the name or, type A or B")
            print()
            time.sleep(2)
            guardsofficecheck()
    else:
        # send player to guards office function if no key
        guardsoffice()


def guardsoffice():
    room.append("guardsoffice()")
    print("---Guard-Office---")
    print()
    time.sleep(2)
    print("You get to the guards office")
    x = importantdecide[1]
    print()
    time.sleep(1)
    global guardhp
    global playerhp
    h_gun_ = False
    h_knife_ = False
    h_bomb_ = False
    h_shiv_ = False
    if x == "a" or x == "b":
        x = random.randint(0, 9)
        if x <= 4:
            print("A guard is in the room")
            time.sleep(2)
            print("He sees you!")
            for objects in inv:
                if objects['name'] == "hand-gun":
                    h_gun_ = True
                else:
                    if objects['name'] == "knife":
                        h_knife_ = True
                    else:
                        if objects['name'] == "gas-bomb":
                            h_bomb_ = True
                        else:
                            h_shiv_ = True
            if h_gun_ == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        print("You find a key in the room")
                        for objects in items:
                            if objects['name'] == "Keys":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                        break
                    else:
                        playerhp -= 5
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use your gun")
                        print("You shoot the guard")
                        print()
                        guardhp -= 12
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_knife_ == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        print("You find a key in the room")
                        for objects in items:
                            if objects['name'] == "Keys":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                        break
                    else:
                        playerhp -= 5
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You stab the guard")
                        print()
                        guardhp -= 8
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_bomb_ == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        print("You find a key in the room")
                        for objects in items:
                            if objects['name'] == "Keys":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                        break
                    else:
                        playerhp -= 2
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use the gas bomb")
                        print("You throw it to the guard")
                        print()
                        guardhp -= 5
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            elif h_shiv_ == True:
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        print("You find a key in the room")
                        for objects in items:
                            if objects['name'] == "Keys":
                                iteminv.append(objects)
                                print("--You have", inv, iteminv, "in your inventory--")
                                print()
                                time.sleep(2)
                                break
                        break
                    else:
                        playerhp -= 2
                        print("You get hit ", playerhp, " is your current hp")
                        print()
                        time.sleep(2)
                        print("You use your shiv")
                        print("You stab the guard")
                        print()
                        guardhp -= 5
                        print("The guard's hp is now ", guardhp)
                        print()
                        time.sleep(2)
            # check if they have a weapon if not then use shiv else use the weapon
        else:
            # if there is no guard then the user is able to look around
            print("No one is inside the office")
            print()
            time.sleep(2)
            # decision to look around
            looking = input("A) Look around B) Just grab the keys ").lower()
            decided.append(looking)
            if looking == "a":
                print("There is a large desk in the center of the room")
                time.sleep(1)
                print("You open the desk")
                print("You find the files of every prisoner")
                print("and a few german plans they took from you")
                time.sleep(2)
                print("You have no space to carry files with you")
                print("Do you destroy them?")
                # decision to destroy files
                d = input("A)Yes or B)No ").lower()
                decided.append(d)
                if d == "a":
                    print("You burn the files in the fire place")
                    print()
                    time.sleep(2)
                elif d == "esc" or d == "escape":
                    print("You decided to leave the game")
                    saves()
                else:
                    print("You place them back where you found them")
            elif looking == "esc" or looking == "escape":
                print("You decided to leave the game")
                saves()
            else:
                print("You want to leave quickly")
            print("You look around and there is a key on the desk")
            print()
            time.sleep(2)
            print("You grab the key")
            print()
            time.sleep(3)
            for objects in items:
                # adding the key into the user's inventory
                if objects['name'] == "Keys":
                    iteminv.append(objects)
                    print("--You have", inv, iteminv, "in your inventory--")
                    print()
                    time.sleep(2)
                    break
    elif x == "c":
        print("The guard is sleeping")
        print("You attempt to grab the keys on the shelf")
        x = random.randint(0, 9)
        if x <= 4:
            print("The guard wakes up ")
            print()
            time.sleep(2)
            print("You quickly hide below the desk")
            x = random.randint(0, 9)
            if x <= 4:
                print("He notices you")
                print("You make him fall over and he snaps his neck")
                time.sleep(2)
                for objects in items:
                    if objects['name'] == "Keys":
                        iteminv.append(objects)
                        print("--You have", inv, iteminv, "in your inventory--")
                        print()
                        time.sleep(2)
                        break
            else:
                print("He doesn't notice you")
                time.sleep(2)
                print("You wait until he falls asleep again")
                time.sleep(3)
                for objects in items:
                    if objects['name'] == "Keys":
                        iteminv.append(objects)
                        print("--You have", inv, iteminv, "in your inventory--")
                        print()
                        time.sleep(2)
                        break
        else:
            for objects in items:
                    if objects['name'] == "Keys":
                        iteminv.append(objects)
                        print("--You have", inv, iteminv, "in your inventory--")
                        print()
                        time.sleep(2)
                        break
        time.sleep(2)

    if guardhp <= 0:
        guardhp += 30
    else:
        pass
    print("--Decision--")
    print()
    print("Do you go:")
    print("A)Armoury")
    print("B)Interrogation room")
    d = input().lower()
    if d == "a" or d == "armoury":
        decided.append(d)
        armouryCheck()
    elif d == "b" or d == "interrogation":
        decided.append(d)
        interrogation()
    elif d == "esc" or d == "escape":
        print("You have decided to exit the game")
        saves()
    else:
        print("--Help--")
        print("Please enter A or B")
        guardsofficecheck()


# here we check if the user has already gathered a weapon
def armouryCheck():
    room.append("armouryCheck()")
    ch_gun = False
    ch_knife = False
    ch_bomb = False
    for objects in inv:
        if objects['name'] == "hand-gun":
            ch_gun = True
        else:
            if objects['name'] == "knife":
                ch_knife = True
            else:
                if objects['name'] == "gas-bomb":
                    ch_bomb = True
    # if the player has a weapon in the inventory
    if ch_gun == True:
        print("--Armoury--")
        print()
        time.sleep(2)
        print("You get to the armoury")
        time.sleep(2)
        print("You already have a gun in your inventory")
        time.sleep(2)
        print("--Decision--")
        print("Do you go:")
        print("A)Guards office")
        print("B)Interrogation room")
        d = input().lower()
        if d == "a":
            decided.append(d)
            guardsofficecheck()
        elif d == "b":
            decided.append(d)
            interrogation()
        elif d == "esc" or d == "escape":
            print("You decided to leave the game")
            saves()
        if d == "help" or d == "h":
            print()
            print("--Help--")
            print("Choose A)guards office B)interrogation")
            armouryCheck()
    elif ch_knife == True:
        print("--Armoury--")
        print()
        time.sleep(2)
        print("You get to the armoury")
        time.sleep(2)
        print("You already have a knife in your inventory")
        time.sleep(2)
        print("--Decision--")
        print("Do you go:")
        print("A)Guards office")
        print("B)Interrogation room")
        d = input().lower()
        if d == "a":
            decided.append(d)
            guardsofficecheck()
        elif d == "b":
            decided.append(d)
            interrogation()
        elif d == "esc" or d == "escape":
            print("You decided to leave the game")
            saves()
        elif d == "help" or d == "h":
            print()
            print("--Help--")
            print("Choose A)guards office B)interrogation")
            armouryCheck()
    elif ch_bomb == True:
        print("--Armoury--")
        print()
        time.sleep(2)
        print("You get to the armoury")
        time.sleep(2)
        print("You already have gas bombs in your inventory")
        time.sleep(2)
        print("--Decision--")
        print("Do you go:")
        print("A)Guards office")
        print("B)Interrogation room")
        d = input().lower()
        if d == "a":
            decided.append(d)
            guardsofficecheck()
        elif d == "b":
            decided.append(d)
            interrogation()
        elif d == "esc" or d == "escape":
            print("You decided to leave the game")
            saves()
        elif d == "help" or d == "h":
            print()
            print("--Help--")
            print("Choose A)guards office B)interrogation")
            armouryCheck()
    else:
        # send them to the armoury function
        armoury()


def armoury():
    room.append("armoury()")
    print("--Armoury--")
    print()
    time.sleep(2)
    print("Do you look around?")
    # you can decide to look around and find a weapon or just leave the room
    look = input("A)Yes or B)No ").lower()
    if look == "a" or look == "yes" or look == "y":
        decided.append(look)
        print("There are several weapons you can grab one")
        print()
        time.sleep(2)
        print("What do you decide to grab?")
        print()
        time.sleep(0.5)
        weapon = input("A 1)hand gun, 2)knife or 3) gas bombs? ").lower()
        print()
        for objects in items:
            # adding the weapon into the  inventory
            if weapon == "1":
                if objects['name'] == "hand-gun":
                    inv.append(objects)
                    print("--You have", inv, iteminv, "in your inventory--")
                    print()
                    time.sleep(2)
                    break
            elif weapon == "2":
                if objects['name'] == "knife":
                    inv.append(objects)
                    print("--You have", inv, iteminv, "in your inventory--")
                    print()
                    time.sleep(2)
                    break
            elif weapon == "3":
                if objects['name'] == "gas-bomb":
                    inv.append(objects)
                    print("Along side this there are gas masks")
                    print("--You have", inv, iteminv, "in your inventory--")
                    print()
                    time.sleep(2)
                    break
            elif weapon == "h" or weapon == "help":
                print()
                print("--Help--")
                print("Choose a weapon")
                print("Or decide to not look around")
                print("1)Hand gun 2)Knife or 3)Gas bomb")
                armoury()
            elif weapon == "esc" or weapon == "escape":
                print("You chose to leave the game")
                saves()
            else:
                print("Error")
                armoury()
    # if the player decides to not look around
    elif look == "b" or look == "no" or look == "n":
        print("You did not gather anything")
        time.sleep(2)
        decided.append(look)
    elif look == "esc" or look == "escape":
        print("You chose to leave the game")
        saves()
    elif look == "h" or look == "help":
        print()
        print("--Help--")
        print("If you want to look around this room type yes")
        print("or no if you do not want to")
        armoury()
    else:
        armoury()
    print("--Decision--")
    print()
    time.sleep(2)
    print("Do you go:")
    print("A)Guards office")
    print("B)Interrogation room")
    d = input().lower()
    if d == "a" or d == "guards office":
        decided.append(d)
        guardsofficecheck()
    elif d == "b" or d == "interrogation":
        decided.append(d)
        interrogation()
    elif d == "esc" or d == "escape":
        print("You chose to leave the game")
        saves()
    else:
        print("--Help--")
        print("Please decide on where to go by typing A or B")
        time.sleep(2)
        print("--Decision--")
        print()
        time.sleep(2)
        print("Do you go:")
        print("A)Guards office")
        print("B)Interrogation room")
        d = input().lower()
        if d == "a" or d == "guards office":
            decided.append(d)
            guardsofficecheck()
        elif d == "b" or d == "interrogation":
            decided.append(d)
            interrogation()
        elif d == "esc" or d == "escape":
            print("You chose to leave the game")
            saves()
        else:
            armouryCheck()

# Part C ###############################################################################################################
# player decides on what room to go to first here
def insiderooms():
    room.append("insiderooms()")
    print("--Decision--")
    print()
    time.sleep(2)
    d = input("Do you go A)straight, B) left or C)back the opposite way? ").lower()
    if d == "a":
        roomdecided.append(d)
        armoury()
    elif d == "b":
        roomdecided.append(d)
        guardsoffice()
    elif d == "c":
        roomdecided.append(d)
        interrogation()
    elif d == "help" or d == "h":
        print()
        print("--Help--")
        print("Type in A)Straight, B)Left or C)The opposite way")
        print()
        insiderooms()
    elif d == "esc" or d == "escape":
        print("You decided to leave the game")
        saves()
    else:
        insiderooms()


# this is where the player is starting the escape
def _escape():
    room.append("Escape()")
    print("---Scene4---")
    print()
    time.sleep(2)
    print("You attempt unlocking the cell door")
    y = importantdecide[0]
    x = random.randint(0, 9)
    if x <= 4:
        # first guard is encountered
        print("You have been seen by the guard")
        print()
        time.sleep(2)
        for objects in inv:
            if objects['name'] == "shiv":
                global guardhp
                global playerhp
                while guardhp > playerhp and guardhp != 0 or playerhp > guardhp and playerhp != 0:
                    if playerhp <= 0:
                        print("You have died")
                        print()
                        sys.exit()
                    elif guardhp <= 0:
                        print("You killed the guard")
                        print()
                        time.sleep(2)
                        break
                    print("You stab the guard")
                    print()
                    guardhp -= 5
                    print("The guard's hp is now ", guardhp)
                    print()
                    time.sleep(2)
                    playerhp -= 2
                    print("You get hit! ", playerhp, " is your current hp")
                    print()
                    time.sleep(2)
                break
    else:
        print("You unlock the cell door")
    print()
    time.sleep(2)
    print("You look around")
    print()
    time.sleep(2)
    if y == "yes" or y =="y":
        print("Frank: You can walk out. I don't see any guards")
        print()
        time.sleep(2)
        print("You open Franks cell")
        print()
        time.sleep(2)
        print("Frank: I know the armoury is straight on,")
        time.sleep(0.5)
        print("the guards office is on the left and ")
        time.sleep(0.5)
        print("the opposite way is the direction they took you to be interrogated")
        print()
        time.sleep(2)
        insiderooms()
    else:
        print("You walk out and attempt to find the way out")
        time.sleep(2)
        print("You can either go straight, turn left, or head the opposite way")
        print()
        time.sleep(2)
    # guard hp is reset
    if guardhp <= 0:
        guardhp += 30
    else:
        pass
    insiderooms()


# Part B ###############################################################################################################
# deciding on the time of day or night to leave
def choice_3():
    room.append("choice_3()")
    print("--Decision--")
    print()
    time.sleep(2)
    print("Do you")
    print("A) Attempt an early escape")
    time.sleep(0.5)
    print("B) Escape during the day time at the guards lunch time")
    time.sleep(0.5)
    print("C) Escape at night")
    print()
    time.sleep(2)
    decide = input("Choose A, B or C: ").lower()
    if decide == "h" or decide == "help":
        print()
        print("--Help--")
        print("Type in A)Early , B)Day-time or C)Midnight")
        print()
        time.sleep(2)
        choice_3()
    elif decide == "esc" or decide == "escape":
        print("You decided to leave the game")
        saves()
    elif decide == "a" or decide == "b" or decide == "c":
        print()
        print("--You have chosen ", decide, " as the time of escape--")
        print()
        time.sleep(2)
        importantdecide.append(decide)
    else:
        choice_3()
    _escape()


# Here the user is given their inventory and finds a way to open the cell
def Theplan():
    x = importantdecide[0]
    room.append("Theplan()")
    print("--The Plan--")
    print()
    time.sleep(2)
    if x == "yes" or x == "y":
        print("Frank: So, in this room you have three cracks on different sides of the room")
        print()
        time.sleep(2)
        print("You have a look within these three cracks and discover")
        time.sleep(0.5)
        print("A shiv, a small amount of twigs that can be sharpened to become")
        time.sleep(0.5)
        print("lock picks, and a dead rat that is covered in small insects")
        time.sleep(2)
        print("eating away at its old carcass")
        print()
        time.sleep(2)
        print("Frank: Now that is gross")
        print()
        print("--You have", inv, "in your inventory--")
        print()
        time.sleep(2)
        print("Frank: So the guards come to check on us every 2 - 3 hours")
        print()
        time.sleep(2)
        print("Depending on the day we will either have early in the morning")
        print()
        print("During their lunch hour, or just after midnight,")
        print()
        print("When the guard sometimes falls asleep")
        print()
        time.sleep(3)
        print("When should we do this and what should we do?")
        print()
        time.sleep(2)
    elif x == "no" or x == "n":
        print("You look around and find several cracks in the walls,")
        time.sleep(0.5)
        print("You see that one of them has a pre-made shiv")
        print()
        time.sleep(2)
        print("Another crack is filled with twigs")
        print()
        time.sleep(3)
        print("You think to yourself and think that you could probably sharpen")
        time.sleep(0.5)
        print("the twigs to then use for picking the cell lock")
        print()
        time.sleep(4)
        print("--You have", inv, "in your inventory--")
        print()
        time.sleep(2)
        print("When will you escape?")
        print()
        time.sleep(2)
    choice_3()


# the player decides on whether or not to escape with frank
def choice_2():
    room.append("choice_2()")
    print("--Decision--")
    print()
    time.sleep(2)
    talk = input("Yes or No? ").lower()
    if talk == "h" or talk == "help":
        print()
        print("--Help--")
        print("Type in Yes or No")
        print()
        print("Or you can type in exit or esc to leave the game")
        time.sleep(2)
        print()
        choice_2()
    elif talk == "escape" or talk == "esc":
        print("You decided to leave the game")
        saves()
    else:
        print("You decided to say", talk)
        print()
        time.sleep(2)
    if talk == "no" or talk == "n":
        print("Why not?, I don't wat to die here.")
        print()
        time.sleep(1)
        print("Please!!")
        print()
        time.sleep(2)
        print("Several german soldiers pass by...")
        print()
        time.sleep(2)
        print("Shut it you two or else!")
        print()
        time.sleep(2)
        print("You fall asleep")
        print()
        time.sleep(4)
        importantdecide.append(talk)
    elif talk == "yes" or talk == "y":
        print("Wonderful! Thank you so much!")
        print()
        time.sleep(2)
        print("Several german soldiers pass by...")
        print()
        time.sleep(2)
        print("Shut it you two or else!")
        print()
        time.sleep(2)
        print("You both start thinking of a plan.")
        print()
        time.sleep(2)
        importantdecide.append(talk)
    else:
        choice_2()
    Theplan()


# here player meets frank
def Prisoncell():
    room.append("Prisoncell()")
    print("---Prison Cell---")
    print()
    time.sleep(2)
    print("In a dark poorly lit corner of a stone room a small")
    time.sleep(0.5)
    print("rat squealing and running around bites you, you wake up and look around")
    global playerhp
    playerhp -= 1
    print("--Health--")
    print("Your hp dropped and is now ", playerhp, "hp")
    time.sleep(2)
    print()
    print("Psst")
    time.sleep(3)
    print("Pssst")
    print()
    print("You say: What?")
    print()
    time.sleep(2)
    print("You're John Smith aren't you? My old cell mate used to be")
    time.sleep(0.5)
    print(" in that cell before you know, *slice*.")
    print()
    time.sleep(4)
    print("You say: And?")
    print()
    time.sleep(1)
    print("Well he was thinking of a way out of here before hand and")
    time.sleep(0.5)
    print("I know he has lots of hidden things in that cell of yours.")
    print()
    time.sleep(0.5)
    print("I'm Frank, a French reporter... I wondered if you would like to ")
    time.sleep(0.5)
    print("attempt to escape with me..")
    print()
    time.sleep(1)
    print("I know all the guard times and schedules the only problem ")
    time.sleep(0.5)
    print("is that I feel its best to fight in a team rather than alone")
    print()
    time.sleep(1)
    print("Will you help me escape, I don't want to die here!")
    print()
    time.sleep(2)
    choice_2()


# small choice of giving germans information
def choice_1():
    print("--Decision--")
    print()
    time.sleep(2)
    global playerhp
    room.append("choice_1()")
    talk = input("Will you tell them about any confidential information? Yes or No? ").lower()
    if talk == "h" or talk == "help":
        print()
        print("--Help--")
        time.sleep(1)
        print("Type in yes or no")
        print()
        print("Or you can type in escape or esc to leave the game")
        time.sleep(2)
        print()
        choice_1()
    elif talk == "escape" or talk == "esc":
        print("You decided to leave the game")
        time.sleep(2)
        print("You have not completed enough of the game to save")
        time.sleep(2)
        sys.exit()
    else:
        print("You said", talk)
        print()
        time.sleep(2)
    if talk == "no" or talk == "n":
        print("Well")
        print()
        time.sleep(2)
        print("That was the wrong choice")
        print()
        time.sleep(3)
        print("The German soldiers start to beat you up")
        playerhp -= 20
        print("--Health--")
        print("you hp dropped and is now ", playerhp, "hp")
        print()
        time.sleep(3)
        print("The pain is too much and you pass out...")
        print()
    elif talk == "yes" or talk == "y":
        print("There is a pause in the room")
        print()
        time.sleep(3)
        print("Thank you... for this key information")
        print()
        time.sleep(2)
        print("You get knocked out...")
        print("No hp is lost")
        print()
        time.sleep(2)
    else:
        print()
        print("--Help--")
        time.sleep(1)
        print("Type in yes or no")
        time.sleep(2)
        print()
        choice_1()
    decided.append(talk)
    Prisoncell()


# introduction to a german soldier and a small interrogation scene
def interrogation1():
    # this is the first scene in the prison / camp where you meet an ss soldier and are interrogated
    print("---Interrogation Room---")
    print()
    time.sleep(2)
    room.append("interrogation1()")
    print("Your face gets splashed by a large mass of water,")
    time.sleep(0.5)
    print(" waking you up with its sharp frozen temperature")
    print()
    time.sleep(2)
    print("Nice to see that you have joined us Mr.Smith")
    print()
    time.sleep(2)
    print("My name is Obergruppenfuhrer Blazgowitz")
    print("We have been following you for quite some time, ")
    time.sleep(0.5)
    print("and you have quite a bit of knowledge from both sides, wouldn't you say?")
    print()
    time.sleep(3)
    print("We aren't here to just hurt you, you see, you")
    time.sleep(0.5)
    print("have key information that the Reich finds important")
    print()
    time.sleep(3)
    print("Now I know our countries do not have much in common, ")
    time.sleep(0.5)
    print("but what we do have is a strong feel for ones information of the other")
    print()
    time.sleep(3)
    print("Would you care to elaborate on any thing your country may")
    time.sleep(0.5)
    print(" be planning in the future Mr.Smith?")
    time.sleep(3)
    print()
    choice_1()


# here player decides on the start of the game
def choosepath():
    global playerhp
    room.append("choosepath()")
    print("--Decision--")
    print()
    time.sleep(2)
    path = input("What'll you do?! Fight, Hide or Die? ").lower()
    if path == "h" or path == "help":
        print()
        print("--Help--")
        print("Type in fight hide or die")
        print()
        print("Or you can type in exit or esc to leave the game")
        time.sleep(2)
        print()
        choosepath()
    elif path == "escape" or path == "esc":
        print("You decided to leave the game")
        time.sleep(2)
        print("You have not completed enough of the game to save")
        time.sleep(2)
        sys.exit()
    else:
        print()
        time.sleep(2)
    if path == "fight" or path == "f":
        decided.append(path)
        print("Do you ")
        fight = input("A)Look for something to hit them with B)Use fists ").lower()
        if fight == "h" or fight == "help":
            print()
            print("--Help--")
            print("Type in A or B")
            print()
            print("Or you can type in escape or esc to leave the game")
            time.sleep(2)
            print()
            choosepath()
        elif fight == "escape" or fight == "esc":
            print("You decided to leave the game")
            time.sleep(2)
            print("You have not completed enough of the gae to save")
            time.sleep(2)
            sys.exit()
        else:
            print()
            time.sleep(2)
        if fight == "a" or fight == "look":
            print("You find a broom")
            time.sleep(2)
            print("You attempt to hit the soldier")
            time.sleep(2)
            print("The soldiers grab you and beat you up")
            playerhp -= 25
            print("--Health--")
            print("Your hp dropped and is now ", playerhp, "hp")
            time.sleep(2)
            print()
        elif fight == "b" or fight == "fists":
            print("You have been grabbed")
            playerhp -= 20
            print("--Health--")
            print("Your hp dropped and is now ", playerhp, "hp")
            time.sleep(2)
            print()
        elif fight != "a" or fight != "looks" or fight != "b" or fight != "fists":
            choosepath()
        interrogation1()
    elif path == "hide" or path == "hi":
        decided.append(path)
        print("The door breaks")
        print("The guards look around")
        time.sleep(2)
        print()
        print("They find you and several German men grab you and arrest you.")
        time.sleep(2)
        print()
        interrogation1()
    elif path == "die" or path == "d":
        print("You have died")
        sys.exit()
    else:
        choosepath()


# introduction to game ie the start of the game
def intro():
    # this is  scene 1 where the user will get captured #
    print("---Introduction---")
    print()
    time.sleep(2)
    room.append("intro()")
    print("You wake up and your flight back home is in a couple of hours")
    time.sleep(0.5)
    print("You hear a set of loud violent knocks on the front door!")
    time.sleep(0.5)
    print("You have seconds to destroy all the information you have gathered on the Germans")
    time.sleep(2)
    print()
    choosepath()


# Part A #############################################################################################################
# the start up of the game player gives the name and is given helpful information
def start_up():
    print("--Start Up--")
    print()
    time.sleep(2)
    print("Hello")
    print("")
    time.sleep(2)
    print("Welcome to NaziEscape")
    print("")
    time.sleep(2)
    global playerinfo
    # players name is given
    playerinfo = input("Please enter your name: ").upper()
    print("")
    if playerinfo == "":
        print("Please enter a name")
        print()
        time.sleep(2)
        start_up()
    else:
        pass
    time.sleep(2)
    print("Hello ", playerinfo, "!")
    print()
    time.sleep(2)
    print("If you need help, type (--h--) when you get given a decision to make")
    time.sleep(2)
    print("If you want to save and quit the game, type (--esc--) when given a decision to make")
    time.sleep(2)
    print("When you are ready type in Start")
    start = input("Ready: ").lower()
    if start == "start" or start == "st":
        intro()
    elif start == "help" or start == "h":
        print("To start, type in:")
        print("start")
        print("or")
        print("st")
        s = input().lower()
        if s == "st" or s == "start":
            intro()
        else:
            start_up()
    else:
        start_up()


start_up()
