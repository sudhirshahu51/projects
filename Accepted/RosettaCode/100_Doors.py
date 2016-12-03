''' Only the perfect squares will remain open'''

class Door:
    def __init__(self, key):
        self.state = 'CLOSE'
        self.id = key

    def visit(self):
        if self.state == 'CLOSE':
            self.state = 'OPEN'
        else:
            self.state = 'CLOSE'
my_list = []
for i in range(0, 101):
    my_list.append(Door(i))
for i in range(1, 101):
    for j in range(0, len(my_list), i):
        my_list[j].visit()
for i in my_list:
    print(i.id, i.state)