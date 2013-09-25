reader = open('pg76.txt', 'r')
character_count = 0
line_count = 0

for line in reader:
  if line.startswith('#'): continue
  line_count += 1
  character_count += len(line)
reader.close()

print "# of lines: %d\n# of chars: %d" % (line_count, character_count)
#print "# of lines: ", line_count
#print "# of chars: ", character_count


