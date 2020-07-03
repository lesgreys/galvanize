from itertools import zip_longest


class Polynomial(object):

    def __init__(self, coefficient):
        self.coefficient = coefficient


    def __repr__(self):
        #return f'{self.coefficient[-1]}x^{len(self.coefficient)-1}x'
        x_lst= []
        for num, co in enumerate(self.coefficient):
            if num == 0:
                x_lst.append(str(self.coefficient[0]))
            else:
                x_lst.append(f'{co}x^{num}')

        return ' + '.join(x_lst[::-1])
    # def __init__(self, degree):
    
    def evaluate(self, x):

        sum_ = 0

        for num, co in enumerate(self.coefficient):
            sum_ += co*x**num
        return sum_

    def __add__(self, other):
        z = []
        for i, j in zip_longest(self.coefficient, other.coefficient,fillvalue=0):
            z.append(i+j)
        return Polynomial(z)


    def __sub__(self, other):
        z = []
        for i, j in zip_longest(self.coefficient, other.coefficient,fillvalue=0):
            z.append(i-j)
        return Polynomial(z)

    def __neg__(self):
        n = []

        for coef in self.coefficient:
            n.append(-coef)
        return n

    def __mul__(self,other):
        z = [0] * (len(self.coefficient) + len(other.coefficient) + 1)
        for num1, coef1 in enumerate(self.coefficient):
            for num2, coef2 in enumerate(other.coefficient):
                z[num1+num2] += coef1*coef2
        return Polynomial(z)
            

    def __eq__(self, other):
        return self.coefficient == other.coefficient

    def diff_poly(self):
        result = []

        for num in range(1,len(self.coefficient)):
            result.append(num * self.coefficient[num])
        return Polynomial(result)

    def inte(self):
        result = []

        for num in range(len(self.coefficient)):
            result.append(round(self.coefficient[num] / (num+1),2))
        return Polynomial(result)




    

if __name__ == '__main__':
    test = Polynomial([1,2,3,4])
    test2 = test.evaluate(2)
    test3 = Polynomial([4,3,2,1])
    test4 = test3.evaluate(2)
    test5 = test3.diff_poly()
    test6 = test3.inte()
    print(test3)
    print(test2)
    print(test+test3)
    print(test-test3)
    print(test==test3)
    print(test*test3)
    print(test5)
    print(test6)
