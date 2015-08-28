__author__ = 'jens'

import Tkinter


def add_indent(indent, text, indent_text=' '):
    for x in xrange(indent):
        text = indent_text + text
    return text


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


def copy_to_clipboard(s):
    tk = Tkinter.Tk()
    tk.withdraw()
    tk.clipboard_clear()
    tk.clipboard_append(print_prep(s))
    tk.destroy()


def raw_multi_line_input(sentinel=''):
    return iter(raw_input, sentinel)
