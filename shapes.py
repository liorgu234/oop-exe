class shape:

    def __init__(self, color=None, area=1, girf=1):
        self.color = color
        self.area = area
        self.girf = girf

    def scolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

    def sarea(self, area):
        self.area = area

    def getarea(self):
        return self.area

    def sgrif(self, grif):
        self.girf = grif

    def getgrif(self):
        return self.girf


"""'shape1'"" = shape("blue", 5, 7)
print(shape1.getcolor())
shape1.sarea(5)
print(shape1.getarea())"""
