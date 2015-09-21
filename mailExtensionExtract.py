__author__ = 'jens'

import util
import re

# Extract email extensions from a list of mails use mailExtract.py first to get mails from text

text = util.raw_multi_line_input()
util.copy_to_clipboard(re.findall(r'@[\w\.-]+', ' '.join(text)))
