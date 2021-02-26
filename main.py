from time import sleep
import random


class Item:
    def __init__(self, dmg, name):
        self.dmg = dmg
        self.name = name


item_list = [Item(10, 'branch'), Item(20, 'wooden sword'), Item(20, 'wooden sword'), Item(30, 'rusty sword'), Item(30,
             'rusty sword'), Item(50, 'straight sword'), Item(60, 'greatsword'), Item(70, 'enchanted branch')]

random.shuffle(item_list)

weapon = item_list[0]


class Entity:
    def __init__(self, hp, xp, mana, defense, item, name):
        self.hp = hp
        self.xp = xp
        self.mana = mana
        self.defense = defense
        self.item = item
        self.name = name

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False


class Enemy(Entity):
    def attack(self):
        print(Enemy.hp)


foe_list = [Enemy(100, 50, 20, 1, weapon, 'skeleton'), Enemy(100, 50, 20, 1, weapon, 'skeleton'), Enemy(100, 50, 20, 1,
            weapon, 'skeleton'), Enemy(200, 75, 10, 3, weapon, 'zombie'), Enemy(200, 75, 10, 3, weapon, 'zombie'),
            Enemy(150, 100, 50, 5, weapon, 'knight'), Enemy(50, 80, 0, 25, weapon, 'corrosive slime')]

random.shuffle(foe_list)

enchanted_greatsword = Item(150, 'enchanted greatsword')

foe_list.append(Enemy(500, 0, 250, 15, enchanted_greatsword, 'lord'))


class Player(Entity):
    level = 0

    def level_up(self):
        if self.xp >= (100 + self.level * 10):
            self.hp += 25
            self.mana += 25
            self.level += 1
            print('You\'ve gained 25HP, 25 mana and 1 level.')

    def status(self):
        print('Your weapon, ' + str(protagonist.item.name) + ', deals ' + str(self.item.dmg) + ' damage.')
        sleep(1)
        print('You have ' + str(self.mana) + ' mana.')
        sleep(1)
        print('You have ' + str(self.hp) + ' HP.')
        sleep(1)
        print('You have ' + str(self.defense) + ' defense.')
        sleep(1)
        print('You have ' + str(self.xp) + ' XP.')
        sleep(1)
        print('You\'re level ' + str(self.level))

    def attack(self):

        sleep(1)

        print('Do you wish to attack (P)hysically or (M)agically?')

        sleep(1)

        print('Remaining mana: ' + str(self.mana))

        dmg_type = input('P/M: ')

        if dmg_type == 'P':
            foe.hp -= self.item.dmg - foe.defense
            print('You deal ' + str(self.item.dmg - foe.defense) + ' damage. The enemy has ' + str(foe.hp) + 'HP left.'
                  if foe.hp >= 1 else 'Your enemy has died. You have ' + str(self.hp) + 'HP left.')
            sleep(2)
            if foe.is_alive() and foe.mana >= 20:
                foe_magic_dmg = foe.item.dmg + 30 - protagonist.defense
                self.hp -= foe_magic_dmg
                print('Your enemy deals ' + str(foe_magic_dmg - self.defense) + ' magical damage. You have ' +
                      str(self.hp) + 'HP left.')
                sleep(2)
            elif foe.is_alive():
                self.hp -= foe.item.dmg - protagonist.defense
                print('Your enemy deals ' + str(foe.item.dmg - self.defense) + ' damage. You have ' + str(self.hp) +
                      'HP left.')
                sleep(2)

        elif dmg_type == 'M':
            magic_dmg = self.item.dmg + 50 - foe.defense
            if (self.mana - 25) >= 0:
                self.mana -= 25
                print('Remaining mana: ' + str(self.mana))
                foe.hp -= magic_dmg
                print('You deal ' + str(magic_dmg - foe.defense) + ' magical damage. Your enemy has ' + str(foe.hp) +
                      'HP left.' if foe.hp >= 1 else 'Your enemy has died. You have ' + str(self.hp) +
                      'HP left.')
                sleep(2)
                if foe.is_alive() and foe.mana >= 20:
                    foe_magic_dmg = foe.item.dmg + 30 - protagonist.defense
                    self.hp -= foe_magic_dmg
                    print('Your enemy deals ' + str(foe_magic_dmg - self.defense) + ' magical damage. You have ' +
                          str(self.hp) + 'HP left.')
                    sleep(2)
                elif foe.is_alive():
                    self.hp -= foe.item.dmg - protagonist.defense
                    print('Your enemy deals ' + str(foe.item.dmg - self.defense) + ' damage. You have ' + str(self.hp) +
                          'HP left.')
                    sleep(2)
            else:
                print('You don\'t have enough mana.')


def choose_class():
    player_class = None

    print('Which class will you be?: Paladin, Warlock, Assassin')

    while player_class is None:
        player_class = input()
        global protagonist
        if player_class == 'Paladin':
            protagonist = Player(500, 0, 250, 10, weapon, 'Paladin')
            break
        elif player_class == 'Warlock':
            protagonist = Player(250, 0, 350, 5, weapon, 'Warlock')
            break
        elif player_class == 'Assassin':
            protagonist = Player(300, 0, 200, 3, weapon, 'Assassin')
            break
        else:
            print('Try again.')


choose_class()
while protagonist.is_alive():
    random.shuffle(item_list)

    protagonist.status()

    while foe_list:
        protagonist.level_up()

        foe = foe_list.pop(0)

        sleep(2)

        print('A ' + foe.name + ' attacks you.')

        sleep(1)

        print('They have ' + str(foe.hp) + ' HP.')

        sleep(1)

        while foe.is_alive():
            if protagonist.is_alive():
                pass
            else:
                print('You\'ve died.')
                break
            protagonist.attack()

        sleep(1)

        protagonist.xp += foe.xp

        print('You gained ' + str(foe.xp) + ' XP. You need ' + str((100 + protagonist.level * 10) - protagonist.xp) +
              ' more to level up.' if ((100 + protagonist.level * 10) - protagonist.xp) >= 0 else 'You\'ve leveled up.')

        print(protagonist.level_up())

    break

if protagonist.is_alive():

    sleep(2)

    print("You\'ve won.")

else:

    sleep(2)

    print("You\'ve died.")
