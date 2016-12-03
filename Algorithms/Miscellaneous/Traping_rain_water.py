# To find out the maximum rain water that can be traped between the bar of width 1
# file:///D:/WORK/Offline/geeksforgeeks_latest/geeks/www.geeksforgeeks.org/trapping-rain-water/index.html


def maxm(lst):
    if isinstance(lst, list):
        if len(lst) >= 1:
            return max(lst)
        else:
            return 0


bar = list(map(int, input('Enter the height of bars with spaces').split()))
l = len(bar)
water = 0
for i in range(l):
    x = maxm(bar[0:i])
    y = maxm(bar[i+1:l])
    if x > bar[i] < y:
        water += min(x, y) - bar[i]
print(water)