import random

game_name="""  
██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
"""                                                                                                                     

player_choices="""
1-Rock
2-Paper
3-Scissor
"""

choices=[1,2,3]  #players will choose from the give list 'choices'.
opponent_score,player_score=0,0
opponents=["Alankrit","Anirban","Alok","Anurag","Kalash","Jack","Henry","Lusef","Mark","Joseph","Larry","Lita","Sophia","Jenne"]



########  Introductory part   #########
print(game_name)
print("Welcome you to the new version of the self developed game.....")
player_name=str(input("Please enter your Name -->"))
opponent_name=random.choice(opponents)
print("Your opponent is ",opponent_name)
print("\nRules:-\n\tDear ",player_name," You have to select among the choices that are listed below....")
print(player_choices)



#######  Here in this function the score will be evaluated.   #########
def score(a,b):
    global opponent_score,player_score
    if((a==1 and b==1) or (a==2 and b==2) or (a==3 and b==3)):
        print("Turn Draw\n")
        gaming_mode()
    elif(a==1):
        if(b==2):
            opponent_score+=2
            print("\n")
        if(b==3):
            player_score+= 2
            print("\n")
    elif(a==2):
        if(b==1):
            player_score+= 2
            print("\n")
        if(b==3):
            opponent_score+= 2
            print("\n")
    elif(a==3):
        if(b==1):
            opponent_score+= 2
            print("\n")
        if(b==2):
            player_score+= 2
            print("\n")
    else:
        print("Invalid  move, Please make a choice among the given only\n")
        

        
###########  Loop for asking the options.  ############
def gaming_mode():
    player=int(input(player_name+" --> "))
    while(player<1 or player>3):   #Checking that whether the input is either 1/2/3 or not.
        player=int(input("Invalid move!\n"+player_name+" --> "))
    computer=random.choice(choices)
    print(opponent_name," --> ",computer)
    score(player,computer)



######### Calculation of who is the winner ############
def winner():
    print("\nBoth Played Well\n")
    print(player_name,"'s score is --> ",player_score)
    print(opponent_name,"'s score is --> ",opponent_score)
    if(opponent_score>player_score):
        print("The winner is ",opponent_name," leading with ",opponent_score-player_score," points, Congratulation.")
    elif(opponent_score<player_score):
        print("The winner is ",player_name," leading with ",player_score-opponent_score," points, Congratulation.")
    print("""
  _____ _              _         ___          ___ _           _           
 |_   _| |_  __ _ _ _ | |__ ___ | __|__ _ _  | _ \ |__ _ _  _(_)_ _  __ _ 
   | | | ' \/ _` | ' \| / /(_-< | _/ _ \ '_| |  _/ / _` | || | | ' \/ _` |
   |_| |_||_\__,_|_||_|_\_\/__/ |_|\___/_|   |_| |_\__,_|\_, |_|_||_\__, |
                                                         |__/       |___/
                                """)


#########  Function calls   ##########   
for i in range(3):
    gaming_mode()

winner()
