
# y = input()
# if '^' in y:
#     x = y.split('^')
# else:
#     x = y
# if x == y:
#     print(x[0])
# elif x[1] == '2':
#     print(x[1]+'x')
# else:
#     print(str(int(x[0][0])*int(x[1]))+'x'+'^'+str(int(x[1])-1))

# z=input
# k=a=int(z())
# exec("k**=a;"*(int(z())-2))
# z(a**k)

# n = int(input())
# lst=[]
# for i in range(n):
#     s = input()
#     lst.append(s)
# m = int(input())
# a=[int(x) for x in input().split()]
# for i in range(n,n+m):
#     b=lst[n-i]
#     for j in a:
#         if i==j:b+='.'
#         if i<j:b+='.'
#         if i>j:b+='#'
#     print(*b)

# n = int(input())
# xs = []
# for i in range(n):
#     s,t = input().rsplit(" ",1)
#     t = int(t)
#     if t >= 0:
#         xs += [(t,s)]
# if not xs: print("NONE")
# for _,x in sorted(xs):print(x)

# c=input()
# print(sum([i*(x==c)for i,x in enumerate(input())]))

# exec("print()")

# p=input().split()
# lst=[]
# for i in p:
#     i = i.strip(":;,.?!")
#     if i[:6]=="print(" and i[-1:]==")":
#         if i[6] == "'" and i[7:len(i)-2]!='' and i[-2]== "'":
#             lst.append(i[7:len(i)-2])
#         else:
#             lst=[]
#             break
# if len(lst)==0:
#     print('invalid syntax')
# else:
#     for el in lst:
#         print(el)
# z=input
# n=int(z())
# s=[]
# exec("s+=[z()];"*n)
# z()
# h=list(map(int,z().split()))
# for i in range(n):
#     t=""
#     for j in h:t+="#"*(j>=n-i)+"."*(j<n-i)
#     print(s[i]+t)

# n = int(input())
# a=[int(x) for x in input().split()]
# for i in range(max(a),0,-1):
#     b=[]
#     for j in a:
#         if i==j:b+=['***']
#         if i<j:b+=['* *']
#         if i>j:b+=['   ']
#     print(*b)

a, n = [float(i) for i in input().split()]
s = 0
for i in range(0,int(n)+1):
    x = 1
    while i>=0:
        x = x*(1/(a+i))
        i-=1
    s += x
print(round(s,6))