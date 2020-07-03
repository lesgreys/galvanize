import random

HIT = True
STAY = False

class Card(object):
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        if rank > 10:
            self.points = 10
        elif rank == 1:
            self.points = 11
        else:
            self.points = rank

    def __repr__(self):
        face = {11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace'}
        others = {num: str(num) for num in range(2, 11)}
        others.update(face)
        return f'{others[self.rank]} of {self.suit}'


class Deck(object):
    
    def __init__(self, shuffled=True):
        self.stack = []
        
        # Two nested for loops for each rank in each suit
        for rank in range(1, 14):
            for suit in ("Spades", "Clubs", "Hearts", "Diamonds"):
                self.stack.append(Card(rank, suit))

        if shuffled:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.stack)

    # def __str__(self):
    #     string = ""
    #     for card in self.stack:
    #         string += str(card) + "\n"
    #     return string.strip("\n")

    def hit(self):
        if not self.stack:
            self.__init__()

        return self.stack.pop()

        

    # def deal(self, num=1):
    #     if self.stack:
    #         return [self.stack.pop() for _ in range(num)]
        
    #     user_input = input("The deck is empty! New deck?(y/n): ").lower()
    #     if user_input == 'y':
    #         self.__init__()
    #         return [self.stack.pop() for _ in range(num)]
    #     elif user_input == 'n':
    #         print("Game over!")



class Player(object):
    
    def __init__(self, name, wins=0, losses=0):
        self.name = name
        self.hand = []
        self.wins = wins
        self.losses = losses
        self.winrate = None
        self.action = HIT

    def update_winrate(self):
        if self.losses + self.wins:
            self.winrate = self.wins/(self.losses + self.wins)

    def __str__(self):
        return f"{self.name} winrate: {self.winrate} ({self.wins}/{self.losses})"


class Game(object):
    def __init__(self):
        num_players = int(input("Number of players: "))
        self.players = [Player(input(f"Player {i} name: ").capitalize()) for i in range(1, num_players+1)]
        self.point_dict = {player.name:0 for player in self.players}
        
        self.play_round()

        # Play rounds until the user declines
        while True:
            user_input = input("Play Again?(y/n) ")
            if user_input == 'n':
                break
            self.play_round()

        print("Game Over!")
        for player in self.players:
            print(player)


    def play_round(self):
        print("New Round, Dealing...")
        deck = Deck()
        for player in self.players:
            player.hand = []
            player.action = HIT
            player.hand.extend(self.deal(deck))
            print(f"{player.name}: {str(player.hand).strip('[]')}")

        while self.check_playing():
            for player in self.players:
                player.current_points = 0
                while player.action == HIT:
                    points = 0
                    aces = 0
                    for card in player.hand:
                        points += card.points
                        if card.rank == 1:
                            aces += 1

                    while points > 21 and aces:
                        points -= 10
                        aces -= 1
         
                    if points > 21:
                        print(f"{player.name}, yah busted with {points} points")
                        player.action = STAY
                        self.point_dict[player.name] = points
                        break

                    hitting = input(f"{player.name} ({points} points): Hit or Stay?(h/s) ").lower()
                    if hitting == 'h':
                        player.hand.append(deck.hit())
                        print(str(player.hand).strip('[]'))
                    else:
                        player.action = STAY
                        self.point_dict[player.name] = points
            self.update_wins()

            
                

    def update_wins(self):
        max_points = 0
        max_name = ""
        for name, points in self.point_dict.items():
            if points > max_points and points <= 21:
                max_points = points
                max_name = name
        for player in self.players:
            if player.name == max_name:
                player.wins += 1
            else:
                player.losses += 1
            player.update_winrate()

    
    def check_playing(self):
        for player in self.players:
            if player.action:
                return True
        return False

    # Deal two cards from the given deck
    def deal(self, deck):
        return [deck.hit(), deck.hit()]


if __name__=='__main__':
    game = Game()