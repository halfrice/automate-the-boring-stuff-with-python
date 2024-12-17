#!/usr/bin/env python3

# selective_copy.py
# Usage: py.exe selective_copy.py <path/to/source/dir>

import glob
import os
import re
import shutil
import sys
from pathlib import Path

extension_regex = re.compile(r'(\.+(\w+))$')
yes_no_regex = re.compile(r'^(y|n)$', re.IGNORECASE)

# Get file extension to search for from user
while True:
    extension_input = input('Enter a file extension: ').lower()
    extension_match = extension_regex.match(extension_input)
    if extension_match is not None:
        extension = extension_match.group()
        break
    else:
        print('Invalid file extension. Try again.')

# Check sys.argv exists and use as base dir, otherwise default to cwd
if len(sys.argv) > 1:
    source_path = Path(sys.argv[1])
else:
    source_path = Path.cwd()

# Recursive search through directories and create a list of files to copy
files = glob.glob(str(source_path) + '/**/*' + extension, recursive=True)
if len(files) > 0:
    print(f'Found {len(files)} files:')
    for file in files:
        print(file)
else:
    print(f'No files found with the extension: {extension}')
    sys.exit()

# Confirm copy
dest_path = source_path.parents[0] / (
    f'{source_path.name}-copy-{extension_match.group(2)}'
)
print(f'Prepared to copy files to: {dest_path}')
while True:
    confirmation_input = input('Proceed? (y/n): ').lower()
    confirmation_match = yes_no_regex.match(confirmation_input)
    if confirmation_match is not None:
        if confirmation_match.group() == 'y':
            break
        else:
            sys.exit()
    else:
        print('Invalid input. Try again.')

# Check if destination folder exists and create it
if not dest_path.exists() and not dest_path.is_dir():
    os.mkdir(dest_path)
else:
    # Confirm overwrite
    while True:
        overwrite_input = input(
            'Destination path already exists. Overwrite? (y/n): '
        ).lower()
        overwrite_match = yes_no_regex.match(overwrite_input)
        if overwrite_match is not None:
            if overwrite_match.group() == 'y':
                break
            else:
                sys.exit()
        else:
            print('Invalid input. Try again.')


# Copy files into destination folder
for file in files:
    p = Path(file)
    shutil.copy(p, dest_path)
print(f'Copied {len(files)} files into: {dest_path}')
