__author__ = 'jens'

import util

# Remove all double entries and entries that don't have a given extension out of the second list

print 'Base set'
base = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
print 'Extensions to find in base'
to_find = util.create_set(util.raw_multi_line_input(), lambda s: s.lower())
found = []
for to_find_entry in to_find:
    for entry in base:
        if entry.endswith(to_find_entry):
            found.append(entry)
util.copy_to_clipboard(sorted(found, key=str.lower))
