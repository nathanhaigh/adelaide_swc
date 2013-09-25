import sys
cmd_args = sys.argv[1:]
cmd_args.sort()
cmd_args[0] = cmd_args[0].title()

string = ', '.join(cmd_args[0:-1])

print string + ', and ' + cmd_args[-1] + '.'

