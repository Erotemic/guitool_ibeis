#!/usr/bin/env python2.7
from __future__ import absolute_import, division, print_function
from setuptools import setup
import utool

INSTALL_REQUIRES = [
    #'PyQt4'  # non pipi index
]
CYTHON_FILES = utool.glob('*_cython.pyx')

if __name__ == '__main__':
    #import pyximport; pyximport.install(reload_support=True, setup_args={'script_args':["--compiler=mingw32"]})
    from utool.util_setup import setuptools_setup

    import pyximport; pyximport.install()  # NOQA

    kwargs = setuptools_setup(
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
    setup(**kwargs)
