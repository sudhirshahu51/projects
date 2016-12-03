x=int(input("Enter a no. whose length is to be found out"))
for i in range(1000):
    if int(x/10**i)==0:
        break
    else:
        n=i+1
        continue
print("length of the entered no. is {n}".format(**locals()))
