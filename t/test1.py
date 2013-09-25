def dna_starts_with(in_seq, expected):
  return in_seq[:(len(expected))] == expected

assert dna_starts_with('actggt', 'act')
assert not dna_starts_with('actggt', 'agt')
