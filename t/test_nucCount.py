import nucCount

Tests = [
  ['ACGTGT', {'A': 1, 'C': 1, 'T': 2, 'G': 2}],
  ['CAGGTT', {'C': 1, 'A': 1, 'G': 2, 'T': 2}],
]

passes = 0
for (i, (seq, expected)) in enumerate(Tests):
  if nucCount.nucCount(seq) == expected:
    passes += 1
else:
  print('test %d failed' % i)

print('%d/%d tests passed' % (passes, len(Tests)))
