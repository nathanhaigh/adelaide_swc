import sys
cmd_args = sys.argv[1:]
cmd_args.sort()
cmd_args[0] = cmd_args[0].title()

string = ', '.join(cmd_args[0:-1])

print ', and '.join([string,cmd_args[-1]])
# or
print string + ', and ' + cmd_args[-1]

