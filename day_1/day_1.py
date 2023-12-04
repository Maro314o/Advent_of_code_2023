with open("input.txt",'r') as file:
    file=file.read().splitlines()
test=["1abc2",
"pqr3stu8vwx",
"a1b2c3d4e5f",
"treb7uchet"]

tot=0
c=''

for i in file:
    for d in i:
        if d.isnumeric():
            c+=d
            i=i[::-1]
            for f in i:
                if f.isnumeric():
                    c+=f
                    break
            break
    tot+=int(c)
    c=''
print(f"prima parte:{tot}")

tr=10000
o=0

test2=["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
       "fiveeight792eightqskstrftdpccsrgskrhc","nine1ztqbs"]

numeri=["one","two","three", "four", "five", "six", "seven", "eight", "nine"]
tot=0
c=''
ew=10000
for numero in file:
    for m,d in enumerate(numeri):
        if d in numero:
            if ew>numero.index(d):
                ew=numero.index(d)
                o=m+1
    for eww,gd in enumerate(numero):
        if gd.isnumeric() and eww<ew:
            ew=eww
            o=gd
    c+=str(o)
    o=0
    ew=100000
    
    for m,d in enumerate(numeri):
        if d[::-1] in numero[::-1]:
            if ew>numero[::-1].index(d[::-1]):

                ew=numero[::-1].index(d[::-1])
                o=m+1
    for eww,gd in enumerate(numero[::-1]):
        if gd.isnumeric() and eww<ew:
            ew=eww
            o=gd
            
           # print(o,9)
   # print(o)
    c+=str(o)
    tot+=int(c)
    c=''
    ew=1000
print(f"seconda parte:{tot}")








                           




