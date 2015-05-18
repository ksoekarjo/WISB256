v= float(input())
g= float(input())
d= float(input())

import math
a = 0.5*math.asin(g*d/v**2)
a = "{0:.2f}".format(a)
print(a)
