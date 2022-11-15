#!/usr/bin/python3
'''This module recieved logs from command line,
parse and print out some stats'''
import sys


def log_line(line):
    '''Take line and take necessary data for statistics'''
    try:
        line = line[:-1]
        words = line.split(" ")
        file_size[0] += int(words[-1])
        code = int(words[-2])
        if code in codes:
            codes[code] += 1
    except:
        pass


def print_stats():
    '''print statistics of current files'''
    print("File size: {}".format(file_size[0]))
    for code in sorted(codes.keys()):
        if codes[code]:
            print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
    file_size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 1

    try:
        for line in sys.stdin:
            # Skip, if the line format is not valid
            # if not match_format(line):
            #     continue
            # log data for statistics
            log_line(line)
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
