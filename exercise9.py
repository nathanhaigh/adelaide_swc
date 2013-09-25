import sys
in_filename = sys.argv[1]
reader = open(in_filename, 'r')
stats = {}
seq_name = ''
for line in reader:
  line = line.rstrip('\r\n')
  if line.startswith('>'):
    if seq_name != '':
      print "%s N: %d" % (seq_name, stats[seq_name]['N'])
      print "A: %d" % (stats[seq_name]['A'])
      print "C: %d" % (stats[seq_name]['C'])
      print "G: %d" % (stats[seq_name]['G'])
      print "T: %d" % (stats[seq_name]['T'])
    seq_name = line[1:]
    stats[seq_name] = {'N':0, 'A':0, 'C':0, 'G':0, 'T':0}
  else:
    # on a sequence line for seq_name
    stats[seq_name]['N'] += line.count('N')
    stats[seq_name]['A'] += line.count('A')
    stats[seq_name]['C'] += line.count('C')
    stats[seq_name]['G'] += line.count('G')
    stats[seq_name]['T'] += line.count('T')

print "%s N: %d" % (seq_name, stats[seq_name]['N'])
print "A: %d" % (stats[seq_name]['A'])
print "C: %d" % (stats[seq_name]['C'])
print "G: %d" % (stats[seq_name]['G'])
print "T: %d" % (stats[seq_name]['T'])
reader.close()

