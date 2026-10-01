import sys


if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is", arg)