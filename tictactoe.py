import random


class board:
    def __init__(self, positions, player_pos, bot_pos):
        self.positions = positions
        self.player_pos = player_pos
        self.bot_pos = bot_pos

    def check_win(self):
        pass
        # todo

    def check_draw(self):
        if any(item in [0, 1, 2, 3, 4, 5, 6, 7, 8] for item in self.positions):
            return False
        else:
            return True

    def cycle(self):
        # awwww hell yeah, list comprehension for possible moves
        possibilities = [works for works in self.positions if type(works) == int if works not in self.bot_pos if
                         works not in self.player_pos]

        # show the board
        print('''
                            {}-{}-{}
                            {}-{}-{}
                            {}-{}-{}
                            '''.format(self.positions[0], self.positions[1], self.positions[2],
                                       self.positions[3], self.positions[4], self.positions[5],
                                       self.positions[6], self.positions[7], self.positions[8]))

        checks_out = False

        while not checks_out:
            where = int(input('kuhu käid ' + str(possibilities) + ': '))
            if where in possibilities:
                checks_out = True
                self.player_pos.append(where)
                self.positions[where] = 'x'
            else:
                print('nope')
                continue

        random.shuffle(possibilities)
        bot_where = possibilities[0]

        self.bot_pos.append(bot_where)
        self.positions[bot_where] = 'o'


ok = board([0, 1, 2, 3, 4, 5, 6, 7, 8], [], [])


win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

while True:
    if ok.check_win():
        print('sina v tema voitis')
        exit()
    elif ok.check_draw():
        print('viik')
        exit()
    else:
        ok.cycle()
