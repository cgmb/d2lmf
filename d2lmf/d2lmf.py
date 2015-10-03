# -*- coding: utf-8 -*-

"""d2lmf.d2lmf: provides entry point main()."""

from __future__ import print_function
import argparse
import os
import errno

__version__ = "0.0.1"

def makedirs_exist(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def extract(args):
    import zipfile
    makedirs_exist(args.output_folder)
    with zipfile.ZipFile(args.input_file, 'r') as z:
        z.extractall(args.output_folder)

def main():
    parser = argparse.ArgumentParser(prog='d2lmf',
            description='d2lmf is a suite of tools to help mark assignments '
            'submitted to D2L.')
    subparsers = parser.add_subparsers(help='')

    extract_parser = subparsers.add_parser('extract', help='')
    extract_parser.add_argument('input_file',
            help='The zip file to extract data from.')
    extract_parser.add_argument('output_folder',
            help='The folder in which to put extracted data.')
    extract_parser.set_defaults(func=extract)

    args = parser.parse_args()
    args.func(args)
