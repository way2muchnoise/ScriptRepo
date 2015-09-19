__author__ = 'jens'

import util

# Remove all double entries and entries that have an extension out of the second list

print 'Base set'
base = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
print 'Extensions to remove from base'
to_del = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
for to_del_entry in to_del:
    base_set = set(base)
    for entry in base_set:
        if entry.endswith(to_del_entry):
            base.remove(entry)
util.copy_to_clipboard(sorted(base.difference(to_del), key=str.lower))
