class Vector:
    x = 7
    y = 8
    z = 10

    def __str__(self):
        return f'{self.x}i + {self.y}j + {self.z}k'

v = Vector()
print(v)