with open('input.txt') as f:
    file=f.read().splitlines()
test=["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
t=[[[g.strip(',') for g in j.strip().split()] for j in x.split(':')[1].split(';')] for x in file]
print(t)
real={'red':12,'green':13,'blue':14}
tot=0
c=0
for game,i in enumerate(t):
    c=0

    data={'red':0,'green':0,'blue':0}
    for j in i:

          data={'red':0,'green':0,'blue':0}
          print(j)
          for k in range(0,len(j),2):
             data[j[k+1]]+=int(j[k])
          for h in real:
            if real[h]<data[h]:
                c=1
    if c==0:
        tot+=game+1
print(f"prima parte :{tot}")
tot=0
c=1
real={'red':0,'green':0,'blue':0}
for game,i in enumerate(t):
    c=1
    real={'red':0,'green':0,'blue':0}
    data={'red':0,'green':0,'blue':0}
    for j in i:

          data={'red':0,'green':0,'blue':0}
          print(j)
          for k in range(0,len(j),2):
             data[j[k+1]]+=int(j[k])
          for h in real:
            if real[h]<data[h]:
                real[h]=data[h]
    for gg in real:
        c*=real[gg]
    tot+=c
print("parte due : {tot}")


