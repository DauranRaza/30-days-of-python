# Write an example for different python data types such as Numeric(Int, float, complete), string, boolean,
# list, tuple, set and dictionary

#x = 3
#print("x is ", type(x))

#y = 3.3
#print("y is ", type(y))

#z = 3j
#print("z is ", type(z))

#s = "abc"
#print("s is ", type(s))

#b = True
#print("b is ", type(b))

#l = ["banana", "apple", "orange"]
#print("l is ", type(l))

#t = ("banana", "apple", "orange")
#print("t is ", type(t))

#e = {"banana", "apple", "orange"}
#print("e is ", type(e))

#d = {"name" : "john", "age" : 36}
#print(d)
#print ("d is ", type(d))

# find Euclidean distance between (2,3) and (10,8)

import math

p = (2,3)
q = (10,8)

d = math.sqrt((((q[0] - p[0])**2) + ((q[1] - p[1]))**2))

print("The euclidean distan between (2,3) and (10,8) is ", + d)