"""Helper file for novx_xtg test.

Create config file.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os
from nvxtglib.xtg_config import XtgConfig
from novx_xtg_ import STYLES
from novx_xtg_ import OPTIONS
from novx_xtg_ import TEMPLATES
from novx_xtg_ import APPNAME


def run(iniFile):
    iniDir = os.path.dirname(iniFile)
    if not os.path.isdir(iniDir):
        os.makedirs(iniDir)
    configuration = XtgConfig(STYLES, OPTIONS, TEMPLATES)
    configuration.write(iniFile)
    print(f'{iniFile} written.')


if __name__ == '__main__':
    try:
        iniFile = sys.argv[1]
    except:
        iniFile = f'./novx_xtg/{APPNAME}.ini'
    run(iniFile)
