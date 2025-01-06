"""Regression test for the novx_xtg project.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from shutil import copyfile
import os
import unittest
import novx_xtg_

# Test environment

# The paths are relative to the "test" directory,
# where this script is placed and executed

TEST_PATH = f'{os.getcwd()}/../test'
TEST_DATA_PATH = f'{TEST_PATH}/data/'
TEST_EXEC_PATH = f'{TEST_PATH}/temp/'
TEMPLATES = 'novx_xtg/'

# To be placed in TEST_DATA_PATH:
REFERENCE_NOVX = f'{TEST_DATA_PATH}normal.novx'
REFERENCE_XTG_TEMPLATES = f'{TEST_DATA_PATH}templates.XTG'
REFERENCE_XTG_DEFAULTS = f'{TEST_DATA_PATH}defaults.XTG'

# Test data
TEST_NOVX = f'{TEST_EXEC_PATH}yw7 Sample Project.novx'
TEST_XTG = f'{TEST_EXEC_PATH}yw7 Sample Project.XTG'


def read_file(inputFile):
    try:
        with open(inputFile, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        # HTML files exported by a word processor may be ANSI encoded.
        with open(inputFile, 'r') as f:
            return f.read()


def remove_all_testfiles():

    try:
        os.remove(TEST_NOVX)
    except:
        pass
    try:
        os.remove(TEST_XTG)
    except:
        pass

    for f in os.listdir(f'{TEST_EXEC_PATH}{TEMPLATES}'):
        os.remove(f'{TEST_EXEC_PATH}{TEMPLATES}{f}')


class NormalOperation(unittest.TestCase):
    """Test case: Normal operation."""

    def setUp(self):

        try:
            os.mkdir(TEST_EXEC_PATH)

        except:
            pass

        try:
            os.mkdir(f'{TEST_EXEC_PATH}{TEMPLATES}')

        except:
            pass

        remove_all_testfiles()
        copyfile(REFERENCE_NOVX, TEST_NOVX)

    def test_templates(self):

        for f in os.listdir(f'{TEST_DATA_PATH}{TEMPLATES}'):
            copyfile(f'{TEST_DATA_PATH}{TEMPLATES}{f}',
                     f'{TEST_EXEC_PATH}{TEMPLATES}{f}')

        os.chdir(TEST_EXEC_PATH)

        novx_xtg_.main(TEST_NOVX, silentMode=True)

        self.assertEqual(read_file(TEST_XTG),
                         read_file(REFERENCE_XTG_TEMPLATES))

    def test_defaults(self):
        os.chdir(TEST_EXEC_PATH)

        novx_xtg_.main(TEST_NOVX, silentMode=True)

        self.assertEqual(read_file(TEST_XTG),
                         read_file(REFERENCE_XTG_DEFAULTS))

    def tearDown(self):
        remove_all_testfiles()


def main():
    unittest.main()


if __name__ == '__main__':
    main()
