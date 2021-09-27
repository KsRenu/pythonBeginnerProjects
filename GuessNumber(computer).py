#Third project=guess number(Computer)-provider(user)

import random


def computer(x):
    low=0
    high=x
    ans=''
    while ans!='c':
        if low==high:
            guess=low
        else:
            guess=random.randint(low,high)
        print(guess)
        ans=input('Answer is High(h), Low(l) or Correct(c) : ')
        ans=ans.lower()
        if ans=='h':
            high=guess-1
        elif ans=='l':
            low=guess+1
    print("Found the answer")

computer(199)
    
    
