from combain import *
from Circle import *
import random


class Container:

    def __init__(self):
        self.__container = []

    def genrate(self, x=1):  # calls the random shape func for a number of times and adds the new shapes to a list
        while x != 0:
            self.__container.append(self.random_shape())
            x = x - 1
        return self.__container  # returns the list

    def random_shape(self):  # creates a random shape with random attributes
        rshape = random.randrange(0, 3)
        if rshape == 0:
            new_shape = rec(self.random_color(), random.randrange(1, 10), random.randrange(1, 10))
            return new_shape
        elif rshape == 1:
            new_shape = square(self.random_color(), random.randrange(1, 10))
            return new_shape
        elif rshape == 2:
            new_shape = circle(self.random_color(), random.randrange(1, 10))
            return new_shape

    def sum_area(self, shapelist):  # calculate the sum of all the areas
        sum_area = 0
        for i in shapelist:
            sum_area += int(i.getarea())
        return sum_area

    def sum_perimater(self, shapelist):  # calculate the sum of all the perimeters
        sum_pera = 0
        for i in shapelist:
            sum_pera += i.getgrif()
        return sum_pera

    def count_colors(self, shapelist):  # count how many shapes are in each color
        red = 0
        blue = 0
        green = 0
        yellow = 0
        purple = 0
        for x in shapelist:
            if x.getcolor() == "blue":
                blue = blue + 1
            elif x.getcolor() == "red":
                red = red + 1
            elif x.getcolor() == "green":
                green = green + 1
            elif x.getcolor() == "yellow":
                yellow = yellow + 1
            elif x.getcolor() == "purple":
                purple = purple + 1
            else:
                print(x.getcolor)
        return "red: " + str(red) + " blue: " + str(blue) + " green: " + str(green) + " yellow: " + str(yellow) + \
               " purple: " + str(purple)

    def random_color(self):  # returns a random color
        rcolor = random.randrange(0, 5)
        if rcolor == 0:
            return "blue"
        elif rcolor == 1:
            return "red"
        elif rcolor == 2:
            return "green"
        elif rcolor == 3:
            return "yellow"
        elif rcolor == 4:
            return "purple"
