class Dynamic:
    def __init__(self):
        self.size = 0
        self.array = []
    def insert_data(self,value):
        self.array.append(value)
        self.size += 1
    def get_data(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])


D = Dynamic()
D.insert_data(22)
D.insert_data(31)
D.insert_data(11)
D.insert_data(41)
D.insert_data(21)
v = D.get_data(2)
print(v)
D.print_all()