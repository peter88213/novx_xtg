"""Build a Python script for the novx_xtg distribution.
        
In order to distribute a single script without dependencies, 
this script "inlines" all modules imported from the novxlib package.

The novxlib library (see see https://github.com/peter88213/novxlib)
must be located on the same directory level as the novx_xtg project. 

Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../novxlib/src')
import inliner

SRC = '../src/'
BUILD = '../test/'
SOURCE_FILE = f'{SRC}novx_xtg_.py'
TARGET_FILE = f'{BUILD}novx_xtg.py'


def main():
    inliner.run(SOURCE_FILE, TARGET_FILE, 'nvxtglib', '../src/', copynovxlib=False)
    inliner.run(TARGET_FILE, TARGET_FILE, 'novxlib', '../../novxlib/src/', copynovxlib=False)
    # inliner.run(SOURCE_FILE, TARGET_FILE, 'nvxtglib', '../src/')
    # inliner.run(TARGET_FILE, TARGET_FILE, 'novxlib', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
