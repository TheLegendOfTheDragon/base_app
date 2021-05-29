# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
import simplegui
# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print ("invalid name"),name

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "invalid number",number
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print ("Player chooses ") + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print ("Computer chooses ") + comp_choice
    # compute difference of comp_number and player_number modulo five
    value = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if (value==1) or (value==2):
        print ("Computer wins!")
    elif (value==3) or (value==4):
        print ("Player wins!")
    elif (value==0):
        print( "Player and computer tie!")
    else:
        print ("Invalid value"), value
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

canvas_width = 250
canvas_height = 300

player_number = 0
comp_number = 0
value = 0 #value represents game status 0 means it's a tie
games_played = 0
games_won = 0
games_lost = 0
games_tied = 0
rock = simplegui.load_image('http://2.bp.blogspot.com/-nlKaPBPlsVY/VCCoy1SmI6I/AAAAAAAABZc/BmG2ceJx80s/s1600/rock.png')
paper = simplegui.load_image('http://2.bp.blogspot.com/-BypROdnByMo/VCCoy9UExTI/AAAAAAAABZY/g7eCRxM1qxc/s1600/paper.png')
scissors = simplegui.load_image('http://2.bp.blogspot.com/-prOPXhff7Ys/VCCozfNQiBI/AAAAAAAABZg/3nwG1uI4ZsA/s1600/scissors.png')
lizard = simplegui.load_image('http://3.bp.blogspot.com/-tpRtGTJN2Qg/VCCoy7PhNkI/AAAAAAAABZ4/_5XbOJ3N9ps/s1600/lizard.png')
spock = simplegui.load_image('http://3.bp.blogspot.com/-AevWvaP-QHA/VCCoznhP_ZI/AAAAAAAABZk/HlFxZqFP_GI/s1600/spock.png')
leftarrow = simplegui.load_image('http://1.bp.blogspot.com/-z2looRXTiCo/VCCs_sSPCzI/AAAAAAAABaE/ZZCBfyxeTJE/s1600/leftarrow.png')
rightarrow = simplegui.load_image('http://4.bp.blogspot.com/-UJT31ftL60s/VCCs_jR1nxI/AAAAAAAABaI/q5r0yY8OROY/s1600/rightarrow.png')
noarrow = simplegui.load_image('')
images = [rock,spock,paper,lizard,scissors]
def draw_game_status(canvas):
    global value,player_number,comp_number,games_played,games_won,games_lost,games_tied,images,rock,lizard
    #print out player's choice
    message = "You chose '" + number_to_name(player_number) + "'"
    point = (10, 20) # The point is the lower left-hand corner of the text
    text_size = 15
    color = "White"
    canvas.draw_text(message, point, text_size, color)
    #print out computer's choise
    message = "Computer chose '" + number_to_name(comp_number) + "'"
    point = (10, 40) # The point is the lower left-hand corner of the text
    text_size = 15
    color = "White"
    canvas.draw_text(message, point, text_size, color)
    #print game rule
    if ((player_number == 0) and (comp_number == 1) or \
        (player_number == 1) and (comp_number == 0)):
        message = "Spock vaporizes rock!"
    elif ((player_number == 0) and (comp_number == 2) or \
        (player_number == 2) and (comp_number == 0)):
        message = "paper covers rock!"
    elif ((player_number == 0) and (comp_number == 3) or \
        (player_number == 3) and (comp_number == 0)):
        message = "rock crushes lizard!"
    elif ((player_number == 0) and (comp_number == 4) or \
        (player_number == 4) and (comp_number == 0)):
        message = "rock crushes scissors!"
    elif ((player_number == 1) and (comp_number == 2) or \
        (player_number == 2) and (comp_number == 1)):
        message = "paper disproves Spock!"
    elif ((player_number == 1) and (comp_number == 3) or \
        (player_number == 3) and (comp_number == 1)):
        message = "lizard poisons Spock!"
    elif ((player_number == 1) and (comp_number == 4) or \
        (player_number == 4) and (comp_number == 1)):
        message = "Spock smashes scissors!"	
    elif ((player_number == 2) and (comp_number == 3) or \
        (player_number == 3) and (comp_number == 2)):
        message = "lizard eats paper!"
    elif ((player_number == 2) and (comp_number == 4) or \
        (player_number == 4) and (comp_number == 2)):
        message = "scissors cut paper!"
    elif ((player_number == 3) and (comp_number == 4) or \
        (player_number == 4) and (comp_number == 3)):
        message = "scissors decapitate lizard!"
    else:
        message = number_to_name(player_number) + " ties with " + number_to_name(comp_number) + "!"
    color = "#FFFF00"
    point = (10,60)
    canvas.draw_text(message, point, text_size, color)
    #print out game status, like who wins or a tie
    if value in [1,2]:
        message = "You lose!"
        color = "Red"
        arrow = leftarrow
    elif value in [3,4]:
        message = "You win!"
        color = "Lime"
        arrow = rightarrow
    else:
        message = "You and computer tie!"
        color = "White"
        arrow = noarrow
    point = (10, 80) # The point is the lower left-hand corner of the text
    text_size = 15
    canvas.draw_text(message, point, text_size, color)

    #print number of games played and games won
    message = "You won " + str(games_won) + " out of " + str(games_played) + " games."
    point = (10, 120) # The point is the lower left-hand corner of the text
    text_size = 15
    color = "#8888FF"
    canvas.draw_text(message, point, text_size, color)
    message = "You lost " + str(games_lost) + " out of " + str(games_played) + " games."
    point = (10, 140) # The point is the lower left-hand corner of the text
    canvas.draw_text(message, point, text_size, color)
    message = "You tied " + str(games_tied) + " out of " + str(games_played) + " games."
    point = (10, 160) # The point is the lower left-hand corner of the text
    canvas.draw_text(message, point, text_size, color)
    #show game's art
    #canvas.draw_image(images[player_number], (64/2, 65/2), (64, 65), (64/2, 65/2), (64, 65))
    canvas.draw_image(images[player_number], (64/2, 65/2), (64, 65), (10+64/2, 200 + 65/2), (64, 65))
    canvas.draw_image(images[comp_number], (64/2, 65/2), (64, 65), (130+64/2, 200 + 65/2), (64, 65))
    canvas.draw_image(arrow, (64/2, 65/2), (64, 65), (70+64/2, 200 + 65/2), (64, 65))
    
    #You and Computer indicators
    message = "     You                     Computer"
    color = "#FFFFFF"
    point = (10,280)
    canvas.draw_text(message, point, text_size, color)
def play_computer():
    global comp_number,value,player_number,games_played,games_won,games_lost,games_tied
    comp_number = random.randrange(0,5)
    value = (comp_number - player_number) % 5
    games_played += 1
    if value in [3,4]:
        games_won += 1
    elif value in [1,2]:
        games_lost += 1
    else:
        games_tied += 1
        
def rock_button():
    global player_number
    player_number = 0
    play_computer()
    
def Spock_button():
    global player_number
    player_number = 1
    play_computer()
    
def paper_button():
    global player_number
    player_number = 2
    play_computer()
    
def lizard_button():
    global player_number
    player_number = 3
    play_computer()
    
def scissors_button():
    global player_number
    player_number = 4
    play_computer()
frame = simplegui.create_frame("rock paper scissors lizard Spock", canvas_width, canvas_height) 

# Register Event Handlers

frame.add_button("rock", rock_button, 60)
frame.add_button("paper", paper_button, 60)
frame.add_button("scissors", scissors_button, 60)
frame.add_button("lizard", lizard_button, 60)
frame.add_button("Spock", Spock_button, 60)
#images = [rock,spock,paper,lizard,scissors]
frame.set_draw_handler(draw_game_status)

frame.start()