#Сравнивает все элементы один за другим и свайпает, процесс идет до тех пор пока не будет ни одного свайпа
def bubble(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    return lst
#Находить минимум из списка(отрезок от i до конца) и свайпает местами с первым элементом
def selection(lst):
    for j in range(len(lst)-1):
        current_min = lst[j]
        position = j 
        for i in range(j, len(lst)):
            if current_min > lst[i]:
                current_min = lst[i]
                position = i
        lst[j], lst[position] = current_min, lst[j]
    return lst
#Сравнивает ключевой элемент с предыдущим до начала списка и перемешает большие элементы на одну позицию вверх    
def insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1 
        while (j>=0 and lst[j]>key):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def merge(lst):
    if(len(lst)>1):
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i+=1
            else:
                lst[k] = right[j]
                j+=1
            k+=1 

        while i < len(left): 
            lst[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            lst[k] = right[j] 
            j+= 1
            k+= 1
    return lst
    
l = [10, 9, 8, 7]
print(merge(l))
