__author__ = 'jens'

import util

multiLineInput = util.raw_multi_line_input()
uniqueSorted = sorted(set(multiLineInput), key=str.lower)
util.copy_to_clipboard(uniqueSorted)
