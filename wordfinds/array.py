import english_words as ew
from .wordbank import WordBank
from .utils import rrange


class RawWordFindArray:  
    def __init__(self, size: tuple, wordbank: WordBank = WordBank([])):
        if min(size) < 1:
            raise ValueError('Dimensions have to be greater than 1')
        self.size = size

        if type(wordbank) != WordBank:
            raise ValueError("'{}' object is not a WordBank object".format(type(wordbank)))
        
        self.wordbank = wordbank

        self._all = set(
            [x.lower() for x in self.wordbank.words] + 
            list(ew.english_words_lower_set)
        )
        
        self.letter_array = [[]]

    def __str__(self):
        return self.view()

    def valid_word_length(self, word: str):
        return len(word) <= max(self.size)
    
    def view(self, hsep=' ', vsep='\n'):
        return vsep.join([hsep.join(row) for row in self.letter_array])
    
    def letter_combos(self, min_len=2):
        for wordlen in range(min_len, max(self.size) + 1):
            # Rows
            for row in self.letter_array:
                for i in range(len(row) - wordlen + 1):
                    yield ''.join(row[i:i + wordlen])
            # Columns
            for column in zip(*self.letter_array):
                for i in range(len(column) - wordlen + 1):
                    yield ''.join(column[i:i + wordlen])
            # Diagonals
            for _ in range(2):
                for diagonal in self.diagonals():
                    for i in range(len(diagonal) - wordlen + 1):
                        yield ''.join(diagonal[i:i + wordlen])
                self.letter_array.reverse()

    def find_words(self, min_len=2):
        return set(filter(
            lambda x: x.lower() in self._all or x.lower()[::-1] in self._all,
            self.letter_combos(min_len),
        ))

    def diagonals(self):
        w,h = self.size
        for p in range(-w,w+2):
            for d in [-1, 1]:
                vec = []
                indices = [
                    (p+x*d, x) for x in range(w)
                    if 0 <= p+x*d < h and 0 <= x < w
                ]
                for x, y in indices:
                    try:
                        vec.append(self.letter_array[x][y])
                    except IndexError:
                        continue
                if vec:
                    yield vec


class WordArray(list):
    @property
    def width(self):
        return len(self[0])
    
    @property
    def height(self):
        return len(self)
    
    def place_word(self, word, start, end, test=False):
        (x1, y1), (x2, y2) = start, end
        if not self.check_coords(x1,y1):
            raise ValueError('Start coordinate is out of bounds.')
        if not self.check_coords(x2,y2):
            raise ValueError('End coordinate is out of bounds.')
        if x1 - x2 != y1 - y2 and min([abs(x1 - x2), abs(y1 - y2)]) > 0:
            raise ValueError('Coords in non-valid direction')
        if len(word) - 1 > max([abs(x1-x2), abs(y1-y2)]):
            raise ValueError(f'Cannot fit the word "{word}" between {start} and {end}')
        
        xcoords = rrange(x1,x2) if abs(x1 - x2) > 0 else [x1] * (abs(y1-y2) + 1)
        ycoords = rrange(y1,y2) if abs(y1 - y2) > 0 else [y1] * (abs(x1-x2) + 1)
        for char,x,y in zip(word.upper(), xcoords, ycoords):
            if self[y][x] in [char, '.']:
                if not test:
                    self[y][x] = char
            else:
                raise IndexError(f'The word "{word}" will overlap {self[y][x]} at {(x,y)}')

    def check_coords(self, x,y):
        return 0 <= x < self.width and 0 <= y < self.height


