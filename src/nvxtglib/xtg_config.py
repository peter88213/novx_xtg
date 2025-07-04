"""Provide a configuration class for reading and writing INI files.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import json
from nvlib.configuration.configuration import Configuration


class XtgConfig(Configuration):
    """Read/write the program configuration.
    """

    def __init__(self, settings={}, options={}, templates={}, lookup={}):
        """Overrides the superclass constructor, redefining _sLabel.
        """
        self.templates = None
        self.lookup = None
        self._sLabel = 'STYLES'
        self._oLabel = 'OPTIONS'
        self.set(settings, options, templates, lookup)

    def set(self, settings=None, options=None, templates=None, lookup=None):
        """Overrides the superclass method.
        """
        if settings is not None:
            self.settings = settings.copy()
        if options is not None:
            self.options = options.copy()
        if templates is not None:
            self.templates = templates.copy()
        if lookup is not None:
            self.lookup = lookup.copy()

    def read(self, iniFile):
        """Read a configuration file.
        Settings and options that can not be read in, remain unchanged.
        Extends the superclass.
        """
        super().read(iniFile)
        iniPath = os.path.dirname(iniFile)
        for template in self.templates:
            try:
                with open(
                    f'{iniPath}/{template}.XTG',
                    'r',
                    encoding='utf-8',
                ) as f:
                    self.templates[template] = f.read()
            except:
                pass
        for lookup in self.lookup:
            try:
                with open(
                    f'{iniPath}/{lookup}.json',
                    'r',
                    encoding='utf-8',
                ) as f:
                    self.lookup[lookup] = json.load(f)
            except:
                pass

    def write(self, iniFile):
        """Save the configuration to iniFile.
        """
        super().write(iniFile)
        iniPath = os.path.dirname(iniFile)
        for template in self.templates:
            with open(f'{iniPath}/{template}.XTG', 'w', encoding='utf-8') as f:
                f.write(self.templates[template])
        for lookup in self.lookup:
            with open(f'{iniPath}/{lookup}.json', 'w', encoding='utf-8') as f:
                json.dump(self.lookup[lookup], f, indent=4)
