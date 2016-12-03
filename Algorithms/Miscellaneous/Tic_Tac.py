#!/usr/bin/env python3
import random


class Game:
    def __init__(self, player):
        self.moves = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ',
                      8: ' ', 9: ' '}
        self.active_player = player
        self.empty_sites = list(range(1, 10))
        self.full_sites = []

    def move(self, pos):
        assert type(pos) == int, "Something" "Wrong"
        if pos in self.empty_sites:
            self.moves[pos] = self.active_player
            self.empty_sites.remove(pos)
            self.full_sites.append(pos)
            if self.active_player == 'X':
                self.active_player = 'O'
            elif self.active_player == 'O':
                self.active_player = 'X'
        else:
            print('Occupied Space or not your turn')

    def main_frame(self):
        d = self.moves
        print("%s|%s|%s" % (d[1], d[2], d[3]))
        print("-----")
        print("%s|%s|%s" % (d[4], d[5], d[6]))
        print("-----")
        print("%s|%s|%s" % (d[7], d[8], d[9]))
        print("-----")

    def game_over(self):
        d = self.moves
        flag = False
        value = 0
        for i in self.full_sites:
            if i != 5:
                if d[5] == d[i] == d[10-i] != ' ':
                    flag = True
                    value = d[5]
                    break
        if d[1] == d[2] == d[3] != ' ':
            flag = True
            value = d[1]
        elif d[7] == d[8] == d[9] != ' ':
            flag = True
            value = d[7]
        elif d[1] == d[4] == d[7] != ' ':
            flag = True
            value = d[1]
        elif d[3] == d[6] == d[9] != ' ':
            flag = True
            value = d[3]
        if flag:
            print('game over\n%s WINS\n' % value)
            return True
        else:
            if len(self.empty_sites) == 0:
                print('Game draw')
                return True
            return False

try:
    print('This game is for Human vs Human')
    print("1|2|3")
    print("-----")
    print("4|5|6")
    print("-----")
    print("7|8|9")
    print("-----")
    ans = input('Do you want to play the game (yes or no)\n')
    while ans == 'yes':
        player_1 = input('Player 1 chose: X or O\n')
        if player_1 == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'
        tmp = random.randint(0, 1)
        if tmp == 1:
            print('Player 1 will go first')
            g = Game(player_1)
        else:
            print('Player 2 will go first')
            g = Game(player_2)
        while True:
            print('What\' your move? ', g.active_player)
            a = int(input())
            g.move(a)
            g.main_frame()
            val = g.game_over()
            if val:
                break
            else:
                pass
        ans = input('Do you want to play the game (yes or no)')
except Exception as er:
    print('Something big happened: ' + str(er))
