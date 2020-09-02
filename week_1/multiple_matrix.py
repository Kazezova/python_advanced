# m,k x k,n = mxn 
class Matrix:
    def __init__(self, first_matrix, second_matrix):
        self.first = first_matrix
        self.second = second_matrix
        self.result = []
        for i in range(len(self.first)):
            temp = []
            for j in range(len(self.second[0])):
                temp.append(0)
            self.result.append(temp)
    
    def multiple(self):
        if(len(self.first[0]) == len(self.second)):
            for i in range(len(self.first)): #2
                for j in range(len(self.second[0])): #4☺
                    s = 0
                    for k in range(len(self.second)): #3
                        self.result[i][j]+=self.first[i][k]*self.second[k][j]
        else:
            print('This matrices can not multiple')
            quit()
    
a = [
    [1, 4, 3],
    [2, 5, 4]
]
b = [
    [2, 5, 4, 5],
    [2, 3, 4, 6],
    [1, 5, 4, 6]
]
c = Matrix(a, b)
c.multiple()
for i in range(len(c.result)):
    for j in range(len(c.result[i])):
        print(c.result[i][j], end=" ")
    print()
    