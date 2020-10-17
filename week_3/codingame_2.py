import operator
import sys
def longest_seq_of_1s():
    b = input()
    def dec(b):
        for i in range(len(b)):
            ans = list(b)
            if b[i] == '0':
                ans[i] = '1'
                yield ans
    val = dec(b)
    res = []
    for i in range(len(b)):
        try:
            for x in ''.join(next(val)).split('0'):
                res.append(len(x))
        except:
            pass
    print(max(res))

def ascii():
    l = int(input())
    h = int(input())
    t = list(input())
    lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
    print(t)
    for i in range(h):
        row = input()
        for j in range(len(t)):
            if t[j] in lst:
                print(row[l*lst.index(t[j]):l*lst.index(t[j])+l])
            else:
                print(row[l*26:l*26+l])

def scrabble():
    data = {'e': 1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
    'd':2, 'g':2, 'b':3,'c':3,'m':3,'p':3, 
    'f':4, 'h':4,'v':4,'w':4, 'y':4,'k':5,'j':8,'x':8,'q':10,'z':10
    }
    n = int(input())
    wrds = [input() for i in range(n)]
    wrds.reverse()
    letters = tuple(input())
    valid = []
    for wrd in wrds:
        inv = False
        ls = list(letters)
        for lt in wrd:
            if lt not in ls:
                inv = True
                break
            else:
                ls.remove(lt)
        if inv == False:
            valid.append(wrd)
    res = {}
    for each in valid:
        pnt = 0
        for l in each:
            pnt += data[l]
        res[each] = pnt
    print(max(res.items(), key=operator.itemgetter(1))[0])
def happy_num():
    def isHappy(x):
        seen = {1}
        while x not in seen:
            seen.add(x)
            x = sum([int(x)**2 for x in str(x)])
        return x == 1
        n = int(input())
        for i in range(n):
            x = input()
            print(x, ":)" if isHappy(x) else ":(")


def min_ball_cost():
    b,w,x,y,z = [int(i) for i in input().split()]
    print(b*x+w*y+min(b*(y-x+z),w*(x-y+z),0))

def pascal():
    r = int(input())       
    def PascalTriangle(n):
       trow = [1]
       y = [0]
       for x in range(n):
          trow=[left+right for left,right in zip(trow+y, y+trow)]
       return trow
    a = PascalTriangle(r)
    s = 1
    for i in a:
        s = s*i
    print(s)
def _1():
    w = ''
    for s in input().split():w=f'{w}{int(s[:-1])*s[-1]}'
    print(w)
def _2():
    s = input().split()
    s = reversed(s)
    print(*s)
def _3():
    n = int(input())
    y = sum([int(i)**2 for i in str(n)])
    print(n, "IS HAPPY" if y == 1 else "IS UNHAPPY")

def _4():
    s = input()
    key = list('31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    eng = sorted('qwertyuiopasdfghjklzxcvbnm'.upper())
    eng.reverse()
    def caesar(d, msg, k):
        ans = ''
        j = 0
        for i in msg:
            try:
                ans += d[(d.index(i) + int(k[j]))%26]
            except:
                ans += i
            j += 1
        return ans 
    print(caesar(eng, s, key))
def _5():
    def get_divisors(n):
        cnt = 0
        for i in range(1, int(n / 2) + 1):
            if n % i == 0:
                cnt += 1
        return cnt
    a, b = [int(i) for i in input().split()]
    ans = 0
    for num in range(a, b+1):
        if get_divisors(num)%2==1: ans+=1
    print(ans)
def _6():
    n=int(input())
    for i in range(n):
        t=input()
        print(str(sum(int(d) for d in t[:3])==sum(int(d) for d in t[3:])).lower())

def _7():
    P = set()
    l = int(input())
    n = int(input())
    for i in range(n):
        st, ed = [int(j) for j in input().split()]
        for f in range(st,ed):P.add(f)
    print("Debug messages...", file=sys.stderr, flush=True)
    print(l-len(P))


def _8():
    from collections import Counter
    count = int(input())
    lst = [input() for i in range(count)]
    d = Counter(lst)
    print(d)
    if d[-2] == d[-1]:
        print('N')
    else:
        print(d[-1])

def _9():
    from string import punctuation
    s = input()
    sorted_list = sorted(list(s), key=str.casefold)
    ans = ''
    for i in s:
        if i in set(punctuation):
            ans += i
    print(''.join(sorted_list).strip()[len(ans):] + ans)

def _10():
    from math import gcd
    n = int(input())
    lst = [int(i) for i in input().split()]
    lcm = lst[0]
    for i in lst[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    print(lcm)

def _11():
    import re
    n = int(input())
    q = int(input())
    d = {}
    for i in range(n):
        ext, mt = input().split()
        d[ext] = mt
    for i in range(q):
        fname = input()
        lst = re.findall('[\d\D]+\.([\d\D]+)', fname)
        print(lst)
        if len(lst)!=0:
            mim = lst[0]
            print(d.get(mim, 'UNKNOWN'))
        else:
            print('UNKNOWN')
def _12():
    w,d,o=input().split()
    o=int(o)
    l=len(w)
    for i in range(o*2+1):
        print(''.join(d*o+' '+w+' '+d*o) if i==(o*2+1)//2 else ''.join(d*(l+(o*2)+2)))

def code_game():
    nF,w,r,xF,xP,c,E,nE=[int(i) for i in input().split()]
    map=[xP]*nF
    for i in range(nE):
        eF,elP=[int(i) for i in input().split()]
        map[elF]=elP
    while True:
        cF,cP,d=input().split()
        print("BLOCK" if ((cP<map[int(cF)] and d=="LEFT") or (c>map[int(cF)] and d=="RIGHT")) else "WAIT")

def bot():
    import math
    boost = 0
    while True:
        x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
        opponent_x, opponent_y = [int(i) for i in input().split()]
        dist = ((x - next_checkpoint_x)**2 + (y - next_checkpoint_y)**2)**0.5
        if boost == 0 and next_checkpoint_dist > 4000  and abs(next_checkpoint_angle)<90:
            thrust = "BOOST"
            boost = 1
        elif ((x - opponent_x)**2 + (y-opponent_y)**2)**0.5 <= 400:
            thrust = "SHIELD"
        elif abs(next_checkpoint_angle) > 90:
            thrust = 10
        elif abs(next_checkpoint_angle) < 90:
            thrust = 100 - abs(next_checkpoint_angle)//4
        else:
            thrust = 100
        print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + f" {thrust}")

def magic_word():
    magic_phrase = input()
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    def alpha(pos, idx):
        if abs(pos - idx)<13:
            return '+'
        else:
            return '-'
    def direct(pos, let):
        if let in d:
            if eng.index(let)<pos:
                return '>'
            else:
                return '<'
        return '>'
    v = 0
    d = []
    for i in magic_phrase:
        if i == ' ':
            ans+='.'
            continue
        b=alpha(v, eng.index(i))
        ans+=b+'.'+direct(v, i)
        d.append(ans)
        if b=='+':
            v += 1
        elif b=='-':
            v -= 1
    print(ans)