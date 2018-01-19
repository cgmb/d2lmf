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
d2lmf extract -R "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01
```

It extracts the submissions from the zip folder into the directory `A1/T01`.
The `-R` option makes it run all the recommended cleanup actions on the
submissions, and is equivalent to using `-x`, `-j`, `-c` and `-m`.

The `-x` specifies that we want to extract any zip, rar, tar, or 7z archives
that students submitted. The `-j` deletes 'junk' like `.DS_Store`. The `-c`
collapses needlessly nested directories. Finally, the `-m` merges all submitted
files into a single directory for each student.

If you haven't added your local Python bin directory to your path, you may need
to invoke d2lmf as a module, like so:
```bash
python -m d2lmf extract -R "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01
```

## How to Install
d2lmf is available through [pip](https://docs.python.org/3/installing/index.html).
If you're running a recent version of Python, you probably already have pip
installed. If not, that's the first step in each of the commands below.

### Ubuntu
```bash
sudo apt-get install python-pip
pip install --user d2lmf

# add the local Python bin directory to the path
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.profile
source ~/.profile
```

### OSX
```bash
sudo easy_install pip
pip install --user d2lmf

# add the local Python bin directory to the path
echo 'export PATH="$PATH:$HOME/Library/Python/2.7/bin"' >> ~/.profile
source ~/.profile
```

### Windows
First, download and install Python from https://www.python.org/downloads/

Then, install d2lmf:
```bash
python -m pip install --user d2lmf
```

## Dependencies
The extraction of rar and 7z archives depends on external tools. If you do not
have a rar or 7z utility installed, those archives will be skipped.

On Windows, I suggest installing [7-Zip](http://www.7-zip.org/).
On Ubuntu, p7zip is the equivalent, and it can be installed with
`sudo apt-get install p7zip-full`. p7zip is also available for OSX, and can
be installed from [homebrew](http://brew.sh/) with `brew install p7zip`.
