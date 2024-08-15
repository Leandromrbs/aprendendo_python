x={}

x[(5,7,6)] = 7
x[(4,1,1)] = 5
x[(7,5)] = 4
x[(4,1,1)] = 0

total = 0

for i in x:
    total=total+x[i]

print(len(x)+total)