# Contributing

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

