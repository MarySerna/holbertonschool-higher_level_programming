#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print("{} arguments.".format(l - 1))
    elif l == 2:
        print("{} argument: ".format(l - 1))
    elif l > 2:
        print("{} arguments: ".format(l - 1))
    for count in range(1, len(argv)):
        print("{} : {}".format(count, argv[count]))
        count = count + 1
