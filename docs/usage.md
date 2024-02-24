[Project homepage](https://github.com/peter88213/novx_xtg) > Instructions for use

---

The novx_xtg Python script runs through all chapters and sections of a novelibre 7 project and fills XTG templates.

## Instructions for use

### Intended usage

The included installation script prompts you to create a shortcut on the desktop. You can launch the program by dragging a novelibre project file and dropping it on the shortcut icon. 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the novelibre project file as an argument, or
- launch the program via a batch file.

usage: `novx_xtg.pyw [--silent] Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the novelibre project file.

#### optional arguments:

`--silent`  suppress error messages and the request to confirm the use of default values

---

## General

### About XTG

The XTG file format uses the *XPress Tags* language, the knowledge of which is assumed. You can 
download the manual *A Guide to XPress Tags* for your program version from the *Quark* web site.

### novelibre text markup

Bold and italics are supported. Other highlighting such as underline and strikethrough are lost.

### Quotation marks and punctuation

It is assumed that quotation marks and punctuation marks are already set correctly; this is best done in advance with a word processor, e.g. via novelibre's "proof read" function. 

## Configuration

- Place a subfolder named **novx_xtg** in the novelibre project folder. It contains the configuration file
and all template files as listed below to be applied to this project. The best way is to copy the provided sample folder and customize the contained files with a text editor according to your needs. 

- If there is no configuration data in the project file, data stored in `c:\Users\<user name>.novelibre\novx_xtg\config` is used prior to the script's default configuration data.

- If a template file or a configuration entry is missing, *novx_xtg* uses the lower priority source as a fallback. 


### Configuration file

This is an exapmle configuration file containing the default values mentioned above:

```ini
[STYLES]
first_paragraph = @Text body:

# XPress tag for paragraphs preceded by a heading or a blank line.

indented_paragraph = @Text body indent:

# XPress tag for indented paragraphs.

other_paragraph = @First line indent:

# XPress tag for regular paragraphs.

italic = <@Emphasis>

# XPress tag opening italic sections. 

italic0 = <@$p>

# XPress tag closing italic sections.

bold = <@Strong emphasis>

# XPress tag opening bold sections.

bold0 = <@$p>

# XPress tag closing bold sections.

acronym =

# XPress tag opening acronyms.
 
acronym0 = 

# XPress tag closing acronyms.

figure =

# XPress tag opening figure groups.

figure0 = 

# XPress tag closing figure groups.

[OPTIONS]

adjust_digits = Yes

# If Yes, adjust digit-separating blanks.

space_points = Yes

# If Yes, space digit-separating points.

per_chapter = No

# If Yes, create one XTG file for each chapter.
# If No, create one XTG file for the entire document.

```

#### Style tags

- **textbody** - The QX paragraph style applied to all paragraphs in a section, except the first. The first paragraph's style can be set in the section level templates.
- **italic** - The opening tag to replace novelibre's *italic* formatting.
- **italic0** - The closing tag to replace novelibre's *italic* formatting.
- **bold** - The opening tag to replace novelibre's *bold* formatting.
- **bold0** - The closing tag to replace novelibre's *bold* formatting.
- **acronym** - The opening tag to format sequences of uppercase characters (e.g. set a slightly smaller font size).
- **acronym0** - The closing tag to format sequences of uppercase characters.
- **figure** - The opening tag to format figures (e.g. switch the font to get "osf" text figures).
- **figure0** - The closing tag to format figures.

#### Options

- **adjust_digits** - Replace regular spaces between digits with thin spaces.
- **space_points** - Insert a thin space after each point that separates digits.
- **per_chapter** - Generate one XTG file per chapter. The file names consist of the chapter's number and title. the files are written to the XTG_Chapters subdirectory.

You can define styles in *fileHeader.XTG*, but it is preferable to use the names of styles that already exist in the QX book project instead.

## List of templates

### Project level templates

- **fileHeader.XTG** - This template must contain at least the version code and encoding indication.

### Chapter level templates

- **partTemplate.XTG** - Chapter header; applied to chapters marked "section beginning".
- **chapterTemplate.XTG** - Chapter header; applied to all "used" and "normal" chapters unless a "part template" exists.


### Section level templates

- **firstSectionTemplate.XTG** - Applied  to sections at the beginning of the chapter.
- **sectionTemplate.XTG** - Applied to "used" sections within "normal" chapters.
- **sectionDivider.XTG** - Section divider placed between sections.
- **appendedSectionTemplate.XTG** - Applied to sections to be appended to the previous section.


## Placeholders

### Syntax

There are two options:

1. $Placeholder
2. ${Placeholder}


### "Project template" placeholders

- **$Title** - Project title
- **$Desc** - Project description, html-formatted
- **$AuthorName** - Author's name
- **$AuthorBio** - Information about the author


- **$FieldTitle1** - Rating names: field 1
- **$FieldTitle2** - Rating names: field 2
- **$FieldTitle3** - Rating names: field 3
- **$FieldTitle4** - Rating names: field 4

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

### "Chapter template" placeholders

- **$ID** - Chapter ID,
- **$ChapterNumber** - Chapter number (in sort order),

- **$Title** - Chapter title
- **$Desc** - Chapter description, html-formatted

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

### "Section template" placeholders

- **$ID** - Section ID,
- **$SectionNumber** - Section number (in sort order),

- **$Title** - Section title
- **$Desc** - Section description, html-formatted

- **$WordCount** - Section word count
- **$WordsTotal** - Accumulated word count including the current section
- **$LetterCount** - Section letter count
- **$LettersTotal** - Accumulated letter count including the current section

- **$Status** - Section status (Outline, Draft etc.)
- **$SectionContent** - Section content, html-formatted

- **$FieldTitle1** - Rating names: field 1
- **$FieldTitle2** - Rating names: field 2
- **$FieldTitle3** - Rating names: field 3
- **$FieldTitle4** - Rating names: field 4
- **$Field1** - Section rating: field 1
- **$Field2** - Section rating: field 2
- **$Field3** - Section rating: field 3
- **$Field4** - Section rating: field 4

- **$Date** - Specific section date (yyyy-mm-dd)
- **$Time** - Time section begins: (hh:mm)
- **$Day** - Day section begins 
- 
- **$ScDate** - Date or day

- **$LastsDays** - Amount of time section lasts: days
- **$LastsHours** - Amount of time section lasts: hours
- **$LastsMinutes** - Amount of time section lasts: minutes

- **Duration** - Combination of days and hours and minutes

- **$ReactionSection** - A(ction) or R(eaction)
- **$Goal** - The section protagonist's goal, html-formatted
- **$Conflict** - The section conflict, html-formatted
- **$Outcome** - The section outcome, html-formatted
- **$Tags** - Comma-separated list of section tags
- **$Image** - Image filename

- **$Characters** - Comma-separated list of characters assigned to the section
- **$Viewpoint** - Viewpoint character
- **$Locations** - Comma-separated list of locations assigned to the section
- **$Items** - Comma-separated list of items assigned to the section

- **$Notes** - Section notes

- **$Language** - Language code acc. to ISO 639-1
- **$Country** - Country code acc. to ISO 3166-2

## Installation path

The setup script installs *novx_xtg.pyw* in the user profile. This is the installation path on Windows: 

`c:\Users\<user name>.novx\novx_xtg`
