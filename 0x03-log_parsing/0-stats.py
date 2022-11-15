#!/usr/bin/python3
import sys
"""
a python script that reads stdin line by line & computes metrics
the format must be
File size: <total size>
<status code>: <number>
"""


def get_size(line):
    """
    get_size: functin to read a line and find the total size
    Arguments:
        line: the given line
    Returns:
        the total size
    """
    line_spt = line.split()
    first_ocatet = line_spt[0].split('.')[0]
    first_ocatet = int(first_ocatet)
    if len(line_spt) != 9 or first_ocatet > 255 or first_ocatet < 0:
        return 0
    s_code = line_spt[-2]
    if s_code in status_code:
        status_code[s_code] += 1
    size = int(line_spt[-1])
    return size


def display():
    """
    display - function to display the status in the mentioned format
    Argumetns:
        nothing
    Returns:
        nothing
    """
    print("File size: {}".format(f_size))
    for key, value in status_code.items():
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == '__main__':
    """
    entry point of the program
    """
    f_size = 0
    nbr_line = 0
    status_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    try:
        for line in sys.stdin:
            f_size += get_size(line)
            if nbr_line % 10 == 0:
                display()
            nbr_line += 1
    except KeyboardInterrupt:
        display()
