from array import array
import math

class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            self.array = array('d',[0]*args[0])
        else:
            if type(args[1]) == float or type(args[1]) == int:
                self.array = array('d',[args[1]]*args[0])
            else:
                self.array = array('d',args[1])


    def __str__(self):
        values = [str(i) for i in self.array]
        return '\n'.join(values)


    def lincomb(self,other,alpha,beta):
        a = array('d',[0]*len(self.array))
        for i in range(len(self.array)):
            a[i] = alpha*self.array[i]
        b = array('d',[0]*len(other.array))
        for i in range(len(other.array)):
            b[i] = beta*other.array[i]
        c = array('d',[0]*len(a))
        for i in range(len(a)):
            c[i] = a[i] + b[i]
        return Vector(len(c),c)

    
    def scalar(self, alpha):
        a = array('d',[0]*len(self.array))
        for i in range(len(self.array)):
            a[i] = alpha*self.array[i]
        return Vector(len(a),a)


    def inner(self, other):
        a = 0
        i = 0
        while i<len(self.array):
            a += self.array[i]*other.array[i]
            i += 1
        return a

    def norm(self):
        return math.sqrt(self.inner(self))
