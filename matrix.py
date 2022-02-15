from random import randint

class Matrix:
    def __init__(self, x_dim,y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.data = []
        self.resize(x_dim,y_dim)

    def __str__(self):
        x=0
        y=0
        ostr = ''
        while y < self.y_dim:
            while x < self.x_dim:
                ostr += str(self.get(x,y))+'\t'
                x+=1
            ostr+='\n'
            x=0
            y+=1
        return(ostr)

    def resize(self, x_dim,y_dim):
        self.data.clear()
        tmp = []
        for y in range(self.y_dim):
            tmp.append(None)

        for x in range(self.x_dim):
            self.data.append(tmp.copy())

    def set(self, x, y, val):
        if x <= self.x_dim+1 and y <= self.y_dim+1:
            self.data[x][y] = val
        else:
            print('index out of bounds')

    def get(self, x, y):
        try:
            return(self.data[x][y])
        except:
            pass
        else:
            pass

    def print(self):
        print(self.__str__())

    def del_col(self, x):
        self.data.remove(self.data[x])
        self.x_dim -=1

    def del_row(self, y):
        for sublist in self.data:
            sublist.remove(sublist[y])
        self.y_dim -=1

    def populate(self):
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                #self.set(x,y, chr(randint(192,600)))
                self.set(x,y, randint(192, 600))

##################################
# SCRIPT
##################################

# inp = input("create matrix with dimensions x,y:\n")
# inp = inp.split(",")
# inp = [int(item) for item in inp]
#
# m = Matrix(inp[0], inp[1])
#
# for x in range(m.x_dim):
#     for y in range(m.y_dim):
#         m.set(x,y, chr(randint(80,500)))
#
# m.print()
