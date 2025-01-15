class Array1D:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        
    def get(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")
        
    def set(self, index, value):
        if 0 <= index < self.size:
            self.array[index] = value
        else:
            raise IndexError("Index out of bounds")
        
    def length(self):
        return self.size
    
    def display(self):
        print(self.array)
        
my_array = Array1D(5)

my_array.set(0, 10)
my_array.set(1, 20)                
my_array.set(2, 30)                
my_array.set(3, 40)                
my_array.set(4, 50)

my_array.display()

print("Value at index 2: ", my_array.get(2))
print("Value at index 4: ", my_array.get(4))

print("Array length: ", my_array.length())