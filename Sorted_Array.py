class sorted_array:
    def __init__(self):
        self.size = 0
        self.array = []
    def insert_data(self,value):
        i = 0
        while i < len(self.array) and self.array[i] < value:
            i += 1
        self.array.append(value)
    def get_data(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(len(self.array)):
            print(self.array[i])


s = sorted_array()
s.insert_data(22)
s.insert_data(31)
s.insert_data(11)
s.insert_data(41)
s.insert_data(21)
v = s.get_data(2)
print(v)
s.print_all()