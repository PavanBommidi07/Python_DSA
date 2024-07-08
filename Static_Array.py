class static:
    def __init__(self,size):
        self.size = size
        self.array = [None] * size

    def add_data(self,index, value):
        if index<0 or index >= self.size:
            raise IndexError("Index out of range")
        else:
            self.array[index] = value
    def get_data(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(len(self.array)):
            print(self.array[i])

s = static(5)
s.add_data(0,22)
s.add_data(3,31)
s.add_data(1,11)
s.add_data(4,41)
s.add_data(2,21)
v = s.get_data(4)
print(v)
s.print_all()