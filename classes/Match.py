STRATEGIES = {
    'marksman': .8,
    'bruiser': .2,
    'balanced': .5
}

class Match:
"""
Two players enter; both leave, but one leaves as the winner
"""
    def __init__(self, user_player, opposing_player, score=11):
        self.user_player = user_player
        self.opposing_player = opposing_player
        self.st

    def get_players(self):
        """
        Returns players involved in match instance
        """
        return [self.user_player, self.opposing_player]

    def play_point(self):
        user_strategy = STRATEGIES[self.user_player.style]
        opp_strategy = STRATEGIES[self.opposing_player.style]

        