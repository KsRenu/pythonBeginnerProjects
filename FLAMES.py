n1=list(input("Enter first name : ").lower())
n2=list(input("Enter second name: ").lower())
l=[]
for i in n1:
    for j in n2:
        if i==j:
            n1.remove(i)
            n2.remove(i)
n=len(n1)+len(n2)
print(n)
game=['F','L','A','M','E','S']
idx=0
while len(game)>1:
    idx=((idx+n)%len(game))-1
    game.remove(game[idx])
    print(game)
print(game)



