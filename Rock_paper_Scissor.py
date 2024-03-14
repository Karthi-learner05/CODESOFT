from random import *
def user():
    while True:
        choice1=input("Ente Your choice(rock,paper,scissor) = ").lower()
        if choice1 in ['rock','paper','scissor']:
            return choice1
        else:
            print("Invalid Choice!")
def computer():
    return choice(['rock','paper','scissor'])
def win(c1,c2):
    if c1==c2:
        return "...Tie..."
    elif((c1=='rock' and c2=='scissor' )or(c1=='paper' and c2=='rock' )or(c1=='scissor' and c2=='paper' )):
        return "...You win..."
    else:
        return "...You Loss..."
print("---....ROCK PAPER SCISSOR GAME....---")
play='y'
while play.lower()=='y':
    print("\n")
    u_choice=user()
    c_choice=computer()
    print("Your     choice = ",u_choice)
    print("Computer choice = ",c_choice)
    print(win(u_choice,c_choice))
    print("\n")
    play=input("Do you want to play again?(y/n) = ")

print("\n---.....THANK YOU....---")
