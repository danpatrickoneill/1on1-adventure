class Match:
"""
Two players enter; both leave, but one leaves as the winner
"""
    def __init__(self, user_player, opposing_player, score=11):
        self.user_player = user_player
        self.opposing_player = opposing_player

    def get_players(self):
        """
        Returns players involved in match instance
        """
        return [self.user_player, self.opposing_player]