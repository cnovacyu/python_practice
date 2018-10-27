#! python3
# Chapter 8 example problem
#mcb.pyw - Saves and loads pieces of text to the clipboard
#Usage: py.exe mcb.pyw save <keyword> - Saves clipboad to keyword.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#       py.exe mcb.pwy list - Loads all keywords to clipboard.
#       py.exe mcb.pwy delete <keyword> - Deletes keyword from clipboard.
#       py.exe mcb.pwy delete - Deletes all keywords from clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete a keyword from the clipboard
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # Copy list of all keywords to clipboard. Paste in a word editor to view 
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Type in a keyword to load content to clipboard and paste where needed
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    #Delete all keywords from the clipboard
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

mcbShelf.close()