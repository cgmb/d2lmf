# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'd2lmf',
    version = '0.0.3',
    description = 'A command-line tool to help mark assignments submitted to D2L.',
    license='GPLv3+',
    url='https://github.com/cgmb/d2lmf',
    author = 'Cordell Bloor',
    author_email = 'cgbloor@ucalgary.ca',
    packages = ['d2lmf'],
    entry_points = {
        'console_scripts': ['d2lmf = d2lmf.d2lmf:main']
        },
    install_requires = (
        'patool',
    ),
    tests_require = ['nose'],
    test_suite = "nose.collector",
    classifiers=[
         'Development Status :: 4 - Beta',
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
         'Topic :: Education',
    ],
    long_description = """
d2lmf is a command-line tool to help mark assignments submitted to D2L (Desire2Learn).
"""
)
