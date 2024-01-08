"""Helper file for novx_xtg test.

Create config file and template files for German QX document.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import os

from nvxtglib.xtg_config import XtgConfig
from novx_xtg_ import APPNAME

SCENE_DIVIDER = ''
TEMPLATES = dict(file_header='<v11.10><e9>\n',
                 part_template='@Überschrift 1:${Title}\n',
                 chapter_template='@Überschrift 1:${Title}\n',
                 first_section_template='@Textkörper:$SectionContent\n',
                 section_template='@Textkörper:$SectionContent\n',
                 appended_section_template='$SectionContent\n',
                 section_divider=f'@Überschrift 3:{SCENE_DIVIDER}\n',
                 )
STYLES = dict(first_paragraph='@Textkörper:',
              indented_paragraph='@Textkörper Einrückung:',
              other_paragraph='@Textkörper Einzug:',
              italic='<@Betont>',
              italic0='<@$p>',
              bold='<@Stark betont>',
              bold0='<@$p>',
              acronym='<t4z9>',
              acronym0='<tz$p>',
              figure='<f"Adobe Garamond Small Caps & Old">',
              figure0='<f$p>',
              )
OPTIONS = dict(
    adjust_digits='Yes',
    space_points='Yes',
    per_chapter='Yes',
)


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
