class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __str__(self):
        return (f'Vector: {self.x}i + {self.y}j + {self.z}k')
    
v1 = Vector(3, 4, 7)
v2 = Vector(5, 3, 9)
v3 = v1 + v2
v4 = v1 * v2
print(f'Vector summation: {v3}')
print(f'Vector dot product: {v4}')
