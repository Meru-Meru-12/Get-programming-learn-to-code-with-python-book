# The problem
# You want to simulate playing the card game War. Each round, players will take a card from one deck and compare the cards. 
# The one with the higher card wins the round and gives their card to the other player. The winner is determined after numerous rounds, when the deck is empty.
# The winner is the person with fewer cards in their hand. You'll create two types of objects: a Player and a CardDeck. 
# After defining the classes, you'll write code that simulates a game between two players. You'll first ask users for their names then create two Player objects.
# Both players will use the same card deck. Then you'll use methods defined in the Player and CardDeck classes to automatically simulate the rounds and determine the winner.


class Player(object):
    """a player """
    def __init__(self,name):
        """sets the name and an empty hand """
        self.hand = []
        self.name = name
    def get_name(self):
        """Returns the name of the player """
        return self.name

class Player(object):
    """a player """
    def add_card_to_hand(self, card):
        """card, a string
        Adds valid card to the player's hand"""
        if card != None:
            self.hand.append(card)
    def remove_card_from_hand(self,card):
        """car, a string
            Remove card from the player's hand"""
        self.hand.remove(card)
    def hand_size(self):
        """Returns the number of cards in player's hand """
        return len(self.hand)

class CardDeck(object):
    """A deck of cards 2-9 of spades, hearts, diamonds, clubs"""
    def __init__(self):
        """a deck of cards (strings e.g. "2C" for the 2 of clubs)
        contains all cards possible """
        hearts = "2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H"
        diamonds = "2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D"
        spades =  "2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S"
        clubs  = "2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C"
    self.deck =  hearts.split (',')+diamonds.split(',')+spades.split(',')+clubs.split(',')