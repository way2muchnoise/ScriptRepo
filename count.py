__author__ = 'jens'

import util

# Read multi line input and count times each line occers
# This will also trim all leading and trailing spaces

multiLineInput = util.raw_multi_line_input()
counter = dict()
for line in multiLineInput:
    if line in counter:
        counter[line] += 1
    else:
        counter[line] = 1
util.copy_to_clipboard(counter)
