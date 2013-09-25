#input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"
#create a dictionary in the following format:
#{'G': (# of occurences in the string),
#'A': ...
#}

input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"

print dict(zip(input_string, map(input_string.count,input_string)))
#print {key:input_string.count(key) for key in set(input_string)}

