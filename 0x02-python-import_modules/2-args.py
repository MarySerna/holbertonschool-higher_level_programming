#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = len(argv)
    if numarg == 1:
        print('{} arguments.'.format(numarg - 1))
    elif numarg == 2:
        print('{} argument:'.format(numarg - 1))
    elif numarg > 2:
        print("{} arguments:".format(numarg - 1))
    for c in range(1, len(argv)):
        print('{}: {}'.format(c, argv[c]))
        c = c + 1
