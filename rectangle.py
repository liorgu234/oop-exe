from shapes import *
import math


class rec(shape):

    def __init__(self, color="", side1=1, side2=1):
        area = side1*side2
        grif = side1 * 2 + side2 * 2
        super().__init__(color, area, grif)
        self.side1 = side1
        self.side2 = side2

    def getside1(self):
        return self.side1

    def getside2(self):
        return self.side2

