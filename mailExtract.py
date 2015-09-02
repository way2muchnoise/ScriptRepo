__author__ = 'jens'

import util
import re

# Extract emails from text

text = util.raw_multi_line_input()
util.copy_to_clipboard(re.findall(r'[\w\.-]+@[\w\.-]+', ' '.join(text)))
