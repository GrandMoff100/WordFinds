class WordBank:
    abc = "qwertyuiopasdfghjklzxcvbnm"

    def __init__(self, words, english_only=True):
        for word in words:
            if not self.valid_word(word) and english_only:
                raise ValueError('The word "{}" contains characters not in the alphabet'.format(word))

        self.words = [x.upper() for x in words]

    def valid_word(self, word: str):
        return False not in [char in self.abc for char in word]
