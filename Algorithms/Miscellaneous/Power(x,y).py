# To find the x power y in O(log n) time in comparison to O(n) time for classical method
# x can be float and y can be negative


def power(x, y):
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            return power(x, y//2)*power(x, y//2)
        else:
            if y > 0:
                return power(x, y//2)*power(x, y//2)*x
            else:
                return power(x, y//2)*power(x, y//2)/x


if __name__ == '__main__':
    x = float(input('Enter the base'))
    y = float(input('Enter the power'))
    ans = power(x,y)
    print(ans)