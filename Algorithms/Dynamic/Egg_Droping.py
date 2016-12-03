# You've certain number of floors and certain no. of eggs
# Find the minimum number of attempts to find out that eggs break from which floor
# For ex if you've two eggs and three floors then it can be found out in 2 attempts


def egg_droping(floor, eggs):
    table = [[0 for _ in range(1, floor+1)] for __ in range(1, eggs+1)]
    for i in range(1, floor+1):
        table[0][i] = i
    


'''
floor = int(input('Enter the no. of floors'))
eggs = int(input('Enter the no. of eggs'))
'''
egg_droping(6, 2)