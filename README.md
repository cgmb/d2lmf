# d2lmf
A command-line tool to help mark assignments submitted to D2L

## How to Use
A sample command might be:
```bash
d2lmf extract -xcm "Assignment 1 Download Oct 11, 2015 803 PM.zip" marks/a1/T01
```

This extracts the submissions from the zip folder into the directory
`marks/a1/T01`. The flags x, c and m specify that we want to extract any
zip, rar, tar, or 7z archives that students submitted, collapse needlessly
nested directories, and merge each students submissions (if they made more
than one).

## How to Install
### Ubuntu
```bash
sudo apt-get install python-pip
sudo pip install d2lmf
```

### Other
This software has only been tested with Python 2.7 on Ubuntu 14.04. It is
likely, however, that it works on other platforms. The
[Python docs](https://docs.python.org/2.7/installing/index.html) detail
installing for other platforms.

## Release Status
If you note the version number, it's `0.0.1`.

There may be bugs, and the inferface may undergo significant changes between releases.
