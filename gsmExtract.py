__author__ = 'jens'

import util
import re

# Extracts belgian phone numbers from text

lines = util.raw_multi_line_input()
pattern = "(?:\+32|0032|0)(\d{8}\d?)"
phones = []
for line in lines:
    phones.extend(re.findall(pattern, line.translate(None, '/. ')))
phones = ["0032" + phone for phone in phones]
util.copy_to_clipboard(phones)
