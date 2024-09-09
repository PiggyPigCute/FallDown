from sys import argv
from time import sleep

class FallDownExplosion(Exception):
    def __init__(self, dot, tick, prefix = ""):
        super().__init__("💥" + prefix + " at position (" + str(dot[0]) + "," + str(dot[1]) + ") at tick " + str(tick) + " with direction " + "× ↓ ← → ↑"[d[2]])
class FallDownInput(Exception,id):
    def __init__(self, awnser) -> None:
        text = ("?) must be positive integers","!) must be a single character")[id]
        super().__init__("💀 input values with ("+text+", but awnsered " + awnser)
class FallDownUnexpected(Exception):
    def __init__(self, message) -> None:
        super().__init__("🐷 "+message)

SOLID_CHARS = "\\/-$|"
FILLED_CHARS = "\\/-$|?!#§:~+"

def forward(dot,op,tick,message=" after crossing operand "):
    if dot[2] == 2:
        dot[0] += 1
    elif dot[2] == 4:
        dot[1] -= 1
    elif dot[2] == 6:
        dot[1] += 1
    elif dot[2] == 8:
        dot[0] -= 1
    else:
        raise FallDownUnexpected("wrong direction crossing "+op)
    if map[dot[0]][dot[1]] in FILLED_CHARS:
        raise FallDownExplosion(dot,tick,message+op)


file_path = argv[1]
file = open(file_path, 'r', encoding="utf-8")
map = file.readlines()
file.close()

tick_pause = "-t" in argv
mixer_print = "-m" in argv

dots = []
sums = []
v_size = len(map)
h_size = 0  # value set just after (it's the max lin length)
for i in range(v_size):
    map[i] = map[i].strip('\n')
    if len(map[i]) > h_size:
        h_size = len(map[i])
    for j in range(len(map[i])):
        if map[i][j] == '.':
            dots.append([i+1,j+1,2,0])  # 2↓ 6→ 4← 8↑
        elif map[i][j] == '+':
            sums.append([i+1,j+1,0])
for i in range(v_size):
    map[i] = ' ' + map[i] + ' ' * (h_size-len(map[i])+1)
map = [' ' * (h_size+2)] + map + [' ' * (h_size+2)]

print(' '*len(str(v_size+1))+'┌'+'─'*(h_size+2)+"┐\n"+"\n".join([' '*(len(str(v_size+1))-len(str(i)))+str(i)+"│"+map[i]+"│" for i in range(len(map))])+'\n'+' '*len(str(v_size+1))+'└'+'─'*(h_size+2)+'┘')

tick = 0
while len(dots) > 0:
    if tick_pause:
        sleep(.05)
    for d in dots:
      #↓
        if d[2] == 2:
            if not map[d[0]+1][d[1]] in SOLID_CHARS:
                d[0] += 1
            elif map[d[0]+1][d[1]] == '/':
                if not map[d[0]+1][d[1]-1] in SOLID_CHARS:
                    d[0] += 1
                    d[1] -= 1
                    d[2] = 4
                elif map[d[0]+1][d[1]-1] == '-' and not map[d[0]][d[1]-1] in SOLID_CHARS:
                    d[1] -= 1
                    d[2] = 4
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]+1][d[1]] == '\\':
                if not map[d[0]+1][d[1]+1] in SOLID_CHARS:
                    d[0] += 1
                    d[1] += 1
                    d[2] = 6
                elif map[d[0]+1][d[1]+1] == '-' and not map[d[0]][d[1]-1] in SOLID_CHARS:
                    d[1] += 1
                    d[2] = 6
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]+1][d[1]] == '$' and not map[d[0]-1][d[1]] in SOLID_CHARS:
                    d[0] -= 1
                    d[2] = 8
            else:
                raise FallDownExplosion(d,tick)
      #←
        elif d[2] == 4:
            if not map[d[0]+1][d[1]] in SOLID_CHARS:
                d[0] += 1
                d[2] = 2
            elif map[d[0]+1][d[1]] in "-\\" and not map[d[0]][d[1]-1] in SOLID_CHARS:
                    d[1] -= 1
            elif map[d[0]+1][d[1]] == '/':
                if not map[d[0]+1][d[1]-1] in SOLID_CHARS:
                    d[0] += 1
                    d[1] -= 1
                elif map[d[0]+1][d[1]-1] == '-' and not map[d[0]][d[1]-1] in SOLID_CHARS:
                    d[1] -= 1
                elif map[d[0]+1][d[1]-1] == '/' and not map[d[0]+2][d[1]-1] in SOLID_CHARS:
                        d[0] += 2
                        d[1] -= 1
                        d[2] = 2
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]+1][d[1]] == '$' and not map[d[0]-1][d[1]] in SOLID_CHARS:
                    d[0] -= 1
                    d[2] = 8
            else:
                raise FallDownExplosion(d,tick)
      #→
        elif d[2] == 6:
            if not map[d[0]+1][d[1]] in SOLID_CHARS:
                d[0] += 1
                d[2] = 2
            elif map[d[0]+1][d[1]] in "-/" and not map[d[0]][d[1]+1] in SOLID_CHARS:
                    d[1] += 1
            elif map[d[0]+1][d[1]] == '\\':
                if not map[d[0]+1][d[1]+1] in SOLID_CHARS:
                    d[0] += 1
                    d[1] += 1
                elif map[d[0]+1][d[1]+1] == '-' and not map[d[0]][d[1]+1] in SOLID_CHARS:
                    d[1] += 1
                elif map[d[0]+1][d[1]+1] == '\\' and not map[d[0]+2][d[1]+1] in SOLID_CHARS:
                        d[0] += 2
                        d[1] += 1
                        d[2] = 2
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]+1][d[1]] == '$' and not map[d[0]-1][d[1]] in SOLID_CHARS:
                    d[0] -= 1
                    d[2] = 8
            else:
                raise FallDownExplosion(d,tick)
      #↑
        elif d[2] == 8:
            if not map[d[0]-1][d[1]] in SOLID_CHARS:
                d[0] -= 1
            elif map[d[0]-1][d[1]] == '/':
                if not map[d[0]-1][d[1]+1] in SOLID_CHARS:
                    d[0] -= 1
                    d[1] += 1
                    d[2] = 6
                elif map[d[0]-1][d[1]+1] == '-':
                    d[1] += 1
                    d[2] = 6
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]-1][d[1]] == '\\':
                if not map[d[0]-1][d[1]-1] in SOLID_CHARS:
                    d[0] -= 1
                    d[1] -= 1
                    d[2] = 4
                elif map[d[0]-1][d[1]-1] == '-':
                    d[1] -= 1
                    d[2] = 4
                else:
                    raise FallDownExplosion(d,tick)
            elif map[d[0]-1][d[1]] == '$' and not map[d[0]+1][d[1]] in SOLID_CHARS:
                d[0] += 1
                d[2] = 2
        else:
            raise FallDownUnexpected("wrong direction")
    
    new_dots = []
    plus = False
    dots.sort()

    for d in dots:
        if map[d[0]][d[1]] == '?':
            awnser = input("? ")
            for char in awnser:
                if not char in "0123456789":
                    raise FallDownInput(awnser,0)
            d[3] = int(awnser)
            forward(d,'?',tick)
        if map[d[0]][d[1]] == '!':
            awnser = input("! ")
            if len(awnser) != 1:
                raise FallDownInput(awnser,1)
            d[3] = ord(awnser)
            forward(d,'!',tick)
        elif map[d[0]][d[1]] == '#':
            print(d[3],end='')
            forward(d,'#',tick)
        elif map[d[0]][d[1]] == '§':
            print(chr(d[3]),end='')
            forward(d,'§',tick)
        elif map[d[0]][d[1]] == ":":
            if d[2] in (2,8):
                raise FallDownExplosion(d,tick," crash into a portal (:)")
            else:
                if d[1] > 1:
                    dot = [d[0],d[1]-1,4,d[3]]
                    new_dots.append(dot)
                    if map[dot[0]][dot[1]] in FILLED_CHARS:
                        raise FallDownExplosion(dot,tick," duplicating through a portal (:)")
                d[1] += 1
                d[2] = 6
                if map[d[0]][d[1]] in FILLED_CHARS:
                    raise FallDownExplosion(d,tick," duplicating through a portal (:)")
        elif map[d[0]][d[1]] == "~":
            forward(d,'~',tick)
        elif map[d[0]][d[1]] == "+":
            plus = True
        
        if d[0] <= v_size and map[d[0]+1][d[1]] == "~" and (d[2]==4 or d[2]==6):
            if d[3] == 0:
                d[0] += 2
                if map[d[0]][d[1]] in FILLED_CHARS:
                    raise FallDownExplosion(d,tick," after passing trough water (~)")
            else:
                forward(d,'',tick," after passing over water (~)")
                d[3] -= 1
    
    for d in new_dots:
        dots.append(d)

    new_dots = []
    if plus:
        for p in sums:
            inputs_directions = []
            value = 0
            i = 0
            while i < len(dots):
                dot = dots[i]
                if dot[:2] == p[:2]:
                    inputs_directions.append(dot[2])
                    value += dot[3]
                    del dots[i]
                else:
                    i += 1
            if len(inputs_directions) >= 1:
                if mixer_print:
                    print('+'+str(value), end='')
                if not 8 in inputs_directions and not map[p[0]+1][p[1]] in FILLED_CHARS:
                    new_dots.append([p[0]+1,p[1],2,value])
                elif not 6 in inputs_directions and not map[p[0]][p[1]-1] in FILLED_CHARS:
                    new_dots.append([p[0],p[1]-1,4,value])
                elif not 4 in inputs_directions and not map[p[0]][p[1]+1] in FILLED_CHARS:
                    new_dots.append([p[0],p[1]+1,6,value])
                elif not 2 in inputs_directions and not map[p[0]][p[1]+1] in FILLED_CHARS:
                    new_dots.append([p[0]-1,p[1],8,value])
                else:
                    FallDownExplosion(p," no exit from mixer (+)")

    for d in new_dots:
        dots.append(d)

    i=0
    while i < len(dots):
        dot = dots[i]
        j = i+1
        collision = False
        while j < len(dots):
            if dots[j][:2] == dots[i][:2]:
                collision = True
                del dots[j]
            else:
                j += 1
        if collision or dot[0]<1 or dot[0]>v_size or dot[1]<1 or dot[1]>h_size:
            del dots[i]
        else:
            if dot[2] == 2:
                dot[3] += 1
            i += 1
    tick += 1
