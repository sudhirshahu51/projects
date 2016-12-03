from random import randint


class GameBoard:
    def __init__(self):
        self.last_items = {}
        self.items = {}
        self.last_empty = {}
        self.empty = {}
        self.build_empty()
        self.build_game_first()
        self.last_score = 0
        self.score = 0

    def build_empty(self):
        for i in range(1, 17):
            self.empty[i] = True
            self.items[i] = 0
            self.last_items[i] = 0
            self.last_empty[i] = True

    def main_frame(self):
        d = {}
        for a, b in self.items.items():
            d[a] = self.format(b)
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[1], d[2], d[3], d[4]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[5], d[6], d[7], d[8]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[9], d[10], d[11], d[12]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[13], d[14], d[15], d[16]))
        print('+-----+-----+-----+-----+')

    def format(self, ch):
        assert type(ch) == int, 'Wrong format'
        if ch == 0:
            return '     '
        elif ch in [2, 4, 8]:
            return '  ' + str(ch) + '  '
        elif ch in [16, 32, 64]:
            return '  ' + str(ch) + ' '
        elif ch in [128, 256, 512]:
            return ' ' + str(ch) + ' '
        elif ch in [1024, 2048, 4096]:
            return ' ' + str(ch)

    def build_game_first(self):
        flag = False
        while not flag:
            tmp = randint(1, 16)
            tmp1 = self.empty[tmp]
            if tmp1:
                self.items[tmp] = 2
                self.empty[tmp] = False
                flag = True

    def build_game(self):
        flag = False
        if self.empty == self.last_empty:
            print('Your move did not do anything')
        else:
            while not flag:
                tmp = randint(1, 16)
                tmp1 = self.empty[tmp]
                if tmp1:
                    self.items[tmp] = 2
                    self.empty[tmp] = False
                    flag = True

    def undo(self):
        for i in self.items.keys():
            self.items[i] = self.last_items[i]
            self.empty[i] = self.last_empty
        self.score = self.last_score

    def game_over(self):
        tmp = 0
        for i in self.empty.values():
            if i:
                tmp += 1
        if tmp == 0:
            return True
        else:
            return False

    def move_spaces(self, arrow):
        if arrow == 'w':
            for j in [1, 5, 9]:
                for i in range(j+4, j+8):
                    if self.items[i-4] == 0:
                        self.items[i-4], self.items[i] = \
                            self.items[i], self.items[i-4]
                        self.empty[i], self.empty[i-4] = \
                            self.empty[i-4], self.empty[i]
        if arrow == 's':
            for j in [13, 9, 5]:
                for i in range(j-4, j):
                    if self.items[i+4] == 0:
                        self.items[i+4], self.items[i] = \
                            self.items[i], self.items[i+4]
                        self.empty[i], self.empty[i+4] = \
                            self.empty[i+4], self.empty[i]
        if arrow == 'a':
            for j in [13, 14, 15]:
                for i in range(j-11, j+2, 4):
                    if self.items[i-1] == 0:
                        self.items[i-1], self.items[i] = \
                            self.items[i], self.items[i-1]
                        self.empty[i], self.empty[i-1] = \
                            self.empty[i-1], self.empty[i]
        if arrow == 'd':
            for j in [14, 15, 16]:
                for i in range(j-13, j, 4):
                    if self.items[i+1] == 0:
                        self.items[i+1], self.items[i] = \
                            self.items[i], self.items[i+1]
                        self.empty[i], self.empty[i+1] = \
                            self.empty[i+1], self.empty[i]

    def move(self, arrow):
        for i in self.items.keys():
            self.last_items[i] = self.items[i]
            self.last_empty[i] = self.empty[i]
        self.last_score = self.score
        if arrow == 'w':
            self.move_spaces(arrow)
            self.move_spaces(arrow)
            for j in [1, 5, 9]:
                for i in range(j+4, j+8):
                    if self.items[i] == self.items[i-4] != 0:
                        self.items[i-4] = 2 * self.items[i]
                        self.score += self.items[i-4]
                        self.items[i] = 0
                        self.empty[i] = True
            self.move_spaces(arrow)
        if arrow == 's':
            self.move_spaces(arrow)
            self.move_spaces(arrow)
            for j in [13, 9, 5]:
                for i in range(j-4, j):
                    if self.items[i] == self.items[i+4]:
                        self.items[i+4] = 2 * self.items[i]
                        self.score += self.items[i+4]
                        self.items[i] = 0
                        self.empty[i] = True
            self.move_spaces(arrow)
        if arrow == 'a':
            self.move_spaces(arrow)
            self.move_spaces(arrow)
            for j in [13, 14, 15]:
                for i in range(j-11, j+2, 4):
                    if self.items[i] == self.items[i-1]:
                        self.items[i-1] = 2 * self.items[i]
                        self.score += self.items[i-1]
                        self.items[i] = 0
                        self.empty[i] = True
            self.move_spaces(arrow)
        if arrow == 'd':
            self.move_spaces(arrow)
            self.move_spaces(arrow)
            for j in [14, 15, 16]:
                for i in range(j-13, j, 4):
                    if self.items[i] == self.items[i+1]:
                        self.items[i+1] = 2 * self.items[i]
                        self.score += self.items[i+1]
                        self.items[i] = 0
                        self.empty[i] = True
            self.move_spaces(arrow)


print('Hello user\nEnter w, a, s, d for movement and u for undo')
game = GameBoard()
game.main_frame()
while True:
    x = str(input())
    if game.game_over():
        print('Game Over')
        break
    if x in ['w', 'a', 's', 'd']:
        game.move(x)
        game.build_game()
        game.main_frame()
        print('SCORE', game.score)
    elif x == 'u':
        game.undo()
        game.main_frame()
        print('SCORE', game.score)
    else:
        break
