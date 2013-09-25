def remove_N(dna):
  return dna.replace('N', '').replace('n','')

def calc_gc(dna):
  char_counts = dict(zip(dna, map(dna.count,dna)))
  if 'G' not in char_counts.keys():
    char_counts['G'] = 0
  if 'C' not in char_counts.keys():
    char_counts['C'] = 0
  return (char_counts['G'] + char_counts['C'])/float(len(dna))*100


dna1 = 'ATGCNNNNNN'
dna2 = 'NGGGGGGGGGC'
dna3 = 'GTGTGTGTGTTTT'

print calc_gc(remove_N(dna1))
print calc_gc(remove_N(dna2))
print calc_gc(remove_N(dna3))
