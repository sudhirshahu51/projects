n = int(input())
array = list(map(int, input().split()))
adder = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (array[i] & array[j] == array[j]) or\
                (array[i] & array[j] == array[i]):
            adder += max(array[i:j+1])
print(adder)