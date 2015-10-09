__author__ = 'jens'

import util

# Find all entries in that are in both sets

print 'Set one'
base = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
print 'Set two'
to_match = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
util.copy_to_clipboard(sorted(base.intersection(to_match), key=str.lower))
