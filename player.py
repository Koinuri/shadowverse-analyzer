

class Player:
    def __init__(self, deck):
        self.Hand = []
        self.Board = []
        self.Deck = deck
        self.Graveyard = []
        self.PlayPoint = 0
        self.Life = 20
        self.Evo = 0
        self.LeaderEffect = []
        self.Shadow = 0
        self.Played = 0
        self.TurnNumber = 0
        self.Start = False
        self.End = False

