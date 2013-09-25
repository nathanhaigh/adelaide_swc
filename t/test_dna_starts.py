import dna_starts_with
#def dna_starts_with(in_seq, expected):
#  return in_seq[:(len(expected))] == expected

def test_dna_starts_with_self():
  dna = 'actgt'
  assert dna_starts_with(dna,dna)

def test_dna_starts_with_single_char():
  assert dna_starts_with('actgt','a')

def test_dna_not_starts_with_single_char():
  assert not dna_starts_with('actgt','t')

# you need to run the test functions
test_dna_starts_with_self()
test_dna_starts_with_single_char()
test_dna_not_starts_with_single_char()
