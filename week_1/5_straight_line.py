x1, y1 = input('x1, y1: ').split(" ")
x2, y2 = input('x2, y2: ').split(" ")
x, y = input('x, y: ').split(" ")
a = (float(x)-float(x1)) * (float(y2)-float(y1)) - (float(x2)-float(x1)) * (float(y)-float(y1))
if a>0:
    print('Above')
elif a==0:
    print('On line')
else:
    print('Below')