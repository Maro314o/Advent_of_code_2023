with open("input.txt", 'r') as f:
    file = f.read().splitlines()
test = ["467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."]
simboli = []
cord = []
ji = file
num = ''
sing_cord = []
for y, i in enumerate(ji):
    for x, h in enumerate(i):
        if not (h.isnumeric()):
            if num != '':
                cord.append([num, sing_cord])
                num = ''
                sing_cord = []
        else:
            num += h
            sing_cord.append([y, x])
tot = 0
for y, i in enumerate(ji):
    for x, h in enumerate(i):
        if not (h.isnumeric() or h == '.'):
            for k in cord:
                for ff in k[1]:
                    if ff == [y, x + 1] or ff == [y, x - 1] or ff == [y + 1, x] or ff == [y - 1, x] or ff == [y + 1,
                                                                                                              x + 1] or ff == [
                        y - 1, x + 1] or ff == [y + 1, x - 1] or ff == [y - 1, x - 1]:
                        tot += int(k[0])
                        break

print(f"prima parte :{tot}")
tot = 0
o = []
for y, i in enumerate(ji):
    for x, h in enumerate(i):
        if h == '*':
            o = []
            for k in cord:
                for ff in k[1]:
                    if ff == [y, x + 1] or ff == [y, x - 1] or ff == [y + 1, x] or ff == [y - 1, x] or ff == [y + 1,
                                                                                                              x + 1] or ff == [
                        y - 1, x + 1] or ff == [y + 1, x - 1] or ff == [y - 1, x - 1]:
                        o.append(k[0])
                        break
            if len(o) == 2:
                tot += int(o[0]) * int(o[1])
print(f"seconda parte : {tot}")
