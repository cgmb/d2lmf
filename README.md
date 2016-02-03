# d2lmf
A command-line tool to help mark assignments submitted to D2L

## How to Use
A sample command might be:
```bash
d2lmf extract -xjcm "Assignment 1 Download Oct 11, 2015 803 PM.zip" mark/a1/T01
```

This extracts the submissions from the zip folder into the directory
`mark/a1/T01`. The flags x, j, c and m specify that we want to extract any
zip, rar, tar, or 7z archives that students submitted, delete 'junk' like
`.DS_Store`, collapse needlessly nested directories, and merge all submitted
files into a directory for each student.

On Windows, you may need to invoke d2lmf through Python, like so:
```bash
python -m d2lmf extract -xjcm "Assignment 1 Download Oct 11, 2015 803 PM.zip" mark/a1/T01
```

## How to Install
### Ubuntu
```bash
sudo apt-get install python-pip
sudo pip install d2lmf
```

### OSX
```bash
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
sudo python get-pip.py
sudo pip install d2lmf
```

### Windows
First, download and install Python 2.7 from https://www.python.org/downloads/

Then, install d2lmf with the command below:
```bash
python -m pip install d2lmf
```

## Dependencies
The extraction of rar and 7z archives depends on external tools. If you do not
have those tools installed, those archives will be skipped.

On Windows, only zip files may be extracted.

## Release Status
Note the version number: `0.0.4`. There may be bugs, and the interface may
undergo significant changes between releases.
