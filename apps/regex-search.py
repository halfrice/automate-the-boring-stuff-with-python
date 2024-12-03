#!/usr/bin/evn python3

# regex-search.py - Opens text files and matches user-suppolied regex patterns.
# Usage: py.exe regex-search.py <path/to/dir> - Prints regex matching lines to terminal.

import re
import sys
from pathlib import Path


# Check sys.argv exists and use as base dir, otherwise default to cwd
if len(sys.argv) > 1:
    path = Path(sys.argv[1])
else:
    path = Path.cwd()

# Provide a message and exit if path is not a valid directory
if not path.exists() or not path.is_dir():
    print(f'regex-search: {path}: Is not a directory')
    sys.exit()

# Get a valid regex pattern from user
user_input = ''
while True:
    user_input = input('Enter a regular expression:\n')
    try:
        raw_user_input = r'{}'.format(user_input)
        user_regex = re.compile(raw_user_input)
        break
    except re.error:
        print('You entered a non-valid regular expression. Try again.')
        continue

# Search through .txt files and save lines that match regex
matches = []
files = list(path.glob('*.txt'))
for file in files:
    with open(file) as open_file:
        data = open_file.read().splitlines()
        for line in data:
            result = user_regex.search(line)
            if result:
                # Format line to emulate grep search
                line_split = line.split(result.group(), 1)
                red_result = '\033[91m{}\033[00m'.format(result.group())
                s = f'{path}:{line_split[0]+red_result+line_split[1]}'
                matches.append(s)

# Display results
print(f'Searched {len(files)} .txt files, found {len(matches)} matches:')
for f in matches:
    print(f)
