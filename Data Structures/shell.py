class N:
    def __init__(self):
        self.root = None
    
    def p(self):
        if self.root:
            print('helo')
        else:
            print('yelo')


n = N()
n.p()