__author__ = 'jens'

import util

# Read multi line input and copies all unique lines to the clipboard
# This will also trim all leading and trailing spaces

multiLineInput = util.raw_multi_line_input()
uniqueSorted = util.trim(sorted(util.create_set(multiLineInput, lambda s: s.lower()), key=str.lower))
util.copy_to_clipboard(uniqueSorted)
