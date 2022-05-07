import random
def roll_die():
    # randomly rolls a six-sided die
    rng = random.random()
    random.seed(rng)
    dice_roll=random.randint(1,6)
    return dice_roll

def display_state(update):
    # displays the initial state of the players
    update=['* ','_ ','_ ','_ ','_ ','_ ','_ ','_ ']
    print("players begin in the starting position")
    print("*"*36)
    print(''.join(update))
    print("*"*36)
    return update

def update_position(rounds,roll_result_x,roll_result_o, update):
    # updates the position of the players based on the roll of their die
    if rounds%2!=0 and sum(roll_result_x) in range(0,len(update)):
        update[sum(roll_result_x)]='x '
        update[sum(roll_result_x[:-1])] = '- '
    elif rounds%2==0 and sum(roll_result_o) in range(0,len(update)):
        update[sum(roll_result_o)]='o '
        update[sum(roll_result_o[:-1])] = '- '
    elif rounds%2!=0 and sum(roll_result_x)==sum(roll_result_o) and sum(roll_result_x) in range(0,len(update)): # Here we check if kicked
        update[0]='o '
        update[sum(roll_result_x)] = 'x '
        update[sum(roll_result_x[:-1])] = '- '
        print("x kicked the rival!")
        roll_result_o.clear() # Clear o since it has been kicked
    elif rounds%2==0 and sum(roll_result_o)==sum(roll_result_x) and sum(roll_result_o) in range(0,len(update)): # Here we check if kicked
        update[0]='x '
        update[sum(roll_result_o)] = 'o '
        update[sum(roll_result_o[:-1])] = '- '
        print("o kicked the rival!")
        roll_result_x.clear() # Clear x since it has been kicked
    return update
   
def check_game_over(update):
    # shows who won
    if update[7]=='x ': # Aesthetic chenges
        print("player x has won!")
    if update[7]=='o ':
        print("player o has won!")
    return 0

def opponent(rounds,player_x,player_o):
    # makes sure one player goes after the other
    rounds=rounds
    if rounds%2==0:
        input("player o press enter to roll")
        print("player o rolled a ",player_o)
    else:
        input("player x press enter to roll")
        print("player x rolled a ",player_x)
    return 0
  
def main():
    rounds=1
    roll_result_x=[]
    roll_result_o=[]
    update=['* ','- ','- ','- ','- ','- ','- ','- ']
    display_state(update)
    while update[7] != 'x ' and update[7] != 'o ':
        player_x = roll_die()
        player_o = roll_die() # Roll dicex
        if rounds%2!=0:
            if (sum(roll_result_x) + player_x) in range(0,len(update)):
                roll_result_x.append(player_x) # Roll dice depending on player
        if rounds%2==0:
            if (sum(roll_result_o) + player_o) in range(0,len(update)):
                roll_result_o.append(player_o) # Roll dice depending on player
        opponent(rounds,player_x,player_o)
        print("*"*36)
        update_position(rounds,roll_result_x,roll_result_o,update)
        print("update:", ''.join(update))
        print("*"*36)
        
        rounds=rounds+1
        
    check_game_over(update)



if __name__ == "__main__":
        main()