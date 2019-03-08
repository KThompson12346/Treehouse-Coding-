class YatzyScoresheet:
    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = []
        for worth, count in hand._sets.items():
            scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_chance(self, hand):
        total = 0
        for die in hand:
            total += die
        return total

    def score_yatzy(self, hand):
        compare = int(hand[0])
        for die in hand:
            if int(die) == compare:
                continue
            else:
                return 0
        return 50
