# novx_xtg - XPress tagged text export from noveltree projects

For more information, see the [project homepage](https://peter88213.github.io/novx_xtg) with description and download instructions.

## Development

*novx_xtg* is organized as an Eclipse PyDev project. The official release branch on GitHub is *main*.

*novx_xtg* depends on the [novxlib](https://github.com/peter88213/novxlib) library which must be present in your file system. It is organized as an Eclipse PyDev project. The official release branch on GitHub is *main*.

### Mandatory directory structure for building the application script

```
.
├── novxlib/
│   └── src/
│       └── novxlib/
└── novx_xtg/
    ├── src/
    ├── test/
    └── tools/ 
        └── build.xml
```

### Conventions

See https://github.com/peter88213/novxlib/blob/main/docs/conventions.md

## Development tools

- [Python](https://python.org) version 3.11.
- [Eclipse IDE](https://eclipse.org) with [PyDev](https://pydev.org) and *EGit*.
- *Apache Ant* is used for building the application.

## Credits

- The icons are made using the free *Pusab* font by Ryoichi Tsunekawa, [Flat-it](http://flat-it.com/).
- User *Hunter_71* presented the number to English conversion algorithm on [stack overflow](https://stackoverflow.com/a/51849443).
- User *Aristide* presented the integer to roman numeral conversion on [stack overflow](https://stackoverflow.com/a/47713392).


## License

This is Open Source software, and *novx_xtg* is licensed under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novx_xtg/blob/main/LICENSE) file.
