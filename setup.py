# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'd2lmf',
    version = '0.0.1',
    description = 'Tools to help mark assignments downloaded from Desire2Learn.',
    license='MIT',
    url='https://github.com/cgmb/d2lmf',
    author = 'Cordell Bloor',
    author_email = 'cgbloor@ucalgary.ca',
    packages = ['d2lmf'],
    entry_points = {
        'console_scripts': ['d2lmf = d2lmf.d2lmf:main']
        },
    install_requires = (
        'pyunpack',
        'patool',
    ),
    tests_require = ['nose'],
    test_suite = "nose.collector",
    classifiers=[
         'Development Status :: 3 - Alpha',
         'Environment :: Console',
         'Intended Audience :: Developers',
         'Intended Audience :: Education',
         'Intended Audience :: End Users/Desktop',
         'Operating System :: POSIX',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python',
         'Topic :: Education',
    ],
    long_description = """
d2lmf is a suite of tools to help mark assignments submitted to D2L.
"""
)
