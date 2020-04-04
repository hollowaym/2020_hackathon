# -*- coding: utf-8 -*-

#Strings that represent potential player input

WAIT = "Wait"
CLIMB = "Climb"
CHECK = "Check"

#Initialization of variables

player_available_verbs = [WAIT] #Stores dynamic verbs available for player. 

# Narrator actions

def process_player_input(theInput):
    return

def describe_situation():
    return

def list_verbs(theVerbs):
    print("You could:") 
    print(*theVerbs, sep = "\n") 
   
# Player verbs

def player_wait():
    return
def player_climb_mountain():   
    return
def player_check():
    return
# Main game loop

running = True
while running: 
    
    describe_situation()
    list_verbs(player_available_verbs)
    player_input = input ("What do you do? \n") 
    process_player_input(player_input)
    
verbs = {
 CLIMB : player_climb_mountain,
 WAIT : player_wait,
 CHECK : player_check
}