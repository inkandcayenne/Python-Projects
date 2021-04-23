#  BlackJack Card Game

# Создать игру Блэк Джек
# В игре может участвовать один игрок, который играет против дилера
# Игрок может просить еще одну карту или остановиться
# Игрока необходимо оповещать о количестве карт на руках, очках, выигрыше, проигрыше и т.д.
# Для игры используются следующие правила: используется одна колода. Туз - это 11 очков, если количество очков меньше 21,
# Если больше - то считается как 1 очко. Задача игрока - выиграть у дилера, дилер деоржит одну карту закрытой, остальные берет в открытую.
# Дилер обязан остановиться, как только наберёт 17 очков или выше, и обязан брать, пока не достигнет.
# Если сумма очков игрока 21, то количество очков дилера не имеет значения

import random

# словарь с мастями и значениями
suits = ('Черви', 'Буби', 'Пики', 'Треф')
ranks = ('Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз')
values = {'Двойка':2, 'Тройка':3, 'Четверка':4, 'Пятерка':5, 'Шестерка':6, 'Семерка':7, 'Восьмерка':8,
            'Девятка':9, 'Десятка':10, 'Валет':10, 'Дама':10, 'Король':10, 'Туз':0}

#класс для карты с атрибутами и гет методами для самой игры
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + ' ' + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

#класс колоды, методы перемешивания, выдачи карты из колоды

class Deck:
    def __init__(self):
        self.main_deck = []
        for suit in suits:
            for rank in ranks:
                self.main_deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.main_deck)

    def deal_one(self):
        return self.main_deck.pop(0)

#класс для игрока. Дилер тоже игрок, определяется атрибутом
class Player:
    def __init__(self, dealer='N'):
        self.player_hand = []
        self.sum = 0
        self.dealer = dealer

    #метод выдачи карты, расчет количества очков и отдельное поведение для туза
    def give_card(self, new_card):
        self.new_card = new_card
        self.player_hand.append(self.new_card)
        self.sum += self.new_card.get_value()
        if self.new_card.get_rank() == 'Туз':
            self.sum += 11
            if self.sum > 21:
                self.sum = self.sum - 10

    # показываем карты дилера и игрока игроку
    def get_cards(self, final='N'):
        self.final = final
        if self.dealer == 'Y' and self.final == 'N':
            print('карты дилера: Неизвестная карта и', list(map(str, self.player_hand[1::])))
        elif self.dealer == 'Y' and self.final == 'Y':
            print('дилер вскрывается', list(map(str, self.player_hand)))
            print('сумма очков дилера', self.sum)
        else:
            print('ваши карты', list(map(str, self.player_hand)))
            print('ваша сумма очков', self.sum)

    def get_sum(self):
        return self.sum

#Начало игры, перемешиваем колоду, инициализируем мгроков, сдаем по 2 карты
dealer = Player(dealer = 'Y')
player = Player()
our_deck = Deck()
our_deck.shuffle()
game_on = True
turn = 0
print('\n сдаем вам карты:')
player.give_card(our_deck.deal_one())
player.give_card(our_deck.deal_one())
player.get_cards()
print('\n сдаем карты дилера:')
dealer.give_card(our_deck.deal_one())
dealer.give_card(our_deck.deal_one())
dealer.get_cards()

#Сама игра
while game_on == True:
    # Проверяем выигрыш игрока

    if player.get_sum() == 21:
        game_on = False
        player.get_cards()
        print('Вы выиграли')
    elif player.get_sum() > 21:
        game_on = False
        print('Вы проиграли')
    # Если игра не завершилась, спрашиваем нужна ли карта
    else:
        answer_check = False
        while answer_check == False:
            answer = input('Сдать еще карту(да, нет)? ')
            if answer in ['да', 'нет']:
                answer_check = True
            else:
                print('введите ответ из списка')
        # Если не нужна карта, то очередь переходит к дилеру
        if answer == 'нет':
            turn = 1
        # Если карта нужна, сдаем еще одну
        else:
            player.give_card(our_deck.deal_one())
            player.get_cards()
    # Если очередь перешла к дилеру
    if turn == 1:
        while dealer.get_sum() < 17:
            print('сдаем карту дилеру')
            dealer.give_card(our_deck.deal_one())
            dealer.get_cards()
        else:
            game_on = False
            if dealer.get_sum() > player.get_sum() and dealer.get_sum() <= 21:
                dealer.get_cards(final='Y')
                print(f'дилер выиграл, сумма очков {dealer.get_sum()}, ваша - {player.get_sum()}')
            else:
                dealer.get_cards(final='Y')
                print(f'вы выиграли {player.get_sum()}, у дилера - {dealer.get_sum()}')


