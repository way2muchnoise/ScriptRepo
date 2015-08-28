__author__ = 'jens'

import util

print 'Base set'
base = set(util.raw_multi_line_input())
print 'To remove from base'
to_del = set(util.raw_multi_line_input())
util.copy_to_clipboard(sorted(base.difference(to_del), key=str.lower))
