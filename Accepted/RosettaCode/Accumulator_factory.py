'''Accumulating function is kind of function that returns function in return value
and hence making it kind of a object
'''


def accumulator(sum):
    def f(n):
        print(f.sum)
        f.sum += n
        return f.sum
    f.sum = sum
    accumulator.t = 3
    return f


x = accumulator(1)
x(5)
w = x(2)
print(w)
