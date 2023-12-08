with open("input.txt",'r') as f:
    file=f.read().splitlines()

test=["seeds: 79 14 55 13",

"seed-to-soil map:",
"50 98 2",
"52 50 48",

"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",

"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",

"water-to-light map:",
"88 18 7",
"18 25 70",

"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",

"humidity-to-location map:",
"60 56 37",
"56 93 4"]
juicy=test
all_s=[]
o=[]
for i in juicy:
    if i=='':
        continue
    elif 'seeds' in i:
        for g in i.split(':')[1].split():
            o.append(int(g))

    elif  ':' in i:
        all_s.append(o)
        o=[]
    else:
        o.append([int(x) for x in i.split()])
all_s.append(o)
c=[all_s[0]]
c[0]=[79]
vov=[]

for y,i in enumerate(all_s):
    if y!=0:
        for x,j in enumerate(c[y-1]):
            d=len(vov)
            for ii,k in enumerate(i):
              if k[1]+k[2]>j and j>=k[1]:
                vov.append(k[0]+j-k[1])
            if d==len(vov):
                vov.append(j)
        c.append(vov)
        vov=[]
print(f"prima parte:{min(c[-1])}")
vov=[]

                
vov=[]
c=[]
c=[[[all_s[0][x],all_s[0][x+1]] for x in range(0,len(all_s[0])-1,2)]]
for y,i in enumerate(all_s):
    if y!=0:
        for x,j in enumerate(c[y-1]):
            d=len(vov)
            min_seed=j[0]
            max_seed=min_seed+j[1]
            range_seed=k[2]
            new_seed_start=k[0]
            map_seed_start=k[1]

            for ii,k in enumerate(i):

              if ga>=k[1] and gg<=k[1]+k[2]:
                  vov.append([k[0]+ga-k[1],j[1]])
              if ga<k[1] and gg<k[1]+k[2]:
                  vov.append([ga,k[1]-ga])
                  vov.append([k[0],gg-k[1]])
               
              if ga>k[1] and gg>(k[1]+k[2]):
                 vov.append([k[0]+(ga-k[1]),k[1]+k[2]-ga])
                 vov.append([k[1]+k[2],gg-k[1]-k[2]])
              if ga<k[1] and gg>(k[1]+k[2]):
                  vov.append([ga,k[1]-ga])
                  vov.append([k[0],k[0]+k[2]])
                  vov.append([k[1]+k[2],gg-k[1]-k[2]])
            
        c.append(vov)
        vov=[]



print(c)
               
print(len(c[-1]))
r=10000000
for i in c[-1]:
    if i[0]<r:
        r=i[0]
print(r)


 






