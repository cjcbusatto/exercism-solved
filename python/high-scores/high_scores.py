class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return sorted(self.scores, reverse=True)[0]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[0:3]

    def report(self):
        personal_best = self.personal_best()
        latest = self.latest()  # to avoid list sorting multiple times
        if personal_best == latest:
            return f"Your latest score was {latest}. That's your personal best!"

        return f"Your latest score was {latest}. That's {personal_best - latest} short of your personal best!"
