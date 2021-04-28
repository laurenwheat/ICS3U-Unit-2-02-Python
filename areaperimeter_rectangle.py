#!/usr/bin/env python3

# Created by: Lauren
# Created on: April 2021
# This program calculates the area and perimeter of a rectangle
#    with length and width inputted from the user

import math


def main():
    # this function calculates the area and perimeter of a rectangle

    # print("Enter the length of the rectangle")
    # print("Enter the width of the rectangle")
    length = int(input("Enter the length of a regtangle "))
    width = int(input("Enter the width of a rectangle "))
    print("The area is {}".format(length*width))
    print("The perimeter is {}".format(2*(length+width)))


if __name__ == "__main__":
    main()
