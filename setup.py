#!/usr/bin/env python2.7
from __future__ import absolute_import, division, print_function

INSTALL_REQUIRES = [
    #'PyQt4'  # non pipi index
]

if __name__ == '__main__':
    from utool.util_setup import setuptools_setup
    setuptools_setup(
        name='guitool',
        description=('Guitool - tools pyqt4 guis'),
        url='https://github.com/Erotemic/guitool',
        keywords='',
        package_data={},
        classifiers=[],
        author='Jon Crall',
        install_requires=INSTALL_REQUIRES,
        author_email='erotemic@gmail.com',
        setup_fpath=__file__,
    )
