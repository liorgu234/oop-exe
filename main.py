from shapes import *
from gigo import *
from shapesherhouse import *


def main():
    pandora = Container()
    pandoras_box = pandora.genrate(100)
    print("total area: " + str(pandora.sum_area(pandoras_box)))
    print("total paremitar: " + str(pandora.sum_perimater(pandoras_box)))
    print("colors: " + pandora.count_colors(pandoras_box))


if __name__ == "__main__":
    main()
