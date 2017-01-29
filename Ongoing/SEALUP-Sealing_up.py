import math
def dl(x,y,x1,y1):
  return math.sqrt((x-x1)**2+(y-y1)**2)

t=int(input())
for i in range(t):
  sz=int(input())
  aa=list(map(int,input().split()))
  a1=aa[0]
  b1=aa[1]
  ds=[]
  for j in range(sz-1):
    a,b=map(int,input().split())
    ds.append(dl(a,b,aa[0],aa[1]))
    aa[0]=a
    aa[1]=b

  ds.append(dl(a1,b1,aa[0],aa[1]))
  nm=int(input())
  for k in range(nm):
    a,b=map(int,input().split())
  cnt=0
  for k in range(len(ds)):
    cnt+=math.ceil(ds[k]/a)
    print(math.ceil(ds[k]/a))

  print(b*cnt)