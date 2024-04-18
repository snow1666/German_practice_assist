class Quiz():
    def __init__(self, vocab, n=10, attribute=None):
        self.vocab = vocab
        self.attribute = attribute
        self.questions = self.vocab.get_quiz(n, attribute)
        self.question_index = 0
        self.answers = [None]*len(self.questions)
        self.if_correct = [None]*len(self.questions)
        self.score = 0
