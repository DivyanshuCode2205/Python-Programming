class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return int((self.x **2 + self.y ** 2 + self.z ** 2) ** 0.5) # rounded-off to an integer
    
v = Vector(3, 4, 5)
print(f'Dimensions of vector is {len(v)}')
