# Will be factors pushing player toward outside vs. inside shots; not sure about implementation just yet
STRATEGIES = {
    'marksman': .8,
    'bruiser': .2,
    'balanced': .5
}

class Match:
    """
    Two players enter; both leave, but one leaves as the winner
    """
    def __init__(self, user_player, opposing_player, target_score=11, take_it=False):
        self.user_player = user_player
        self.opposing_player = opposing_player
        self.take_it = take_it

    def get_players(self):
        """
        Returns players involved in match instance
        """
        return [self.user_player, self.opposing_player]

    def play_point(self):
        user_strategy = STRATEGIES[self.user_player.style]
        opp_strategy = STRATEGIES[self.opposing_player.style]
