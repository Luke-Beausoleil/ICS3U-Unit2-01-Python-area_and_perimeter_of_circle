#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program calculates the area and the perimeter of a circle
#   with radius 15 mm

import math


def main():
    print("If circle has radius: ")
    print("15 mm")
    print("")
    print("The Area is: {} mm²".format(math.pi * 15 ** 2))
    print("")
    print("The perimeter is: {} mm".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
