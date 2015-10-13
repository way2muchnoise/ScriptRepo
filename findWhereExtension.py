__author__ = 'jens'

import util

# Remove all double entries and entries that don't have a given extension out of the second list

print 'Base set'
base = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
print 'Extensions to remove from base'
to_find = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
for to_find_entry in to_find:
    base_set = set(base)
    for entry in base_set:
        if not entry.endswith(to_find_entry):
            base.remove(entry)
util.copy_to_clipboard(sorted(base, key=str.lower))
