x=str(input("Enter a string to check its length by entering '#' in the last\n"))
for i in range(1000):
    if x[i]=='#':
        n=i
        break
    else:
        continue
print(n)
input('press enter to exit')