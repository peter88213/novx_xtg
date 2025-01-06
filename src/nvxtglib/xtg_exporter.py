"""Provide an XTG exporter class for novelibre.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novx_xtg
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from nvlib.model.converter.converter_ff import ConverterFf
from nvlib.model.novx.novx_file import NovxFile
from nvxtglib.xtg_file import XtgFile


class XtgExporter(ConverterFf):
    """A converter class for XPress tagged file export.

    Class constants:
        EXPORT_SOURCE_CLASSES -- List of YwFile subclasses from which can be exported.
        EXPORT_TARGET_CLASSES -- List of FileExport subclasses to which export is possible.
    """
    EXPORT_SOURCE_CLASSES = [NovxFile]
    EXPORT_TARGET_CLASSES = [XtgFile]

    def _confirm_overwrite(self, filePath):
        """Overrides the superclass method."""
        return True
