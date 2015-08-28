__author__ = 'jens'

import util
import re

text = util.raw_multi_line_input()
util.copy_to_clipboard(re.findall(r'[\w\.-]+@[\w\.-]+', ''.join(text)))
