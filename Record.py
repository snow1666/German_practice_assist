

class Score:
    def __init__(self):
        self.score = [None]*5


class MistakeBook:
    def __init__(self):
        self.mistakes = {}

    def add(self, word):
        self.mistakes[word] = 2

    def remove(self, word):
        if word in self.mistakes:
            del self.mistakes[word]

    def gain_points(self, word):
        self.mistakes[word] = min(0, self.mistakes[word] - 1)
        if self.mistakes[word] == 0:
            del self.mistakes[word]

    def lose_points(self, word):
        self.mistakes[word] = max(2, self.mistakes[word] + 1)



