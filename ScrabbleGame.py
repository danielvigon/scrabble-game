class Game:

  def __init__(self):
    self.scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4,
                   "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1,
                   "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                   "r": 1, "u": 1, "t": 1, "w": 4,
                   "v": 4, "y": 4, "x": 8, "z": 10}

  def get_score(self):
    self.word = input("Qual é a palavra a ser soletrada?\n• ").lower()
    score = 0
    for letter in self.word:
      if letter in self.scores:
        score += self.scores[letter]
    return score


scrabble = Game()
total_score = scrabble.get_score()
print(f'\n        Seu placar é {total_score}!')