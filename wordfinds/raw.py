import random
from .utils import filler
from .array import RawWordFindArray, WordArray


class RawWordFind(RawWordFindArray):
    def __init__(self, size, wordbank):
        super().__init__(size, wordbank)
        for word in wordbank.words:
            if not self.valid_word_length(word):
                raise ValueError(
                    'The word "{}" cannot fit into a {}x{} array.' .format(word, *self.size) +
                'Try using less words or shorter ones.')
        
        total = sum([len(word) for word in wordbank.words])
        w,h = size

        if total > w * h:
            raise ValueError(f'Cannot fit {total} characters in a {w}x{h} array. Try using less words or shorter ones.')

        self.letter_array = self.generate()

    def directions(self, x, y, word):
        return [
            (x-len(word), y-len(word)), 
            (x-len(word), y),
            (x-len(word),y+len(word)),
            (x, y-len(word)), 
            (x, y),
            (x,y+len(word)),
            (x+len(word), y-len(word)), 
            (x+len(word), y),
            (x+len(word),y+len(word)),
        ]

    def find_spots(self, grid, word):
        w, h = self.size
        for x in range(w):
            for y in range(h):
                for end in self.directions(x,y,word):
                    try:
                        grid.place_word(word,(x,y),end,True)
                        yield (x,y), end
                    except (ValueError, IndexError):
                        pass
        
    def generate(self):
        w, h = self.size
        grid = WordArray([['.' for _ in range(w)] for _ in range(h)])
        for word in self.wordbank.words:
            start, end = random.choice(list(self.find_spots(grid, word)))
            grid.place_word(word, start, end)
        return WordArray([[x if x != '.' else filler() for x in row] for row in grid])


class WordFind(RawWordFind):
    pass

