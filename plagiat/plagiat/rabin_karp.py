""" 
  Rabin-Karp Module
  Ref: https://gist.githubusercontent.com/TheDhejavu/39d6cfec2b3f75a1ac111042cb8aebdb/raw/e653f12b095e7b7e2bb99a14fdb3b60fa86df642/rabin_karp.py
"""
class rabin_karp:
  def __init__(self, text, patternSize):
    self.text = text
    self.patternSize = patternSize
    self.base = 26
    self.window_start = 0
    self.window_end = 0
    self.mod = 5807
    self.hash = self.get_hash(text, patternSize)

  def get_hash(self, text, patternSize):
    hash_value = 0
    for i in range(0, patternSize):
      hash_value += (ord(self.text[i]) - 96)*(self.base**(patternSize - i -1)) % self.mod

    self.window_start = 0
    self.window_end =  patternSize

    return hash_value

  def next_window(self):
    if self.window_end <= len(self.text) - 1:
      self.hash -= (ord(self.text[self.window_start]) - 96)*self.base**(self.patternSize-1)
      self.hash *= self.base
      self.hash += ord(self.text[self.window_end])- 96
      self.hash %= self.mod
      self.window_start += 1
      self.window_end += 1
      return True
    return False

  def current_window_text(self):
    return self.text[self.window_start:self.window_end]