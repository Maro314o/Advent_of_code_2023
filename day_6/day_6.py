with open("input.txt","r") as f:
    file=f.read().splitlines()



test=["Time:      7  15   30",
"Distance:  9  40  200"]
race=file
race=[[int(y) for y in x.split(':')[1].split() ]for x in race]
race=[[x,race[1][i]] for i,x in enumerate(race[0])]
c=1
e=0
print(race)
for i in race:
    for j in range(i[0]):
        d=((i[0]-(j+1))*(j+1))
        if d>i[1]:
            e+=1
    
    c*=e
    e=0
print(f"prima parte {c}")
race=[[int(''.join(x.split(':')[1].split())) for x in file]]
c=1
e=0
for i in race:
    for j in range(i[0]):
        d=((i[0]-(j+1))*(j+1))
        if d>i[1]:
            e+=1
    c*=e
    e=0
print(f"seconda parte {c}")


