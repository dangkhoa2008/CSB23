import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):

        self.suits = ['heart', 'diamond', 'club', 'spade']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
    
    def shuffle(self):

        random.shuffle(self.cards)

    def deal_a_card(self):

        if not self.cards:
            return None

        return self.cards.pop(0)

    def sort(self):

        suit_order = {'heart': 4, 'diamond': 3, 'club': 2, 'spade': 1}
        value_order = {value: i for i, value in enumerate(self.values)}


        self.cards.sort(key=lambda card: (suit_order[card.suit], value_order[card.value]), reverse=True)

    def __str__(self):

        return '\n'.join(str(card) for card in self.cards)

#test
if __name__ == "__main__":

    deck = Deck()
    print("Bộ bài ban đầu (đã sắp xếp theo thứ tự mặc định):")
    print(deck)
    print("-" * 20)


    deck.shuffle()
    print("Bộ bài sau khi xáo trộn:")
    print(deck)
    print("-" * 20)


    dealt_card = deck.deal_a_card()
    print(f"Rút một lá bài: {dealt_card}")
    print(f"Số lá bài còn lại: {len(deck.cards)}")
    print("-" * 20)


    deck.sort()
    print("Bộ bài sau khi sắp xếp lại theo yêu cầu:")
    print(deck)