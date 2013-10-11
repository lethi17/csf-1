# Name: Mary Kallem
# Evergreen Login: kalmar19
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

# Note that x = range (n + 1), sum(x) would as well.

import hw2_test

a = 1
b = 0

while (a <= hw2_test.n):
    b = a + b
    a = a + 1 # produces next number in sequence to be added
print b
#I can't believe I figured that out...

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for i in range(2,11):
    print 1.0/i

###
### Problem 3
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(n + 1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
x = 1

for i in range(1, n + 1): 
    x = x * i
print x


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10

for i in range(numlines, 0, -1):
    x = 1
    for j in range(1, i + 1):
        x = x * j
    print x
    

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
k = 1

for i in range(1, numlines + 1):
    x = 1
    for j in range(1, i + 1):
        x = x * j
    recip = 1.0/x
    k = k + recip
print k 

###
### Collaboration
###

# I worked with Robin on problems 1-4, and then Alex the tutor was an invaluable resource for 5 and 6. He was so great!
# Oh, and I sent a few panicked, verging-on-tear texts to Amber. Sorry about that, Amber.

###
### Reflection
###

# ... This assignment took forever, primarily because I got a little hysterical during problem 5. I'm wary of admitting that, primarily
# ... because I'm one of like, 6 women in the class and feel pressure to save face. Yadda yadda, gaslighting, etc.
# ... I wish we had time to go over for loops in class--that would have helped a lot. Also, I'm a creature of repetition. If I have multiple
# ... problems to practice the same lesson/function/operation/whatever, I'll understand and remember it better. Optional problems would be great.