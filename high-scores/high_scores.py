class HighScores(object):
    def __init__(self, scores):
        if type(scores) is list and self.are_all_elements_of_scores_attribute_numbers(scores):
            self.scores = scores
        else:
            raise ValueError('The scores attribute must be a list')

    def are_all_elements_of_scores_attribute_numbers(self, scores):
        result = True
        for score in scores:
            if type(score) is not int:
                result = False
        return result

    def latest(self):
        return self.scores[len(self.scores)-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        results = []
        try:
            for i in range(0, 3):
                results.append(sorted(self.scores, reverse=True)[i])
        except IndexError:
            pass
        return results

    def report(self):
        latest_score = self.scores[len(self.scores)-1]
        if self.scores.index(self.personal_best()) == len(self.scores)-1:
            return "Your latest score was %s. That's your personal best!" \
                    % self.personal_best()
        else:
            return "Your latest score was %s. That's %s short of your personal best!"\
                    % (latest_score, self.personal_best()-latest_score)
