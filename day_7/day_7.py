with open("input.txt","r") as f:
    file=f.read().splitlines()
test=["32T3K 765",
"T55J5 684",
"KTJJT 220",
"KK677 28",
"QQQJA 483"]
segni=["A", "K", "Q",  "T", "9", "8", "7", "6", "5", "4", "3", "2","J"][::-1]
power=[[] for i in range(7)]
ji=test
ji=[x.split() for x in ji]
for i in ji:
    mano=i[0]
    soldi=i[1]
    if mano==mano[0]*5:
        power[6].append(i) 
        continue
    for j in mano:
        if mano.count(j)==4:
            power[5].append(i)
            break
    else:
        for j in mano:
            if mano.count(j)==3:
                if mano.replace(j,'').replace(' ','').count(mano.replace(j,'').replace(' ','')[0])==2:
                    power[4].append(i)
                    break
                else:
                    power[3].append(i)
                    break
                break
        else:
                
            for j in mano:  
                if mano.count(j)==2:
                    for k in  mano.replace(j,''):
                        if mano.replace(j,'').count(k)==2:
                            power[2].append(i)
                            break
                    else:
                        power[1].append(i)
                        break
                    break
            else:
                power[0].append(i)
pow=[]
def sor(i):
    alphabet=''.join(segni)
    a=[x[0] for x in i]
    li= sorted(a, key=lambda word: [alphabet.index(c) for c in word])
    for k in i:
        li[li.index(k[0])]=[k[0],k[1]]
    return li

for i in power:
    pow.extend(sor(i))
rr=0
for x,i in enumerate(pow):
        rr+=(int(i[1])*(x+1))
print(f"prima parte {rr}")

segni=["A", "K", "Q","T", "9", "8", "7", "6", "5", "4", "3", "2","J"][::-1]
power=[[] for i in range(7)]
ji=file
ji=[x.split() for x in ji]
for i in ji:
    mano=i[0]
    soldi=i[1]
    for j in mano:
        if mano.replace('J',j).count(j)==5:
            power[6].append(i) 
            break
    else:
        for j in mano:
            if mano.replace('J',j).count(j)==4:
                power[5].append(i)
                break
        else:
            for j in mano:
                if mano.replace('J',j).count(j)==3:
                    if mano.replace('J',j).replace(j,'').replace(' ','').count(mano.replace("J",j).replace(j,'').replace(' ','')[0])==2:
                        power[4].append(i)
                        break
                    else:
                        power[3].append(i)
                        break
                    break
            else:
                    
                for j in mano:  
                    if mano.replace('J',j).count(j)==2:
                        for k in  mano.replace('J',j).replace(j,''):
                            if mano.replace('J',j).replace(j,'').count(k)==2:
                                power[2].append(i)
                                break
                        else:
                            power[1].append(i)
                            break
                        break
                else:
                    power[0].append(i)
pow=[]


for i in power:
    pow.extend(sor(i))
rr=0
for x,i in enumerate(pow):
        rr+=(int(i[1])*(x+1))
print(f"seconda parte {rr}")






