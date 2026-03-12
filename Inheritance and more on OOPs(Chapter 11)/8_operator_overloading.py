class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other): # 'self' represents object before operator and 'other' represents object after operator
        return Point(self.x + other.x, self.y + other.y) # this creates another point object
    
    def __len__(self): # distance of a point from origin
        return int(((self.x)**2 + (self.y)**2) ** 0.5)
    
    def __str__(self):
        return f'Point ({self.x}, {self.y})'

p1 = Point(2, 3)
print(str(p1))
p2 = Point(5, 6)
# p3 = p1 + p2
p4 = Point(3, 4)
print(p1 + p2) # p1 + p2 is translated to p1.__add__(p2)
print(f'Distance from origin to {p4}: {len(p4)}')
