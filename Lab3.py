n = 100

series = 'sum'

x = 0
y = 0
z = 1
summon = 0

if series == 'fibonacci':
   for i in range(n - 1):
       x = y
       y = z
       z = x + y
   print z

elif series == 'sum':
    for i in range(n + 1):
        summon += (3 * i)
    print summon
 
else:
    print "Invalid String"