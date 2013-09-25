import sys
number = int(sys.argv[1])

if 0 < number < 10:
  print "small posivitive"
elif number >= 0:
  print "large posivive"
else:
  print "negative"

