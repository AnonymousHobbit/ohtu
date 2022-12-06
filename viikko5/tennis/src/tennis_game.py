class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_tie_score(self, scores):
        if self.player1_score not in scores:
            return "Deuce"
        return scores[self.player1_score]+"-All"
        
    def format_score(self, scores):
        return scores[self.player1_score] + "-" + scores[self.player2_score]

    def get_lead_score(self):
        difference = self.player1_score - self.player2_score

        if difference == 1:
            return "Advantage player1"

        if difference == -1:
            return "Advantage player2"

        if difference >= 2:
            return "Win for player1"

        return "Win for player2"


    def get_score(self):
        score = ""

        scores = {0: "Love", 1: "Fifteen",
                  2: "Thirty", 3: "Forty"}

        if self.player1_score == self.player2_score:
            score = self.get_tie_score(scores)
            
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_lead_score()
        
        else:
            score = self.format_score(scores)

        return score
