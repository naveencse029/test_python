x = 1
y = 1
z = 2
n = 3

l1=[*range(x+1)]
l2=[*range(y+1)]
l3=[*range(z+1)]


l4=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+c+b !=n]
print(l4)
