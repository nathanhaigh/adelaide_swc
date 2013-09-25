a = 4
def sum_two_numbers (first_number, second_number):
  result = first_number + second_number
  a = 'something else'
  print "inside a: ", a
  return result

print sum_two_numbers(12, 30)
print "outside a: ", a
