"""Provide a configuration class for reading and writing INI files.

Copyright (c) Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from configparser import ConfigParser
import json
import os


class XtgConfig:
    """Read/write the program configuration.
    """

    def __init__(self, settings={}, options={}, templates={}, lookup={}):
        self.templates = None
        self.lookup = None
        self._sLabel = 'STYLES'
        self._oLabel = 'OPTIONS'
        self.set(settings, options, templates, lookup)

    def set(self, settings=None, options=None, templates=None, lookup=None):
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
        
        Positional arguments:
            iniFile: str -- path configuration file path.
            
        Settings and options that can not be read in, remain unchanged.
        """
        config = ConfigParser()
        config.read(iniFile, encoding='utf-8')
        if config.has_section(self._sLabel):
            section = config[self._sLabel]
            for setting in self.settings:
                fallback = self.settings[setting]
                self.settings[setting] = section.get(setting, fallback)
        if config.has_section(self._oLabel):
            section = config[self._oLabel]
            for option in self.options:
                fallback = self.options[option]
                self.options[option] = section.getboolean(option, fallback)
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

        Positional arguments:
            iniFile: str -- path configuration file path.
        """
        config = ConfigParser()
        if self.settings:
            config.add_section(self._sLabel)
            for settingId in self.settings:
                config.set(
                    self._sLabel,
                    settingId,
                    str(self.settings[settingId]),
                )
        if self.options:
            config.add_section(self._oLabel)
            for settingId in self.options:
                if self.options[settingId]:
                    config.set(self._oLabel, settingId, 'Yes')
                else:
                    config.set(self._oLabel, settingId, 'No')
        with open(iniFile, 'w', encoding='utf-8') as f:
            config.write(f)
        iniPath = os.path.dirname(iniFile)
        for template in self.templates:
            with open(f'{iniPath}/{template}.XTG', 'w', encoding='utf-8') as f:
                f.write(self.templates[template])
        for lookup in self.lookup:
            with open(f'{iniPath}/{lookup}.json', 'w', encoding='utf-8') as f:
                json.dump(self.lookup[lookup], f, indent=4)
