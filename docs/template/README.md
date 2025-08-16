[![Download the latest release](docs/img/download-button.png)](https://raw.githubusercontent.com/peter88213/novx_xtg/main/dist/novx_xtg_v0.99.0.pyz)
[![Changelog](docs/img/changelog-button.png)](docs/changelog.md)
[![News/Feedback](docs/img/news-button.png)](https://github.com/peter88213/novelibre/discussions)
[![User guide](docs/img/help-button.png)](https://peter88213.github.io/novx_xtg/help/)


# ![X](src/icons/xLogo32.png) novx_xtg

The novx_xtg Python script exports [novelibre](https://github.com/peter88213/novelibre/) projects as a whole in the *XPress Tags* format for the Quark XPress DTP software. It generates an XTG file ready for import into a QX book project. This is done based on template files for chapters and sections, so you can be quite flexible with the program output. In addition, the exporter script can take some routine work off your hands, for example, formatting figures and acronyms in a special way, if desired. Formatting codes and paragraph/character style tags are read from a configuration file.
Optionally, one XTG file per chapter can be generated.

![Screenshot](docs/Screenshots/screen01.png)

## Requirements

- Windows.
- [Python](https://www.python.org/) version 3.6+.

## Download and install

### Default: Executable Python zip archive

Download the latest release [novx_xtg_v0.99.0.pyz](https://github.com/peter88213/novx_xtg/raw/main/dist/novx_xtg_v0.99.0.pyz)

- Launch *novx_xtg_v0.99.0.pyz* by double-clicking (Windows/Linux desktop),
- or execute `python novx_xtg_v0.99.0.pyz` (Windows), resp. `python3 novx_xtg_v0.99.0.pyz` (Linux) on the command line.

#### Important

Many web browsers recognize the download as an executable file and offer to open it immediately. 
This starts the installation.

However, depending on your security settings, your browser may 
initially  refuse  to download the executable file. 
In this case, your confirmation or an additional action is required. 
If this is not possible, you have the option of downloading 
the zip file. 


### Alternative: Zip file

The package is also available in zip format: [novx_xtg_v0.99.0.zip](https://github.com/peter88213/novx_xtg/raw/main/dist/novx_xtg_v0.99.0.zip)

- Extract the *novx_xtg_v0.99.0* folder from the downloaded zipfile "novx_xtg_v0.99.0.zip".
- Move into this new folder and launch *setup.py* by double-clicking (Windows/Linux desktop), 
- or execute `python setup.py` (Windows), resp. `python3 setup.py` (Linux) on the command line.

---

[Changelog](docs/changelog.md)

## Usage

See the [user guide](https://peter88213.github.io/nv_custom_export/help/)

## Credits

- The logo and the file icons are made using the free *Pusab* font by Ryoichi Tsunekawa, [Flat-it](http://flat-it.com/).
- User *Hunter_71* presented the number to English conversion algorithm on [stack overflow](https://stackoverflow.com/a/51849443).
- User *Aristide* presented the integer to roman numeral conversion on [stack overflow](https://stackoverflow.com/a/47713392).

## License

This is Open Source software, and *novx_xtg* is licensed under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novx_xtg/blob/main/LICENSE) file.
