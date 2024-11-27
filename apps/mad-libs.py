#!/usr/bin/env python3

# mad-libs.py - Replaces key phrases within a text file with user-prompted words.
# Usage: py.exe mad-libs.py <path/to/file.txt> - Overwrites file with modified version.

import re
import sys
from pathlib import Path

keys_regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
vowels_regex = re.compile(r'[aeiouAEIOU]')
dot_txt_regex = re.compile(r'^(.+?)\.txt$')


def is_vowel(c):
    if vowels_regex.match(c):
        return True
    return False


def is_text_file(s):
    if dot_txt_regex.match(s):
        return True
    return False


data = None
path = None

if len(sys.argv) > 1:
    path = Path(sys.argv[1])

if path.is_file():
    with open(path) as file:
        data = file.read()
    print(f'{data}')

    matches = keys_regex.findall(data)
    for target in matches:
        a = 'a'
        if is_vowel(target[0]):
            a += 'n'
        replace_with_input = input(f'Enter {a} {target.lower()}:\n')
        data = data.replace(target, replace_with_input, 1)

    new_path = Path(path.parent) / (path.stem + '-new' + path.suffix)
    if new_path.is_file():
        file_input = ''
        while not file_input:
            file_input = input(
                f'The default file: {str(new_path)} already exists.\n'
                'Please select an option: (O)verwrite | (R)ename | (E)xit\n'
            ).lower()
            if file_input == 'o':
                continue
            elif file_input == 'r':
                rename_input = input('Enter new filename:\n')
                if not is_text_file(rename_input):
                    rename_input += '.txt'
                new_path = Path(path.parent) / rename_input
                if new_path.is_file():
                    file_input = ''
            else:
                sys.exit()

    with open(new_path, 'w') as new_file:
        new_file.write(data)
    print(f'{data}')
    print(f'Text saved to {str(new_path)}:')
else:
    print(f'Error: {path} does not exist.')
