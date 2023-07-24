0x03. Log Parsing
- Algorithm - Python

This script reads stdin line by line and computes metrics:
Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    (if the format is not this one, the line will be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C),
      it prints these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>
    (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer, it wouldn't print
  anything for this status code
format: <status code>: <number>
status code will be printed in ascending order

## How to run code:
...$ ./0-generator.py | ./0-stats.py