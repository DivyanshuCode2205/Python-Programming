class Two_Dimensional_vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Three_Dimensional_vector(Two_Dimensional_vector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

        # or you can also do so
        
        # self.x = x
        # self.y = y
        # self.z = z

v1 = Two_Dimensional_vector(3, 4)
print(f'2D Vector: {v1.x}i + {v1.y}j')
v2 = Three_Dimensional_vector(5, 4, 9)
print(f'3D Vector: {v2.x}i + {v2.y}j + {v2.z}k')