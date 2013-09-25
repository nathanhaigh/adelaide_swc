def dna_starts_with(sequence, prefix):
  '''Returns a boolean if prefix is a prefix of sequence. What follows is a "doc test", that is a test embeded within the help documentation.
  >>> dna_starts_with('actgt','actgt')
  True
  >>> dna_starts_with('actgt','a')
  True
  >>> dna_starts_with('actgt','t')
  False
  '''
  return sequence[:(len(prefix))] == prefix

if __name__ == '__main__':
  # this runs the doctests when the file is executed by python
  # but doesn't run them when the file is included
  import doctest
  doctest.testmod()
