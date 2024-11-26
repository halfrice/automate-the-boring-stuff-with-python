#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword to clipboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, re

ynRegex = re.compile(r'^(y|n)$', re.IGNORECASE)
mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in list(mcbShelf.keys()):
        ynResult = ynRegex.match(input(f'Confirm deletion of "{sys.argv[2]}"? (y/n): '))
        if ynResult and ynResult.group(1).lower() == 'y':
            del mcbShelf[sys.argv[2]]
            print(f'Success: "{sys.argv[2]}" deleted.')
        else:
            print(f'Abort: "{sys.argv[2]}" was not deleted.')
    else:
        print(f'Error: No key exists with the name {sys.argv[2]}')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(*list(mcbShelf.keys()), sep='\n')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f'Contents from "{sys.argv[1]}" copied to clipboard.')

mcbShelf.close()
