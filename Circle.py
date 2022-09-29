from shapes import *
import math


class circle(shape):

    def __init__(self, color=None, radios=1):
        area = math.pi * (radios*radios)
        grif = radios * 2 * math.pi
        self.grif=grif
        super().__init__(color, area, grif)
