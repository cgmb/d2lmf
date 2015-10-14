# -*- coding: utf-8 -*-

"""d2lmf.d2lmf: provides entry point main()."""

from __future__ import print_function
import argparse
import os
import errno
import shutil
import sys

__version__ = "0.0.1"

def makedirs_exist(path):
    """
    Makes a directory at the given path without raising an error if it already exists
    """
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def copytree_exist(src, dst):
    """
    Copies a directory tree at the given path into the destination directory
    without raising an error if the destination already exists
    """
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)

class ParserError(Exception):
    pass

def parse_submission_dirname(dirname):
    """
    Parses a directory name in the form '<id_number> - <student_name> - <timestamp>'
    """
    seperator = ' - '
    tokens = dirname.split(seperator)
    if len(tokens) < 3:
        raise ParserError('Expected hyphen-separated id, name and timestamp'
                ' in "%s"' % dirname)
    id_number = tokens[0]
    # we'll assume the extra hypens are a part of the student's name
    student_name = seperator.join(tokens[1:-1])
    timestamp = tokens[-1]
    return (id_number, student_name, timestamp)

def merge(src, dest):
    """
    Merges the src folder into the dest folder
    """
    vprint('Merging "%s" into "%s"' % (src, dest))
    for src_root, dirs, files in os.walk(src):
        dest_root = src_root.replace(src, dest, 1)
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)
        for f in files:
            src_file = os.path.join(src_root, f)
            dest_file = os.path.join(dest_root, f)
            if os.path.exists(dest_file):
                os.remove(dest_file)
            shutil.move(src_file, dest_root)
    shutil.rmtree(src)

def rename(input_folder):
    """
    Rename all child folders, using their complicated D2L-given name to infer
    the submitter's name. Use the submitter's name to create a short, easy
    name for a folder to move the data to.

    There may be multiple folders created by the same submitter, as they make
    one for each submission. We'll merge those together, overwriting files
    from the oldest with files from the newest whenever there's a conflict.
    """
    from operator import itemgetter
    from datetime import datetime
    submissions = []
    for name in os.listdir(input_folder):
        if os.path.isdir(os.path.join(input_folder, name)):
            try:
                id_num, student, timestamp = parse_submission_dirname(name)
                parsed_timestamp = datetime.strptime(timestamp,
                        '%b %d, %Y %I:%M %p') # Sep 29, 2015 4:17 PM
                shortname = student.replace(' ', '')
                submissions.append((name, shortname, parsed_timestamp))
            except (ParserError,ValueError) as e:
                print(e, file=sys.stderr)
    # sort by student name, then by date
    submissions.sort(key=itemgetter(1,2))
    for dirname, student_name, timestamp in submissions:
        try:
            oldpath = os.path.join(input_folder, dirname)
            newpath = os.path.join(input_folder, student_name)
            if os.path.exists(newpath):
                merge(oldpath, newpath)
            else:
                os.rename(oldpath, newpath)
        except OSError as e:
            print(e, file=sys.stderr)
            print('Failed to merge "%s"' % oldpath, file=sys.stderr)

def extract_nested(folder):
    """
    Unzip, untar, unrar, or whatever any file found in the student submission.
    """
    from pyunpack import Archive, PatoolError
    from zipfile  import BadZipfile, LargeZipFile
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(('.zip', '.rar', '.tar.gz', '.tgz', '.tar.bz2',
                           '.tar.xz', '.7z', '.tar')):
                try:
                    archive = os.path.join(root, f)
                    vprint('Extracting archive: "%s"' % archive)
                    Archive(archive).extractall(root)
                    os.remove(archive)
                except (PatoolError,BadZipfile,LargeZipFile,OSError) as e:
                    print(e, file=sys.stderr)
                    print('Failed to extract "%s"' % archive, file=sys.stderr)

def collapse_empty(folder):
    """
    Collapse empty folders into their parents
    """
    for submission in os.listdir(folder):
        submission_path = os.path.join(folder, submission)
        if os.path.isdir(submission_path):
            submitted_files = os.listdir(submission_path)
            if len(submitted_files) == 1:
                submitted_file_path = os.path.join(submission_path, submitted_files[0])
                if os.path.isdir(submitted_file_path):
                    vprint('Collapsing directory into parent: "%s"' % submitted_file_path)
                    for f in os.listdir(submitted_file_path):
                        f_path = os.path.join(submitted_file_path, f)
                        shutil.move(f_path, submission_path)

def clean_junk(folder):
    """
    Deletes useless files from the given directory tree
    """
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f in ['.DS_Store']:
                try:
                    junk = os.path.join(root, f)
                    vprint('Removing: "%s"' % junk)
                    os.remove(junk)
                except OSError as e:
                    print(e, file=sys.stderr)
                    print('Failed to remove "%s"' % junk, file=sys.stderr)
        for d in dirs:
            if d in ['__MACOSX']:
                try:
                    junk = os.path.join(root, d)
                    vprint('Removing: "%s"' % junk)
                    shutil.rmtree(junk)
                except (shutil.Error,OSError) as e:
                    print(e, file=sys.stderr)
                    print('Failed to remove "%s"' % junk, file=sys.stderr)

def extract(args):
    import zipfile
    if os.path.isdir(args.input_file):
        copytree_exist(args.input_file, args.output_folder)
    else:
        makedirs_exist(args.output_folder)
        with zipfile.ZipFile(args.input_file, 'r') as z:
            z.extractall(args.output_folder)
    if args.extract_nested:
        extract_nested(args.output_folder)
    if args.junk:
        clean_junk(args.output_folder)
    if args.collapse:
        collapse_empty(args.output_folder)
    if args.merge:
        rename(args.output_folder)

def setup_vprint(args):
    """
    Defines the function vprint, which only prints when --verbose is set
    """
    global vprint
    vprint = print if args.verbose else lambda *a, **k: None

def main():
    parser = argparse.ArgumentParser(prog='d2lmf',
            description='d2lmf is a suite of tools to help mark assignments '
            'submitted to D2L.')
    parser.add_argument('-v','--verbose',
            action='store_true',
            help='Display more information about files being changed.')
    parser.add_argument('--version', action='version',
            version='%(prog)s ' + __version__)
    subparsers = parser.add_subparsers(help='')

    extract_parser = subparsers.add_parser('extract',
            help='Extract student submissions from the D2L zip file and '
            'optionally process them to be easier to work with.')
    extract_parser.add_argument('input_file',
            help='The zip file or unzipped directory to extract data from.')
    extract_parser.add_argument('output_folder',
            help='The folder in which to put extracted data.')
    extract_parser.add_argument('-x','--extract-nested',
            action='store_true',
            help='Uses command-line tools to attempt to extract submitted '
            'archive files, like zip files, tar files, rar files and 7zip '
            'files.')
    extract_parser.add_argument('-c','--collapse',
            action='store_true',
            help='Collapse pointless subdirectories whose parent directory '
            'contains nothing else.')
    extract_parser.add_argument('-m','--merge',
            action='store_true',
            help="Merge all of a student's submissions into a single folder.")
    extract_parser.add_argument('-j','--junk',
            action='store_true',
            help='Clean up any unneccessary files and folders in the'
            "submission, like '.DS_Store'.")
    extract_parser.set_defaults(func=extract)

    args = parser.parse_args()
    setup_vprint(args)
    args.func(args)
