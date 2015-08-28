__author__ = 'jens'

import util

print 'Base set'
base = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
print 'To remove from base'
to_del = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
util.copy_to_clipboard(sorted(base.difference(to_del), key=str.lower))
