#!/usr/bin/python3
"""
Task:
    Write a script that reads stdin line by line and computes metrics:
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
      print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer, don't print
  anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import re
import sys


def print_log(size, status_codes):
    """Prints the computed metric logs"""
    print(f'File size: {size}')
    for stat_code, count in status_codes.items():
        if count > 0:
            print(f'{stat_code}:  {count}')


def parse_log():
    """This function reads stdin line by line and computes metrics"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) -'\
        r' \[(.*?)\]'\
        r' "GET \/projects\/260 HTTP\/1\.1"'\
        r' (\d{3})'\
        r' (\d+)'

    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    size = 0
    i = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                ip_address = match.group(1)
                date = match.group(2)
                status_code = match.group(3)
                file_size = match.group(4)

                if type(status_code) is str \
                    and status_code.isdigit() \
                        and (str(status_code) in status_codes):
                    status_codes[str(status_code)] += 1

                if type(file_size) is str and file_size.isdigit():
                    size += int(file_size)

                i += 1
                if i % 10 == 0:
                    print_log(size, status_codes)
    except KeyboardInterrupt:
        print_log(size, status_codes)


if __name__ == '__main__':
    parse_log()
