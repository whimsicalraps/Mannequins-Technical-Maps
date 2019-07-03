# Mannequins Technical Maps

Technical Maps for Whimsical Raps' Mannequins Eurorack Modules

Feel free to grab printable PDFs for your desired modules, or clone the repository and make your own customizations to the manuals using Markdown or LaTeX!  Hyperlinked, mobile friendly versions of the manuals are also linked below!

*MANGROVE*: [PDF](./mangrove/mangrove.pdf) & [Hyperlinked Web Document](./mangrove/mangrove.md)

*JUST FRIENDS*: [PDF](./just-friends/just-friends.pdf) & [Hyperlinked Web Document](./just-friends/just-friends.md)

*COLD MAC*: [PDF](./cold-mac/cold-mac.pdf) & [Hyperlinked Web Document](./cold-mac/cold-mac-web.md)

## Customizing Your Manual

### Requirements

- [Pandoc](https://pandoc.org/) will render the manual markdown files to PDFs.
- A LaTeX installation (suggestions: [MikTex](http://miktex.org/) for Windows, [BasicTex](http://www.tug.org/mactex/morepackages.html) for MacOS, [TeXLive](http://www.tug.org/texlive/) for Linux) is necessary for Pandoc to render PDFs.
- [Python](https://www.python.org) and [Panflute](http://scorreia.com/software/panflute/) are necessary to accurately create pagebreaks in the PDF.

### Installation

#### Windows & Mac

1. Download the latest Pandoc installer [here](https://pandoc.org/installing.html).
1. Run the Pandoc installer.
1. Donwload the latest MikTeX installer [here](https://miktex.org/download).
1. Run the MikTex installer.
1. Download the latest Python installer [here](https://www.python.org/downloads/).
1. Run the Python installer.
1. Open a command line prompt and run `pip install panflute`.

#### Linux

1. Run `sudo apt-get install pandoc`.
1. Run `sudo apt-get install texlive`.
1. Run `sudo apt-get install python3.6`.
1. Run `pip install panflute`.

### Steps

1. Clone this repository using `git clone` or download this repository as a .zip and unpack it.
2. Navigate to the directory of the module you wish to edit.
3. Make your own personal changes to `<module-name>.md` to include your customizations!  Sticking with [Markdown](https://www.markdownguide.org/basic-syntax/) formatting is easiest, but Pandoc supports many other formatting methods!
4. Run `pandoc <module-name>.md --metadata-file=metadata.md --filter myfilter.py -o <module-name>.pdf` to generate of your new manual!

*NB: Font, paper size, and line spacing settings can be edited in `metadata.md`.*

*NB: Pagebreaks will automatically be created on any level 1 or 2 heading (`#` or `##`).  You can also use `\newpage` or `<div></div>` to insert pagebreaks at any other location.*

