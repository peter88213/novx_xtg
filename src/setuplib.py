"""novx_xtg installer library module. 

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from shutil import copytree
from shutil import copy2
import zipfile
import os
import sys
import stat
from pathlib import Path

APPNAME = 'novx_xtg'
VERSION = ' @release'
APP = f'{APPNAME}.py'

pyz = os.path.dirname(__file__)


def extract_file(sourceFile, targetDir):
    with zipfile.ZipFile(pyz) as z:
        z.extract(sourceFile, targetDir)


def extract_tree(sourceDir, targetDir):
    with zipfile.ZipFile(pyz) as z:
        for file in z.namelist():
            if file.startswith(f'{sourceDir}/'):
                z.extract(file, targetDir)


def cp_tree(sourceDir, targetDir):
    copytree(sourceDir, f'{targetDir}/{sourceDir}', dirs_exist_ok=True)


def main(zipped=True):
    if zipped:
        copy_file = extract_file
        copy_tree = extract_tree
    else:
        copy_file = copy2
        copy_tree = cp_tree

    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    print(f'*** Installing {APPNAME} {VERSION} ***')
    homePath = str(Path.home()).replace('\\', '/')
    applicationDir = f'{homePath}/.novx/'
    if os.path.isdir(applicationDir):
        installDir = f'{applicationDir}{APPNAME}'

        # Install the new version.
        print(f'Copying "{APP}" ...')
        copy_file(APP, installDir)

        # Install the icon files.
        print('Copying icons ...')
        copy_tree('icons', installDir)

        # Make the script executable under Linux.
        st = os.stat(f'{installDir}/{APP}')
        os.chmod(f'{installDir}/{APP}', st.st_mode | stat.S_IEXEC)

        # Provide the sample files.
        print('Copying sample files ...')
        copy_tree('sample', installDir)

        # Show a success message.
        print(
            f'Sucessfully installed "{APPNAME}" '
            f'at "{os.path.normpath(installDir)}".'
        )
    else:
        print(
            'ERROR: Cannot find a novelibre installation '
            f'at "{os.path.normpath(applicationDir)}".'
        )

    input('Press any key to quit.')
