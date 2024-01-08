"""Export noveltree project to XPress tagged text.

Version @release
Requires Python 3.6+
Copyright (c) 2024 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from pathlib import Path
from novxlib.ui.ui_tk import UiTk
from novxlib.ui.ui import Ui
from novxlib.ui.set_icon_tk import set_icon
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
    if silentMode:
        ui = Ui('')
    else:
        ui = UiTk('Export XTG from noveltree @release')
        set_icon(ui.root, icon='xLogo32')

    #--- Try to get persistent configuration data
    sourceDir = os.path.dirname(sourcePath)
    if not sourceDir:
        sourceDir = '.'
    iniFileName = f'{APPNAME}.ini'
    iniFiles = [f'{installDir}/config/{iniFileName}', f'{sourceDir}/{APPNAME}/{iniFileName}']
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
        installDir = f'{homeDir}/.noveltree/{APPNAME}/config'
    except:
        installDir = '.'
    main(sourcePath, silentMode, installDir)
