#!/usr/bin/env python3

# multi_clipboard_extended.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe multi_clipboard_extended.py save <keyword> - Saves clipboard to keyword.
#        py.exe multi_clipboard_extended.py delete <keyword> - Deletes keyword to clipboard.
#        py.exe multi_clipboard_extended.py <keyword> - Loads keyword to clipboard.
#        py.exe multi_clipboard_extended.py list - Loads all keywords to clipboard.

import pyperclip
import re
import shelve
import sys

yes_no_regex = re.compile(r'^(y|n)$', re.IGNORECASE)
mcb_shelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in list(mcb_shelf.keys()):
        yes_no_result = yes_no_regex.match(
            input(f'Confirm deletion of "{sys.argv[2]}"? (y/n): ')
        )
        if yes_no_result and yes_no_result.group(1).lower() == 'y':
            del mcb_shelf[sys.argv[2]]
            print(f'Success: "{sys.argv[2]}" deleted.')
        else:
            print(f'Abort: "{sys.argv[2]}" was not deleted.')
    else:
        print(f'Error: No key exists with the name {sys.argv[2]}')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        print(*list(mcb_shelf.keys()), sep='\n')
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print(f'Contents from "{sys.argv[1]}" copied to clipboard.')

mcb_shelf.close()
