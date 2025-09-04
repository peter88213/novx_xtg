"""Export novelibre project to XPress tagged text.

Version @release
Requires Python 3.7+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or 
(at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.
"""
import os
from pathlib import Path
import sys

from nvlib.gui.set_icon_tk import set_icon
from nvlib.user_interface.ui import Ui
from nvlib.user_interface.ui_tk import UiTk
from nvxtglib.xtg_config import XtgConfig
from nvxtglib.xtg_exporter import XtgExporter

SUFFIX = ''
APPNAME = 'novx_xtg'
SCENE_DIVIDER = ''
STYLES = dict(
    first_paragraph='@Text body:',
    indented_paragraph='@Text body indent:',
    other_paragraph='@First line indent:',
    italic='<@Emphasis>',
    italic0='<@$p>',
    bold='<@Strong emphasis>',
    bold0='<@$p>',
    acronym='',
    acronym0='',
    figure='',
    figure0='',
    )
TEMPLATES = dict(
    file_header='<v11.10><e9>\n',
    part_template='@Heading 1:${Title}\n',
    chapter_template='@Heading 1:${Title}\n',
    first_section_template='@Text body:$SectionContent\n',
    section_template='@Text body:$SectionContent\n',
    appended_section_template='$SectionContent\n',
    section_divider=f'@Heading 3:{SCENE_DIVIDER}\n',
    )
OPTIONS = dict(
    adjust_digits=True,
    space_points=True,
    per_chapter=False,
    )
LOOKUP = {'language_codes':{}}


def main(sourcePath, silentMode=True, installDir='.'):
    major = sys.version_info.major
    minor = sys.version_info.minor
    if  major != 3 or minor < 7:
        raise Exception(
            f'Wrong Python version installed: {major}.{minor}.\n'
            'Must be 3.7 or newer.'
        )

    if silentMode:
        ui = Ui('')
    else:
        ui = UiTk('Export XTG from novelibre @release')
        set_icon(ui.root, icon='xLogo32')

    #--- Try to get persistent configuration data
    sourceDir = os.path.dirname(sourcePath)
    if not sourceDir:
        sourceDir = '.'
    iniFileName = f'{APPNAME}.ini'
    iniFiles = [
        f'{installDir}/config/{iniFileName}',
        f'{sourceDir}/{APPNAME}/{iniFileName}',
    ]
    configuration = XtgConfig(STYLES, OPTIONS, TEMPLATES, LOOKUP)
    for iniFile in iniFiles:
        configuration.read(iniFile)
    kwargs = {'suffix': SUFFIX}
    kwargs.update(configuration.settings)
    kwargs.update(configuration.options)
    kwargs.update(configuration.templates)
    kwargs.update(configuration.lookup)
    converter = XtgExporter()
    converter.ui = ui
    converter.run(sourcePath, **kwargs)
    ui.start()


if __name__ == '__main__':
    silentMode = False
    sourcePath = ''
    if len(sys.argv) > 1:
        sourcePath = sys.argv[-1]
        silentMode = sys.argv[1] in ['--silent', '-s']
    else:
        print('usage: novx_xtg.py [--silent] Sourcefile')
        sys.exit(1)
    try:
        homeDir = str(Path.home()).replace('\\', '/')
        installDir = f'{homeDir}/.novx/{APPNAME}/config'
    except:
        installDir = '.'
    main(sourcePath, silentMode, installDir)
