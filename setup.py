#!/usr/bin/env python2.7
from __future__ import absolute_import, division, print_function
from setuptools import setup
from utool import util_setup
"""
python setup.py build_ext --inplace
python setup.py develop
"""

ext_modules = util_setup.find_ext_modules(disable_warnings=True)

#import os
#os.environ['CC'] = 'g++'
#os.environ['CXX'] = 'g++'

INSTALL_REQUIRES = [
    #'PyQt 4/5'  # non pipi index
]

if __name__ == '__main__':

    kwargs = util_setup.setuptools_setup(
        name='guitool',
        packages=['guitool', 'guitool.__PYQT__'],
        description=('Guitool - tools pyqt4 guis'),
        url='https://github.com/Erotemic/guitool',
        ext_modules=ext_modules,
        cmdclass=util_setup.get_cmdclass(),
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


#import pyximport; pyximport.install(reload_support=True, setup_args={'script_args':["--compiler=mingw32"]})
#from utool.util_setup import setuptools_setup
#import pyximport; pyximport.install()  # NOQA
