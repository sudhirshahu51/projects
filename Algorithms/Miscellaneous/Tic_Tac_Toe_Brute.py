'''#!/usr/bin/env python3'''


import random


class Game:             # Game Class
    def __init__(self, play):
        self.moves = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
                      8: ' ', 9: ' '}
        self.active_player = play         # The player whose chance is next
        self.empty_sites = list(range(1, 10))   # contains the possible moves
        self.full_sites = []                    # occupied sites
        self.last_move = []

    def move(self, pos):
        assert type(pos) == int, "Something" "Wrong"
        if pos in self.empty_sites:
            self.moves[pos] = self.active_player
            self.empty_sites.remove(pos)
            self.full_sites.append(pos)
            self.last_move.append(pos)
            if self.active_player == 'X':       # next chance is of O
                self.active_player = 'O'
            elif self.active_player == 'O':
                self.active_player = 'X'        # next chance is of X
        else:
            print('Occupied Space or not your turn')

    def main_frame(self):                       # To print the game board
        d = self.moves
        print("%s|%s|%s" % (d[1], d[2], d[3]))
        print("-----")
        print("%s|%s|%s" % (d[4], d[5], d[6]))
        print("-----")
        print("%s|%s|%s" % (d[7], d[8], d[9]))
        print("-----")

    def game_over(self):                    # Find if the game is over or not
        d = self.moves
        flag = False
        value = 0
        for i in self.full_sites:
            if i != 5:
                if d[5] == d[i] == d[10-i] != ' ':    # diagonal and middle row
                    flag = True                       # col
                    value = d[5]
                    break
        if d[1] == d[2] == d[3] != ' ':         # top row
            flag = True
            value = d[1]
        elif d[7] == d[8] == d[9] != ' ':       # last row
            flag = True
            value = d[7]
        elif d[1] == d[4] == d[7] != ' ':       # left column
            flag = True
            value = d[1]
        elif d[3] == d[6] == d[9] != ' ':       # right column
            flag = True
            value = d[3]
        if flag:
            print('game over\n%s WINS\n' % value)
            return True, value
        else:
            if len(self.empty_sites) == 0:      # If the game is draw
                print('Game draw')
                return True, 'draw'
            return False, 0

    def neighbour(self, pos):
        tmp = []
        if pos == 1:
            tmp = [2, 4]
        if pos == 2:
            tmp = [1, 3]
        if pos == 3:
            tmp = [2, 6]
        if pos == 4:
            tmp = [1, 7]
        if pos == 5:
            tmp = [1, 2, 3, 4, 6, 7, 8, 9]
        if pos == 6:
            tmp = [3, 9]
        if pos == 7:
            tmp = [4, 8]
        if pos == 8:
            tmp = [7, 9]
        if pos == 9:
            tmp = [8, 6]
        if len(tmp) > 2:
            return tmp
        else:
            return tmp + [5]


def check_fork(x):
    flag = False
    for i in [1, 3]:
        if g.moves[i] == g.moves[10-i] == x and len(g.empty_sites) == 6:
            flag = True
            for _ in range(4):
                tmp = [2, 4, 6, 8][random.randint(0, 3)]
                if tmp in g.empty_sites:
                    g.move(tmp)
                    break
    for i in [1, 3, 7, 9]:
        if g.moves[5] == g.moves[i] == x and len(g.empty_sites) == 6:
            flag = True
            for _ in range(4):
                tmp = [1, 3, 7, 9][random.randint(0, 3)]
                if tmp in g.empty_sites:
                    g.move(tmp)
                    break
    for i in [2, 4, 6, 8]:
        if g.moves[5] == g.moves[i] == x and len(g.empty_sites) == 6:
            flag = True
            g.move(10 - g.last_move[-1])
    return flag


def next_move():
    print('Computer\'s turn')
    if going_to_win(computer):
        pass
    else:
        if going_to_win(player):
            pass
        else:
            cf = create_fork()
            if len(g.empty_sites) == 7 and check_fork(player):
                pass
            elif len(g.empty_sites) == 7 and cf[0]:
                tmp = create_fork()[1]
                g.move(cf[2])
                g.main_frame()
                print('What\' your move??')
                g.move(int(input()))
                g.main_frame()
                print('Computer\' Turn')
                cf2 = create_fork_2(tmp)
                if cf2[0]:
                    a = cf2[1]
                    if a == 0:
                        pass
                    else:
                        g.move(a)
                else:
                    print('1')
                    g.move(g.empty_sites[random.randint(0, len(g.empty_sites)-1)])
            else:
                print('2')
                g.move(g.empty_sites[random.randint(0, len(g.empty_sites)-1)])
    g.main_frame()


def create_fork():
    flag = False
    case = None
    mv = None
    tmp = g.last_move[0]
    if len(g.empty_sites) == 7:
        if tmp in [1, 3, 7, 9]:
            if g.last_move[-1] == 5:
                flag = True
                mv = 10 - tmp
                case = 1
            else:
                flag = True
                mv = 5
                case = 2
        elif tmp in [2, 4, 6, 8]:
            if g.last_move[-1] == 5:
                for i in g.neighbour(g.last_move[0]):
                    for j in g.neighbour(i):
                        if j in g.empty_sites:
                            flag = True
                            mv = j
                            case = 3
                        else:
                            pass
            else:
                flag = True
                mv = 5
                case = 4
        elif tmp == 5:
            if g.last_move[-1] in [1, 3, 7, 9]:
                flag = True
                case = 5
                mv = 10 - g.last_move[-1]
            else:
                flag = True
                case = 6
                if g.last_move[-1] == 2:
                    mv = 3
                elif g.last_move[-1] == 4:
                    mv = 1
                elif g.last_move[-1] == 6:
                    mv = 9
                else:
                    mv = 7
    return flag, case, mv


def create_fork_2(case):
    flag = False
    no = None
    if len(g.empty_sites) == 5:
        if going_to_win(player):
            flag = True
            no = 0
            pass
        elif case == 1:
            if g.last_move[-1] in [1, 3, 7, 9]:
                flag = True
                no = 10 - g.last_move[-1]
        elif case == 2:
            for i in [1, 3, 7, 9]:
                if i in g.neighbour(g.last_move[-1]) or\
                                i in g.neighbour(g.last_move[-3]) and\
                        i in g.full_sites:
                    pass
                else:
                    flag = True
                    no = i
        elif case == 3:
            for i in g.neighbour(g.last_move[0]):
                for j in g.neighbour(i):
                    if j == i and j in g.empty_sites:
                        flag = True
                        no = j
        elif case == 4:
            for i in g.neighbour(g.last_move[0]):
                if i in g.empty_sites:
                    flag = True
                    no = i
        elif case == 5:
            for i in g.neighbour(g.last_move[-2]):
                if i in g.empty_sites:
                    for j in g.neighbour(i):
                        flag = True
                        no = j
        elif case == 6:
            for i in g.neighbour(g.last_move[-2]):
                for j in g.neighbour(i):
                    if j in g.empty_sites:
                        flag = True
                        no = j
    return flag, no


def going_to_win(x):        # Check if player x is winning or lossing
    flag = False            # If True return the move by which it wins or loss
    for i in [0, 3, 6]:
        if g.moves[i+1] == g.moves[i+2] == x and g.moves[i+3] == ' ':
            flag = True
            g.move(i+3)
        elif g.moves[i+2] == g.moves[i+3] == x and g.moves[i+1] == ' ':
            flag = True
            g.move(i+1)
        elif g.moves[i+1] == g.moves[i+3] == x and g.moves[i+2] == ' ':
            flag = True
            g.move(i+2)
    for i in [1, 2, 3]:
        if g.moves[i] == g.moves[i+3] == x and g.moves[i+6] == ' ':
            flag = True
            g.move(i+6)
        elif g.moves[i+3] == g.moves[i+6] == x and g.moves[i] == ' ':
            flag = True
            g.move(i)
        elif g.moves[i] == g.moves[i+6] == x and g.moves[i+3] == ' ':
            flag = True
            g.move(i+3)
    for i in [1, 3]:
        if g.moves[i] == g.moves[10-i] == x and g.moves[5] == ' ':
            flag = True
            g.move(5)
        if g.moves[i] == g.moves[5] == x and g.moves[10-i] == ' ':
            flag = True
            g.move(10-i)
        if g.moves[10-i] == g.moves[5] == x and g.moves[i] == ' ':
            flag = True
            g.move(i)
    return flag


print('Human vs Computer')
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")
print("-----")
ans = input('Do you want to play the game (yes or no)\n')
while ans == 'yes':
    player = input('Player chose: X or O\n')
    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'
    tmp = random.randint(0, 1)
    if tmp == 1:
        print('Player 1 will go first')
        g = Game(player)
        print('What\' your move?')
        g.move(int(input()))
        g.main_frame()
        if g.last_move[-1] in [1, 2, 3, 4, 6, 7, 8, 9]:
            g.move(5)
        else:
            g.move([1, 3, 7, 9][random.randint(0, 3)])
        print('Computer\' turn')
        g.main_frame()
    else:
        print('Computer will go first')
        g = Game(computer)
        g.move(g.empty_sites[random.randint(0, 8)])
        g.main_frame()
    while True:
        if g.active_player == player:
            print('What\' your move?')
            a = int(input())
            g.move(a)
            g.main_frame()
        else:
            next_move()
        val = g.game_over()
        if val[0]:
            break
        else:
            pass
    ans = input('Do you want to play the game (yes or no)')
