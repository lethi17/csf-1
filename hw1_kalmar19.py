# Name: Mary Kallem
# Evergreen Login: kalmar19
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408
p = math.sqrt(b**2 - 4 * a * c)
q = (2 * a)

x = (-b + p) / q
y = (-b - p) / q

print x , y

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
from hw1_test import *
print a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f


###
### Problem 3
###

print "Problem 3 solution follows:"

print ((a and b) or (not c) and not (d or e or f))


###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").