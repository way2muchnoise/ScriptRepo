__author__ = 'jens'

import re
import os
import util

# Gets all lines in files by given regex and folder

folderName = raw_input('Folder: ')
filePattern = raw_input('Regex: ')
lines = []

for file in os.listdir(folderName):
    if re.match(filePattern, file):
        lines.extend(open(folderName + "/" + file).read().split('\n'))

util.copy_to_clipboard(lines)
