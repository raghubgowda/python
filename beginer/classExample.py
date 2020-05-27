class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f'Drawing - {self.x}, {self.y}')


p1 = Point(10, 20)
p1.x = 100
p1.y = 50
print(p1.x)
print(p1.y)
p1.draw()
