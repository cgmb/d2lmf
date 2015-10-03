# -*- coding: utf-8 -*-

"""d2lmf.d2lmf: provides entry point main()."""
from __future__ import print_function
import argparse
from sh import mkdir, unzip

__version__ = "0.0.1"

def extract(args):
    mkdir(args.output_folder)
    unzip(args.input_file, '-d', args.output_folder)

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
