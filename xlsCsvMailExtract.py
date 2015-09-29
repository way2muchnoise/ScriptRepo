__author__ = 'jens'

import xlrd
import csv
import re
import os
import util

# Gets all lines in xls or csv files by given regex and folder

folderName = raw_input('Folder: ')
filePattern = raw_input('Regex: ')
is_csv = filePattern.endswith('.csv')
mails = []
read = 1

for file in os.listdir(folderName):
    if re.match(filePattern, file):
        if is_csv:
            with open(folderName + "/" + file) as csvfile:
                for row in csvfile:
                    mails.extend(re.findall(r'[\w\.-]+@[\w\.-]+', row))
        else:
            book = xlrd.open_workbook(folderName + "/" + file)
            for sheet in book.sheets():
                for row in sheet.get_rows():
                    for cell in row:
                        if type(cell.value) is unicode:
                            mails.extend(re.findall(r'[\w\.-]+@[\w\.-]+', cell.value))
        print('Files read: ' + repr(read))
        read += 1
print('Filtering double mails (total mails ' + repr(len(mails)) + ')')
util.copy_to_clipboard(sorted(util.create_set(mails, lambda s: s.lower()),
                              key=(str.lower if is_csv else unicode.lower)))
