import time
import numpy
with open("input.txt","r") as f:
    file=f.read().splitlines()
test=["LLR",
'',
"AAA = (BBB, BBB)",
"BBB = (AAA, ZZZ)",
"ZZZ = (ZZZ, ZZZ)"]
test2=["RL",
'',

"AAA = (BBB, CCC)",
"BBB = (DDD, EEE)",
"CCC = (ZZZ, GGG)",
"DDD = (DDD, DDD)",
"EEE = (EEE, EEE)",
"GGG = (GGG, GGG)",
"ZZZ = (ZZZ, ZZZ)"]
test3=['LR',
'',
'11A = (11B, XXX)',
'11B = (XXX, 11Z)',
'11Z = (11B, XXX)',
'22A = (22B, XXX)',
'22B = (22C, 22C)',
'22C = (22Z, 22Z)',
'22Z = (22B, 22B)',
'XXX = (XXX, XXX)']
hashmap={}
ji=file
instructions=ji.pop(0)
ji.pop(0)
for i in ji:
    r=i.split('=')
    hashmap[r[0].strip()]=[x.strip() for x in r[1].strip(' ()').split(',')]
instructions=instructions.replace('L','0').replace('R','1')
start='AAA'

c=0
indice=0
while indice<=len(instructions)-1:
    ins=instructions[indice]
    if start=='ZZZ':
        break
    if indice==len(instructions)-1:
        instructions+=instructions
    start=hashmap[start][int(ins)]
    c+=1
    indice+=1

print(f"parte uno {c}")
start=[x.split('=')[0].strip() for x in ji if x.split('=')[0].strip()[-1]=='A']
iu=[[] for x in start]
c=0
indice=0
while indice<=len(instructions)-1:
    ins=instructions[indice]
    
    if indice==len(instructions)-1:
        instructions+=instructions
    for x,i in enumerate(start):
       if i=='':
           continue
       start[x]=hashmap[i][int(ins)]

    c+=1
    indice+=1
    o=0
    d=0
    for fr,k in enumerate(start):
        if k=='':
            d+=1
            continue
        if k[-1]=='Z':
            iu[fr]=c
            start[fr]=''

    if o==len(start) or d==len(start):
        break
print(f"parte due {numpy.lcm.reduce(iu)}")

