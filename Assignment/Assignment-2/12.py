a, b = map(int, input('Enter the no. to be arithmetically solved').split())
print('1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Modulo')
x = int(input())
if x == 1:
    c = a + b
if x == 2:
    c = a - b
if x == 3:
    c = a * b
if x == 4:
    c = a / b
if x == 5:
    c = a % b
print(c)
