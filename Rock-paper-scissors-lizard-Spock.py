# Flavio Barros

# helper functions

def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return False # You can use the False later



def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return False # You can use the False later
  

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    print # Nothing to print = blank line
    import random
    print 'Player chooses', player_choice
   
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0,5)
    
    computer_choice = number_to_name(comp_number)
    print 'Computer chooses', computer_choice
   
    diff = (comp_number - player_number) % 5
  
    if diff == 0:
        print "Player and computer tie!"
    elif diff <= 2:
        print 'Computer wins!'
    else: 
        print 'Player wins!'
 
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





