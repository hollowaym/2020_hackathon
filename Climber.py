# -*- coding: utf-8 -*-

from datetime import time
from datetime import timedelta 
from datetime import datetime

#Strings player inputs

WAIT = "Wait"
CLIMB = "Climb"
CHECK = "Check"
ROLL = "Roll"

#Strings world situations

ALIVE = "You are alive"

#Strings narrator outputs


#Initialization of variables

player_available_verbs = [WAIT, CLIMB, CHECK] #dynamic verbs available for player. 
player_situation = [ALIVE] #dynamic state of player/world
current_time = datetime(2020, 4, 4, 12, 00) #should move remaining (below) variables into datastructure
percent_up_mountain = 0 #out of 100
player_energy = 100
player_health = 100
turn_counter = 0

# World actions

def adjust_player_energy(theEnergyAmount):
    global player_energy
    player_energy = player_energy + theEnergyAmount
    if player_energy > 100:
        player_energy = 100
    if player_energy <= 0:
        health_rollover = player_energy * -1
        print(health_rollover)
        adjust_player_health(-health_rollover)
        player_energy = 0
        print("You feel exhausted.")
    return
    
def adjust_player_health(theHealthAmount):
    global player_health
    player_health = player_health + theHealthAmount
    if(theHealthAmount < 0):
        print("It hurts")
    if player_health > 100:
        player_health = 100
    return

def advance_time_by_minutes(theTimeAmount):
    global current_time
    current_time = current_time + timedelta(minutes=theTimeAmount)
    return

def advance_world():
    return 



# Narrator actions

def check_for_win(thePercent):
    if thePercent >= 100:
        thePercent = 100
        print("You've made it up the mountain. Now you are stuck.")
    return

def check_for_still_alive(theCurrentHealth):
    if theCurrentHealth > 0:
        return True
    else:
        return False

def process_player_input(theInput):
    print("\nYou attempt to " + theInput +":") 
    if (theInput in player_available_verbs) == False:
        print("but you spelled something wrong.")
        return False
    return True #Input was good

def describe_situation(theSituationList):
    print(*theSituationList, sep = ", ", end=".\n")
    return

def list_verbs(theVerbs):
    print(*theVerbs, sep = "\n") 
    return
   
# Player verbs

def player_wait():
    print("Some time passes.")
    advance_time_by_minutes(120)
    adjust_player_energy(30)
    adjust_player_health(7)
    return

def player_climb_mountain():   
    print("You make some progress climbing.")
    advance_time_by_minutes(120)
    adjust_player_energy(-30)
    global percent_up_mountain
    percent_up_mountain = percent_up_mountain + 10
    return

def player_check(): 
    print("The time is: " + str(current_time.time()))
    print("Your energy is: " + str(player_energy))
    print("Your health is: " + str(player_health))
    print("You are " + str(percent_up_mountain) + "% up the mountain")
    return

# Verb function list

verbs = {
 CLIMB : player_climb_mountain,
 WAIT : player_wait,
 CHECK : player_check
}

# System actions 

def process_action(theInput):
    do_verb = verbs[theInput] #potential arbitrary method exec? 
    do_verb()
    return


# Main game loop
# Method calls are prepended with manager
running = True
while running: 
    describe_situation(player_situation) # narrator
    print("You can:\n")
    list_verbs(player_available_verbs)  # narrator
    player_input = input ("\nWhat do you do? \n>")  
    player_input = player_input.capitalize()
    do_action = process_player_input(player_input) 
    if do_action:
        process_action(player_input) # system
    advance_world() # world
    check_for_win(percent_up_mountain) # narrator
    running = check_for_still_alive(player_health) # narrator
    turn_counter = turn_counter + 1
    print("----------="+ str(turn_counter) +"=----------")
    
print("----------=You=----------")
print("----------=Are=----------")
print(" ---------=Dead=---------")