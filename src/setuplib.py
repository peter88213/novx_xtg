"""novx_xtg installer library module. 

Version @release

Copyright (c) 2021 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from pathlib import Path
from shutil import copy2
from shutil import copytree
import stat
import sys
from tkinter import messagebox
import zipfile

APPNAME = 'novx_xtg'
VERSION = ' @release'
APP = f'{APPNAME}.py'

SHORTCUT_MESSAGE = f'''
Now you might want to create a shortcut on your desktop.  

On Windows, open the installation folder, 
hold down the Alt key on your keyboard, 
and then drag and drop {APP} to your desktop.

On Linux, create a launcher on your desktop. 
With xfce for instance, the launcher's command may look like this:
python3 /home/peter/.novx/novx_xtg/novx_xtg.py %F
'''

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


def open_folder(installDir):
    try:
        os.startfile(os.path.normpath(installDir))
        # Windows
    except:
        try:
            os.system('xdg-open "%s"' % os.path.normpath(installDir))
            # Linux
        except:
            try:
                os.system('open "%s"' % os.path.normpath(installDir))
                # Mac
            except:
                pass


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

    print(f'*** Installing {APPNAME} {VERSION} ***\n')
    homePath = str(Path.home()).replace('\\', '/')
    applicationDir = f'{homePath}/.novx/'
    if not os.path.isdir(applicationDir):
        print(
            'ERROR: Cannot find a novelibre installation '
            f'at "{os.path.normpath(applicationDir)}".'
        )
        input('Press any key to quit.')
        sys.exit(1)

    installDir = f'{applicationDir}{APPNAME}'
    if os.path.isfile(f'{installDir}/{APP}'):
        simpleUpdate = True
    else:
        simpleUpdate = False

    #--- Install the new version.
    print(f'Copying "{APP}" ...')
    copy_file(APP, installDir)

    #--- Install the icon files.
    print('Copying icons ...')
    copy_tree('icons', installDir)

    #--- Make the script executable under Linux.
    st = os.stat(f'{installDir}/{APP}')
    os.chmod(f'{installDir}/{APP}', st.st_mode | stat.S_IEXEC)

    #--- Provide the sample files.
    print('Copying sample files ...')
    copy_tree('sample', installDir)

    #--- Display a success message.
    print(
        f'\nSucessfully installed {APPNAME} '
        f'at "{os.path.normpath(installDir)}".'
    )

    #--- Ask for shortcut creation.
    if not simpleUpdate:
        print(SHORTCUT_MESSAGE)
        if messagebox.askyesno(
            title=f'{APPNAME} {VERSION} Setup',
            message='Open the installation folder now?',
        ):
            open_folder(installDir)
            input('Press any key to quit.')
    else:
        input('Press any key to quit.')

