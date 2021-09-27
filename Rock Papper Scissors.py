#r>s,s>p,p>r
import random
def win(player,opponent): # true if player 
    if (player == 'r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
def play():
    user=input("(r)for rocks, (s) for scissors, (p) for papper : ")
    user=user.lower()
    computer=random.choice(['r','s','p'])
    if user==computer:
        print("Its tie")
    if win(user,computer):
        print("Won")

play()
