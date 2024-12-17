#!/usr/bin/env python3

# deleting_unneeded_files.py
# Usage: py.exe deleting_unneeded_files.py <path/to/source/dir>

import os
import sys
from pathlib import Path

THRESHOLD = 100000000  # 100 MB

# Check if user supplied a dir to search, default to cwd if none provided
source_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

# Find files larger than 100 MB
lg_files = []
for root, dirs, files in os.walk(source_path):
    for file in files:
        path = Path(root) / file
        size = os.path.getsize(path)
        if size > THRESHOLD:
            size //= 1000000
            lg_files.append([f'{size}MB', str(path)])

# If no large files found, gracefully exit
if not lg_files:
    sys.exit()

# Get the largest filesize found and format for pretty display
widest = 0
for f in lg_files:
    size = len(f[0])
    if size > widest:
        widest = size

# Display size and absolute path
for f in lg_files:
    size = f[0].rjust(widest)
    path = f[1]
    print(f'{size} {path}')
