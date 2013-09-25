from string import maketrans   # Required to call maketrans function.

class NucleotideString:
  transtable = maketrans("actgACTG", "tgacTGAC")

  def __init__(self, sequence):
    self.sequence = sequence
    self._bases = {}

  def base_count(self, base):
    '''This is help text that appears if a user calls help() on the
    method'''
    if base in self._bases:
      return self._bases[base]
    return self.sequence.count(base)
  
  def gc_content(self):
    n_gc = self.base_count('G') + self.base_count('C') + self.base_count('g') + self.base_count('c')
    #pass
    return n_gc/float(len(self.sequence))
    
  def reverse_comp(self):
    #pass
    return self.sequence[::-1].translate(self.transtable)
    
class DNAString(NucleotideString):
  pass

class RNAString(NucleotideString):
  transtable = maketrans("acugACUG", "ugacUGAC")
