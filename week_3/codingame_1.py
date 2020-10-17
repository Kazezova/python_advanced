import math
from itertools import groupby
def encode_my_norris():
    def encode(b):
        lst = list(b)
        ans = ""
        i = 0
        while i < len(lst):
            if lst[i] !='1':
                ans += ' 00 0'
                k = i
                while k<len(lst)-1 and lst[k+1] == '0':
                    ans += '0'
                    k += 1
                i = k + 1  
            else:
                ans += ' 0 0'
                j = i
                while j<len(lst)-1 and lst[j+1] == '1':
                    ans += '0'
                    j += 1
                i = j + 1
        return ans.strip()

    message = input()
    b_str = ""
    for i in message:
        b_str += str('{0:07b}'.format(ord(i)))
    print(encode(b_str))

# print(input().lower().title())
def sort():
    n = int(input())
    a=input().split()
    for i in range(len(a)):
        a[i]=int(a[i])
    a.sort()
    print(*a)

def temperature():
    ln = input() or '0'
    temps = [int(s) for s in ln.split()]
    temps.sort(key = lambda x: (abs(x),-x))
    print(temps[0])

def horse_racing_duals():
    l = sorted([int(input()) for _ in range(int(input()))])
    print(min((l[i+1] - l[i] for i in range(len(l) - 1))))

def chuck_norris():
    msg = input()
    out=""
    bn=""
    b=""
    for c in msg:
        bn += bin(ord(c))[2:].zfill(7)
    for c in bn:
        if c == "1" != b:
            out += " 0 "
            b="1"
        elif c == "0" != b:
            out += " 00 "
            b="0"
        out += "0"
    print(out.strip())

def power_of_thor():
    lx, ly, x, y = [int(i) for i in input().split()]
    while True:
        move  = 'N' if y>ly else 'S' if y<ly else ''
        move += 'W' if x>lx else 'E' if x<lx else ''
        if 'N' in move: y-=1
        if 'S' in move: y+=1
        if 'W' in move: x-=1
        if 'E' in move: x+=1
        print(move)
def descent():
    while True:
        print(max([(int(input()),x) for x in range(8)])[1])

def myyy_power_of_thor():
    lx, ly, tx, ty = [int(i) for i in input().split()]
    while True:
        remaining_turns = int(input())
        ans_x = ''
        ans_y = ''
        if tx < lx:
            ans_x = 'E'
            tx += 1
        elif tx > lx:
            ans_x = 'W'
            tx -= 1
        if ty < ly:
            ans_y = 'S'
            ty += 1 
        elif ty > ly:
            ans_y = 'N'
            ty -= 1 
        print(ans_y + ans_x)

# speed = int(input())
# light_count = int(input())
# lst = []
# maxi = 0
# for i in range(light_count):
#     distance, duration = [int(j) for j in input().split()]
#     lst.append((distance, duration))

# for k in range(light_count):
#     if ((18 * lst[k][0]) % (10 * speed * lst[k][1]) >= (5 * speed * lst[k][1])):
#         speed -= 1
#         k = -1
# print(speed)

# for k, v in data.items():
#     x = 3.6*(k/v)
#     if speed <= x:
#         while (x/speed).is_integer() == False:
#             speed -= 1
#         maxi = speed
#     else:
#         maxi = speed
#     max_list.append(maxi)
# k % (speed * 10)/36 == 0
def defibrillators():
    lonA = math.radians(float(input().replace(',', '.')))
    latA = math.radians(float(input().replace(',', '.')))
    n = int(input())
    data = {}
    lst = [input() for _ in range(n)]
    close = []
    for defib in lst:
        defib = defib.split(';')
        longtitudeB = math.radians(float(defib[4].replace(',','.')))
        latitideB = math.radians(float(defib[5].replace(',', '.')))
        x = (longtitudeB - lonA) * math.cos((latA + latitideB)/2) 
        y = latitideB - latA
        d = math.sqrt(x**2 + y**2)*6371
        close.append(d)
    print(lst[close.index(min(close))].split(';')[1])

def there_is_no_spon():
    width = int(input())
    height = int(input())
    lst = [list(input()) for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if lst[y][x] == '.': 
                continue
            x2, y2, x3, y3 = -1, -1, -1, -1
            #check right
            try:
                for nx in range(x+1, width):
                    if lst[y][nx] == '0':
                        x2 = nx
                        y2 = y
                        break
            except IndexError:
                pass
            #check buttom
            try:
                for ny in range(y+1, height):
                    if lst[ny][x] == '0':
                        x3 = x
                        y3 = ny
                        break
            except IndexError:
                pass
            print(x, y, x2, y2, x3, y3)
def there_is_no_spon_ep_1():
    width = int(input())  # the number of cells on the X axis
    height = int(input())  # the number of cells on the Y axis
    lines = [input() for _ in range(height)]  # width characters, each either 0 or .


    def find_right_neighbor(x, y):
        for i in range(x + 1, width):
            if lines[y][i] == '0':
                return i, y
        return -1, -1


    def find_bottom_neighbor(x, y):
        for i in range(y + 1, height):
            if lines[i][x] == '0':
                return x, i
        return -1, -1


    for y in range(height):
        for x in range(width):
            if lines[y][x] == '0':
                rx, ry = find_right_neighbor(x, y)
                bx, by = find_bottom_neighbor(x, y)
                print(x, y, rx, ry, bx, by)

def my_conway():
    r = int(input())
    l = int(input())
    if len(str(r))==1:
        lst = [str(r), f'1{r}']
    else:
        lst = [r, f'1 {(r)}']
    for i in range(1, l-1):
        ans = ''
        s = [''.join(g) for _, g in groupby(lst[i])]
        for j in s:
            ans = ans + str(len(j)) + str(j[0])
        lst.append(ans)
    if l == 1:
        print(lst[0])
    elif(len(str(r)) == 1):
        print(*lst[-1])
    else:
        print(' '.join((lst[-1].split()[0].split())[0]) + ' '+str(r))

def improve_conway():
    r = [int(input())]
    l = int(input())
    def next_row(r):
        for v, lst in groupby(r):
            yield sum(1 for k in lst)
            yield v
    for n in range(l-1):
        r = next_row(r)
    print(*r)
def puzzle_of_week():
    def switch_demo(argument):
        switcher = {
            '.': '0',
            '#': '0',
            '^': 'x-1',
            'v': 'x+1',
            '<': 'y-1',
            '>': 'y+1',
            'T': 'done!'
        }
        return switcher.get(argument, 0)
    def valid_map(lst_map, x, y):
        x0, y0 = x, y
        i = 0
        while True:
            try:
                do = switch_demo(lst_map[x][y])
            except IndexError:
                return None
            if do == '0' or (x0 == x and y0 == y and i > 1): 
                return None
            elif do == 'done!':
                break
            elif 'y' in do:
                y = eval(do)
            elif 'x' in do:
                x = eval(do)
            i+=1
        return i+1
    w, h = [int(i) for i in input().split()]
    start_row, start_col = [int(i) for i in input().split()]
    n = int(input())
    data = {}
    for i in range(n):
        lst = []
        for j in range(h):
            map_row = input()
            lst.append(map_row)
        dist = valid_map(lst, start_row, start_col)
        if dist != None:
            data[dist] = i
    if len(data) == 0:
        print('TRAP')
    else:
        print(data.get(min(data)))

def dice():
    dices = sorted(int(i) for i in input().split())
    try:
        print(str(
            any(
                all(dices[i+1] - dices[i] == 1 for i in range(j, j+4))
                for j in range(3)
            )
        ).lower())
    except IndexError:
        print("true")

# n = int(input())
# for i in range(n):
#     if i==0 or i==n-1:
#         print("#"*n)
#     else:
#         print("#"+" "*(n-2)+"#")

def prime():
    I=lambda:map(int,input().split())
    input();input()
    p=1
    for i in I():p*=i
    for i in I():print(['T','F'][i%p>0],end='')
def ans():
    for i in range(5):
        l = input().split()
        for x,y,z in zip(l[0],l[1],l[2]):
            print((y,z)[x=="1"], end="")
        print()

def _my_temperatures():
    n = int(input())
    ln = input() or '0'
    temps = [int(s) for s in ln.split()]
    temps.sort(key = lambda x: (abs(x),-x))
    print(temps)