class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"BasicWord({self.word}, {self.subwords})"

    def word_verification(self):
        for subword in self.subwords:
            if subword in self.subwords:
                return True
            return False

    def number_of_subwords(self):
        return int(len(self.subwords))

