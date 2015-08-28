__author__ = 'jens'

import util

lines = util.raw_multi_line_input()
phones = []
for line in lines:
    splitted = line.split(';')
    if len(splitted) < 4:
        continue
    phone = splitted[3].translate(None, ' /.+')
    if len(phone) is 10:
        phone = '0032' + phone[1:]
    elif len(phone) is 11:
        phone = '00' + phone
    phones.append(phone)
util.copy_to_clipboard(phones)
