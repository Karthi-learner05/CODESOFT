import random

class RPS_GAME:
    player_score=0
    computer_score=0
    def com_choice(self):
        return random.choice(["rock","paper","scissor"])
    def user_choice(self):
        choice=input("Enter your choice : ").lower()
        if choice not in ["rock","paper","scissor","n","s"]:
            print("Invalid Input...\n")
            return self.user_choice()
        return choice
    def check_winner(self,user,com):
        print("Computer choice : ",com)
        if(user==com):
            return "Tie\n"
        elif(((user=="rock")and(com=="scissor"))or((user=="paper")and(com=="rock"))or((user=="scissor")and(com=="paper"))):
            self.player_score+=1
            return "You won the game 🏆 \n"
        else:
            self.computer_score+=1
            return "Computer won the game 😔 \n"
    def check_score(self):
        print("----------------------------------------------------------------------")
        print("|                                |                                   |")
        print("|              PLAYER            |            COMPUTER               |")
        print("----------------------------------------------------------------------")
        print("|                                |                                   |")
        print("|              ",self.player_score,"               |            ",self.computer_score,"                    |")
        print("|                                |                                   |")
        print("----------------------------------------------------------------------\n")
if __name__=='__main__':
    play="y"
    rps=RPS_GAME()
    print("-----------------WELCOME TO ROCK PAPER SCISSOR GAME-----------------\n Choices are,\n 1.rock\n 2.paper\n 3.scissor \n To EXIT input chice as n\n To CHECK SCORE input choice as s\n")
    while(play=="y"):
        user_option=rps.user_choice()
        if(user_option=="s"):
            rps.check_score()
            continue
        if(user_option=="n"):
            print("\n----------THANK YOU 🙏 COME BACK AGAIN----------")
            break
        com_option=rps.com_choice()
        print(rps.check_winner(user_option,com_option))
