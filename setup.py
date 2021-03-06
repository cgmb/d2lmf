# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'd2lmf',
    version = '1.0.0',
    description = 'A command-line tool to help mark assignments submitted to D2L.',
    license = 'GPLv3+',
    url = 'https://github.com/cgmb/d2lmf',
    author = 'Cordell Bloor',
    author_email = 'cgbloor@ucalgary.ca',
    packages = ['d2lmf'],
    entry_points = {
        'console_scripts': ['d2lmf = d2lmf.d2lmf:main']
    },
    install_requires = (
        'patool>=1.9',
    ),
    tests_require = ['nose'],
    test_suite = "nose.collector",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Education',
    ],
    long_description = """
Motivation
----------

It's frustrating dealing with the zip files full of assignment
submissions that you get from D2L.

-  Merging all of a student's submissions into a single folder is
   tedious.
-  Navigating submissions on the command line sucks, because each
   directory name starts with a long number.
-  Extracting all the zip files, tar archives, and 7z archives that
   students submit adds a needless extra step to marking.

I've found this tool useful for eliminating those annoyances, and I hope
you will too.

How to Use
----------

This is the most common command I use:

.. code:: bash

    d2lmf extract -R "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01

It extracts the submissions from the zip folder into the directory
``A1/T01``. The ``-R`` option makes it run all the recommended cleanup
actions on the submissions, and is equivalent to using ``-x``, ``-j``,
``-c`` and ``-m``.

The ``-x`` specifies that we want to extract any zip, rar, tar, or 7z
archives that students submitted. The ``-j`` deletes 'junk' like
``.DS_Store``. The ``-c`` collapses needlessly nested directories.
Finally, the ``-m`` merges all submitted files into a single directory
for each student.

On Windows, you may need to invoke d2lmf as a Python module, like so:

.. code:: bash

    python -m d2lmf extract -R "Assignment 1 Download Oct 11, 2015 803 PM.zip" A1/T01

How to Install
--------------

Ubuntu
~~~~~~

.. code:: bash

    sudo apt-get install python-pip
    sudo pip install d2lmf

OSX
~~~

.. code:: bash

    curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
    sudo python get-pip.py
    sudo pip install d2lmf

Windows
~~~~~~~

First, download and install Python from
https://www.python.org/downloads/

Then, install d2lmf with the command below:

.. code:: bash

    python -m pip install d2lmf

Dependencies
------------

The extraction of rar and 7z archives depends on external tools. If you
do not have a rar or 7z utility installed, those archives will be
skipped.

On Windows, I suggest installing `7-Zip <http://www.7-zip.org/>`__. On
Ubuntu, p7zip is the equivalent, and it can be installed with
``sudo apt-get install p7zip-full``. p7zip is also available for OSX,
and can be installed from `homebrew <http://brew.sh/>`__ with
``brew install p7zip``.
"""
)
