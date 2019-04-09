#!/usr/bin/env python3

"""
     This script is going to takes two balls and computes if they are colliding.
"""

import math

def ball_collide(b1,b2):
    """
        1. The function ball_collide(b1, b2) will takes two balls as parameters and computes if they are colliding.
        2. This function accepts only two parameters and uses tuple unpacking.
        :param b1: First Ball
        :param b2: Second Ball
        :return: a Boolean saying whether or not the balls are colliding

    """
    # formula to calculate distance among centers of two balls.
    distance = math.sqrt(((float(b2[0])-float(b1[0]))**2)+((float(b2[1])-float(b1[1]))**2)+((float(b2[2])-float(b1[2]))**2))
    # check if distance is greater than sum of radious
    if distance > float(b1[3])+float(b2[3]):
        return False
    else:
        return True

# Assign the test file from the url to getFile veriable.
getFile = "balltest.txt"

# open the text filet
with open(getFile) as textFile:
    test_cases = textFile.readlines()
    # Loop over each element in the text file.
    for el in test_cases:
        el = el.strip()
        balls = el.split(':')
        temp1 = balls[0].split(',')
        temp2 = balls[1].split(',')
        ball1 =(temp1[0], temp1[1], temp1[2], temp1[3])
        ball2 =(temp2[0], temp2[1], temp2[2], temp2[3])
        # Print out line format and values.
        print(el)
        # Print out ball1 and ball2 collosion.
        print(ball_collide(ball1,ball2))

def main():
    """Run the script"""
    b1 = ()
    b2 = ()
    try:
        ball_collide(b1, b2)
    except IndexError:
        return -1


if __name__ == "__main__":
    main()
    exit(0)
