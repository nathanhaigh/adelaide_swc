reader = open('Pitching.csv', 'r')
header = reader.readline()
IPouts_idx = header.split(',').index('IPouts')
total=0
n_lines=0
for line in reader:
  n_lines += 1
  total += float(line.split(',')[IPouts_idx])
reader.close()

print "IPouts in column idx: %d\nTotal lines: %d\nSum: %d\nAverage: %d" % (IPouts_idx, n_lines, total, total/n_lines)
