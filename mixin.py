class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Serialize:
    def serialize(self):
        return (",".join(f"{key}={value}" for key, value in self.__dict__.items()))


class Rectangele(Shape, Serialize):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height


r = Rectangele(1, 2, 3, 4)
print(r.serialize())
