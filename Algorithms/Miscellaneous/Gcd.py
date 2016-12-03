# To find the greatest common divisor

def gcd(x,y):
    if x == 0:
        return y
    else:
        return gcd(y%x, x)
