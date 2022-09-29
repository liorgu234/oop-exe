from shapes import *
import math
from rectangle import *


class square(rec):

    def __init__(self, color=None, side=1):
        super().__init__(color, side, side)
        self.side = side

    def getside(self):
        return self.side