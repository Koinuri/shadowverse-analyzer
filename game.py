

class Game:
    def __init__(self, user):
        self.user = user

    def start(self, player1, player2):
        self.user.set_order()
        self.user.mulligan()
        while (not game_over()):
            self.play_turn()
            switch_player()

    def play_turn(self):
        start_turn()
        end_turn = False
        used = 0
        while (not end_turn):
            x = self.user.select_card()
            if (x.Cost + used <= GameState.Player.PlayPoint):
                used += x.Cost
                play_card(x)
        end_turn()

    def game_over():
        if GameState.Player <= 0:
            return True
        elif GameState.Opponent <= 0:
            return True
        else:
            return False

    def start_turn():
        draw_card()
        GameState.Player.TurnNumber += 1
        GameState.Player.PlayPoint += 1
        GameState.Player.Start = True

    def end_turn():
        GameState.Player.End = True

    def switch_player():
        GameState.Player, GameState.Opponent = GameState.Opponent, GameState.Player

    def play_card(card):
        if isinstance(card, (Follower, Amulet)):
            card.Fanfare()
            card.Play()
        if isinstance(card, Spell):
            card.Fanfare()
            card.Destroy()
