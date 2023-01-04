'''Black Jack'''
import random
import time


class Card:
    card_list = {
                '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                '6' : 6, '7' : 7, '8' : 8, '9' : 9,          #   Card list
                '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10,     #   and count
                'A' : 11
                }
    card_list_suit = ['♠','♥', '♣', '♦']

class Deck(Card):
    deck_cards = []
    def deck_generator(self):
        for i in self.card_list:
            for j in self.card_list_suit:
                self.deck_cards.append([i, j])
        random.shuffle(self.deck_cards)
        # return self.deck_cards
    
class Player(Deck):
    card_point_counter = []
    user_card_list = []
    pc_card_list = []
    
    pc_card_point_counter = []
    user_ = 0
    def user_cards(self):
        self.user_card_number_1 = random.randint(0, len(self.deck_cards) - 1)
        self.user_card_1 = self.deck_cards[self.user_card_number_1][0] + self.deck_cards[self.user_card_number_1][1]
        self.user_card_list.append(self.user_card_1)
        self.card_point_counter.append(self.card_list[self.deck_cards[self.user_card_number_1][0]])
        self.deck_cards.remove([self.deck_cards[self.user_card_number_1][0], self.deck_cards[self.user_card_number_1][1]])
        
        self.user_card_number_2 = random.randint(0, len(self.deck_cards) - 1)
        self.user_card_2 = self.deck_cards[self.user_card_number_2][0] + self.deck_cards[self.user_card_number_2][1]
        self.user_card_list.append(self.user_card_2)
        self.card_point_counter.append(self.card_list[self.deck_cards[self.user_card_number_2][0]])
        self.deck_cards.remove([self.deck_cards[self.user_card_number_2][0], self.deck_cards[self.user_card_number_2][1]])
        for i in self.user_card_list:
            print(i, end = " ")
        print()
    def user_cards_count_number(self):
        return sum(self.card_point_counter)
        
    def computer_cards(self):
        self.pc_card_number_1 = random.randint(0, len(self.deck_cards) - 1)
        self.pc_card_1 = self.deck_cards[self.pc_card_number_1][0] + self.deck_cards[self.pc_card_number_1][1]
        self.pc_card_list.append(self.pc_card_1)
        self.pc_card_point_counter.append(self.card_list[self.deck_cards[self.pc_card_number_1][0]])
        self.deck_cards.remove([self.deck_cards[self.pc_card_number_1][0], self.deck_cards[self.pc_card_number_1][1]])
        
        self.pc_card_number_2 = random.randint(0, len(self.deck_cards) - 1)
        self.pc_card_2 = self.deck_cards[self.pc_card_number_2][0] + self.deck_cards[self.pc_card_number_2][1]
        self.pc_card_list.append(self.pc_card_2)
        self.pc_card_point_counter.append(self.card_list[self.deck_cards[self.pc_card_number_2][0]])
        self.deck_cards.remove([self.deck_cards[self.pc_card_number_2][0], self.deck_cards[self.pc_card_number_2][1]])
        for i in self.pc_card_list:
            print(i, end = " ")
        print()
    def pc_cards_count_number(self):
        return sum(self.pc_card_point_counter)

    def new_card(self):
        self.user_new_card_number = random.randint(0, len(self.deck_cards) - 1)
        self.user_new_card = self.deck_cards[self.user_new_card_number][0] + self.deck_cards[self.user_new_card_number][1]
        self.user_card_list.append(self.user_new_card)
        print('Your new card:    ', self.user_new_card)
        self.card_point_counter.append(self.card_list[self.deck_cards[self.user_new_card_number][0]])
        self.deck_cards.remove([self.deck_cards[self.user_new_card_number][0],self.deck_cards[self.user_new_card_number][1]])
        



player = Player()

player.deck_generator()
print('Loading...')
time.sleep(random.uniform(0,2.5))
print('Starting game of Black Jack')
name_of_the_player = input('Please enter your name:    ')
print(f'Nice to meet you {name_of_the_player.title()}, my name is Diana and I will be playing tonight with you...')
time.sleep(random.uniform(0,1.5))

print("Let's start")
print()
print('shuffling...\n')
time.sleep(random.uniform(0, 1.9))
print('Your cards:    ', end = '')
player.user_cards()
print('Your points:    ', player.user_cards_count_number())
print()
print('Diana cards:    ', end = '')
player.computer_cards()
print('Diana points:    ', player.pc_cards_count_number())
print()

while True:
    
    if player.user_cards_count_number() == 21:
        print('Black Jack!!! You win!')
        break
    
    elif player.user_cards_count_number() > 21:
        print('You lose!You are over 21')
        break
    elif player.pc_cards_count_number() == 21:
        print('You lose!Diana has Black Jack')
        break
    elif player.pc_cards_count_number() > 21:
        print('You win! Diana is over 21')
        break
    new_card_answer = input('Do you want another card? y/n    ').lower()
    print()
    if new_card_answer == 'y':
        player.new_card()
        print('Your count:    ', player.user_cards_count_number())
        print()
    else:
        break