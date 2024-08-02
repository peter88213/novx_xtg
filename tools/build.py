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

SOURCE_DIR = '../src/'
TEST_DIR =  '../test/'
SOURCE_FILE = f'{SOURCE_DIR}novx_xtg_.py'
TEST_FILE = f'{TEST_DIR}novx_xtg.py'


def main():
    inliner.run(SOURCE_FILE, TEST_FILE, 'nvxtglib', '../src/', copynovxlib=False)
    inliner.run(TEST_FILE, TEST_FILE, 'novxlib', '../../novxlib/src/', copynovxlib=False)
    # inliner.run(SOURCE_FILE, TEST_FILE, 'nvxtglib', '../src/')
    # inliner.run(TEST_FILE, TEST_FILE, 'novxlib', '../src/')
    print('Done.')


if __name__ == '__main__':
    main()
