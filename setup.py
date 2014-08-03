#!/usr/bin/env python2.7
from __future__ import absolute_import, division, print_function
from setuptools import setup
from Cython.Distutils import build_ext
import utool
"""
python setup.py build_ext --inplace
python setup.py develop
"""

ext_modules = utool.find_ext_modules(disable_warnings=True)

#import os
#os.environ['CC'] = 'g++'
#os.environ['CXX'] = 'g++'

INSTALL_REQUIRES = [
    #'PyQt 4/5'  # non pipi index
]

if __name__ == '__main__':
    #import pyximport; pyximport.install(reload_support=True, setup_args={'script_args':["--compiler=mingw32"]})
    from utool.util_setup import setuptools_setup
    #import pyximport; pyximport.install()  # NOQA

    kwargs = setuptools_setup(
        name='guitool',
        description=('Guitool - tools pyqt4 guis'),
        url='https://github.com/Erotemic/guitool',
        ext_modules=ext_modules,
        cmdclass={'build_ext': build_ext},
        keywords='',
        package_data={},
        classifiers=[],
        #language='c',
        author='Jon Crall',
        install_requires=INSTALL_REQUIRES,
        author_email='erotemic@gmail.com',
        setup_fpath=__file__,
    )
    setup(**kwargs)
