import sys

sys.argv

string1 = 'acafshsdshAGHSGDJDFXDOSPYHWE52H436382vbdjx'
string2 = 'HDHD923,.D;D[]WLDHDHgsjdgwu2720hc.'

# number of characters in common
print 'Number of characters in the union: ' + len(set(string1.upper()).union(set(string2.upper())))

# number of characters in string1 but not string2
print len(set(string1.upper()).difference(set(string2.upper())))

# number of characters in string2 but not string1
print len(set(string2.upper()).difference(set(string1.upper())))



