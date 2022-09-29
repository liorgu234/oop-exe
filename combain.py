from gigo import *
from rectangle import *


def combine(rec, square):
    if rec.getside2() == square.getside() and square.getcolor() == rec.getcolor():
        newshapearea = (rec.getside2() + square.getside()) * square.getside()
        newshapegirf = square.getside() * 4 + rec.getside2() * 2
        newshape = shape(rec.getcolor(), newshapearea(), newshapegirf())
        return newshape
    elif rec.getside1() == square.getside and square.getcolor() == rec.getcolor():
        newshapearea = (rec.getside1 + square.getside()) * square.getside()
        newshapegirf = square.getside() * 4 + rec.getside1() * 2
        newshape = shape(rec.getcolor(), newshapearea, newshapegirf)
        return newshape
