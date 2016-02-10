# d2lmf
A command-line tool to help mark assignments submitted to D2L

## Motivation
It's frustrating dealing with the zip files full of assignment submissions
that you get from D2L.

- Merging all of a student's submissions into a single folder is tedious.
- Navigating submissions on the command line sucks, because each directory name
  starts with a long number.
- Extracting all the zip files, tar archives, and 7z archives that students
  submit adds a needless extra step to marking.

I've found this tool useful for eliminating those annoyances, and I hope you
will too.

## How to Use
This is the most common command I use:
```bash
d2lmf extract -xjcm "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01
```

This extracts the submissions from the zip folder into the directory `A1/T01`.
The `-x` specifies that we want to extract any zip, rar, tar, or 7z archives
that students submitted. The `-j` deletes 'junk' like `.DS_Store`. The `-c`
collapses needlessly nested directories. Finally, the `-m` merges all submitted
files into a single directory for each student. Cool!

On Windows, you may need to invoke d2lmf as a Python module, like so:
```bash
python -m d2lmf extract -xjcm "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01
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
have a rar or 7z utility installed, those archives will be skipped.

On Windows, I suggest installing [7-Zip](http://www.7-zip.org/).
On Ubuntu, p7zip is the equivalent, and it can be installed with
`sudo apt-get install p7zip-full`. p7zip is also available for OSX, and can
be installed from [homebrew](http://brew.sh/) with `brew install p7zip`.

## Release Status
This software is in beta. There may be bugs, and the interface may undergo
significant changes between releases.
