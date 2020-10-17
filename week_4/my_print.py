def inv():
    print('invalid syntax')
    quit()
p = input()
lst = []
while True:
    x = p.find('print')
    if x==-1:
        if len(lst)==0:
            inv()
        break
    if p[x:x+7]=="print('" and p[x+7:].find("')")!=-1:
        idx = x+7+p[x+7:].find("')")
        if p[x+7:idx]!='':
            lst.append(p[x+7:idx])
        else:
            inv()
    else:
        inv()
    p=p[idx:]
for el in lst:
    print(el)