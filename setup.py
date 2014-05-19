#!/usr/bin/env python
from __future__ import absolute_import, division, print_function

if __name__ == '__main__':
    from utool.util_setup import setuptools_setup
    import guitool
    setuptools_setup(
        module=guitool,
        description=('Guitool - tools pyqt4 guis'),
        url='https://github.com/Erotemic/guitool',
        keywords='',
        package_data={},
        classifiers=[],
        author='Jon Crall',
        author_email='erotemic@gmail.com',
        setup_fpath=__file__,
    )
