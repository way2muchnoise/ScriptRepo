__author__ = 'jens'

import Tkinter


# Adds certain amount of indent before a given text
def add_indent(indent, text, indent_text=' '):
    for x in xrange(indent):
        text = indent_text + text
    return text


# Advanced print preparation function
def print_prep(raw, depth=0, indent_text=' '):
    prepped = ''
    if type(raw) is dict:
        for k, v in raw.items():
            if hasattr(v, '__iter__'):
                prepped += add_indent(depth, k, indent_text)
                prepped += print_prep(v, depth+1, indent_text)
            else:
                prepped += add_indent(depth, '%s : %s' % (k, v), indent_text)
            prepped += '\n'
    elif type(raw) is list:
        for v in raw:
            if hasattr(v, '__iter__'):
                prepped += print_prep(v, depth+1, indent_text)
            else:
                prepped += add_indent(depth, v, indent_text)
            prepped += '\n'
    else:
        prepped += add_indent(depth, raw, indent_text)
        prepped += '\n'
    return prepped


# Copy the given object print prepped to the clipboard
def copy_to_clipboard(raw):
    tk = Tkinter.Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(print_prep(raw))
    tk.destroy()


# Get contents of keyboard
def copy_from_clipboard():
    tk = Tkinter.Tk()
    tk.withdraw()
    clipboard = tk.clipboard_get()
    tk.destroy()
    return clipboard


# Read a multi line input for the console with given sentinel
def raw_multi_line_input(sentinel=''):
    return iter(raw_input, sentinel)


# create set using manipulator in raw data
def create_set(raw, manipulator=lambda s: s):
    raw = set(raw)
    result = []
    for i in raw:
        if manipulator(i) not in result:
            result.append(i)
    return set(result)
