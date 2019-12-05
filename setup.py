#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
from os.path import dirname
from os.path import join
from os.path import sys
from os.path import exists


def parse_version(fpath):
    """
    Statically parse the version number from a python file
    """
    import ast
    if not exists(fpath):
        try2 = join(dirname(__file__), fpath)
        if exists(try2):
            fpath = try2
        else:
            raise ValueError('fpath={!r} does not exist'.format(fpath))
    with open(fpath, 'r') as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)
    class VersionVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if getattr(target, 'id', None) == '__version__':
                    self.version = node.value.s
    visitor = VersionVisitor()
    visitor.visit(pt)
    return visitor.version


def native_mb_python_tag():
    import sys
    import platform
    major = sys.version_info[0]
    minor = sys.version_info[1]
    ver = '{}{}'.format(major, minor)
    if platform.python_implementation() == 'CPython':
        # TODO: get if cp27m or cp27mu
        impl = 'cp'
        if ver == '27':
            IS_27_BUILT_WITH_UNICODE = True  # how to determine this?
            if IS_27_BUILT_WITH_UNICODE:
                abi = 'mu'
            else:
                abi = 'm'
        else:
            abi = 'm'
    else:
        raise NotImplementedError(impl)
    mb_tag = '{impl}{ver}-{impl}{ver}{abi}'.format(**locals())
    return mb_tag


def parse_description():
    """
    Parse the description in the README file

    CommandLine:
        pandoc --from=markdown --to=rst --output=README.rst README.md
        python -c "import setup; print(setup.parse_description())"
    """
    from os.path import dirname, join, exists
    readme_fpath = join(dirname(__file__), 'README.rst')
    # This breaks on pip install, so check that it exists.
    if exists(readme_fpath):
        with open(readme_fpath, 'r') as f:
            text = f.read()
        return text
    return ''


def parse_requirements(fname='requirements.txt', with_version=False):
    """
    Parse the package dependencies listed in a requirements file but strips
    specific versioning information.

    Args:
        fname (str): path to requirements file
        with_version (bool, default=False): if true include version specs

    Returns:
        List[str]: list of requirements items

    CommandLine:
        python -c "import setup; print(setup.parse_requirements())"
        python -c "import setup; print(chr(10).join(setup.parse_requirements(with_version=True)))"
    """
    from os.path import exists
    import re
    require_fpath = fname

    def parse_line(line):
        """
        Parse information from a line in a requirements text file
        """
        if line.startswith('-r '):
            # Allow specifying requirements in other files
            target = line.split(' ')[1]
            for info in parse_require_file(target):
                yield info
        else:
            info = {'line': line}
            if line.startswith('-e '):
                info['package'] = line.split('#egg=')[1]
            else:
                # Remove versioning from the package
                pat = '(' + '|'.join(['>=', '==', '>']) + ')'
                parts = re.split(pat, line, maxsplit=1)
                parts = [p.strip() for p in parts]

                info['package'] = parts[0]
                if len(parts) > 1:
                    op, rest = parts[1:]
                    if ';' in rest:
                        # Handle platform specific dependencies
                        # http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-platform-specific-dependencies
                        version, platform_deps = map(str.strip, rest.split(';'))
                        info['platform_deps'] = platform_deps
                    else:
                        version = rest  # NOQA
                    info['version'] = (op, version)
            yield info

    def parse_require_file(fpath):
        with open(fpath, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    for info in parse_line(line):
                        yield info

    def gen_packages_items():
        if exists(require_fpath):
            for info in parse_require_file(require_fpath):
                parts = [info['package']]
                if with_version and 'version' in info:
                    parts.extend(info['version'])
                if not sys.version.startswith('3.4'):
                    # apparently package_deps are broken in 3.4
                    platform_deps = info.get('platform_deps')
                    if platform_deps is not None:
                        parts.append(';' + platform_deps)
                item = ''.join(parts)
                yield item

    packages = list(gen_packages_items())
    return packages


INSTALL_REQUIRES = [
    #'PyQt 4/5'  # non pipi index
    'cachetools>=2.0.1',
]

NAME = 'guitool_ibeis'
MB_PYTHON_TAG = native_mb_python_tag()  # NOQA
VERSION = parse_version('guitool_ibeis/__init__.py')

# try:
#     from Cython.Distutils import build_ext
#     cmdclass = {'build_ext': build_ext}
# except Exception as ex:
#     print(ex)
#     print('WARNING: Cython is not installed. This is only a problem if you are building C extensions')
#     cmdclass = {}


try:
    class EmptyListWithLength(list):
        def __len__(self):
            return 1
except Exception:
    raise RuntimeError('FAILED TO ADD BUILD CONSTRUCTS')

if __name__ == '__main__':
    KWARGS = dict(
        name='guitool_ibeis',
        description=('Guitool - tools pyqt4 guis'),
        author='Jon Crall',
        long_description=parse_description(),
        long_description_content_type='text/x-rst',
        author_email='erotemic@gmail.com',
        packages=['guitool_ibeis', 'guitool_ibeis.__PYQT__'],
        url='https://github.com/Erotemic/guitool',
        # ext_modules=ext_modules,
        version=VERSION,
        # cmdclass=cmdclass,
        # keywords='',
        # package_data={},
        # classifiers=[],
        #language='c',
        install_requires=parse_requirements('requirements/runtime.txt'),
        extras_require={
            'all': parse_requirements('requirements.txt'),
            'tests': parse_requirements('requirements/tests.txt'),
            'build': parse_requirements('requirements/build.txt'),
            'runtime': parse_requirements('requirements/runtime.txt'),
        },
        license='Apache 2',
        # List of classifiers available at:
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: Apache Software License',  # Interpret as Apache License v2.0
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
        ],
    )
    import sysconfig
    import os
    try:
        soconfig = sysconfig.get_config_var('EXT_SUFFIX')
    except Exception:
        soconfig = sysconfig.get_config_var('SO')

    def get_lib_ext():
        if sys.platform.startswith('win32'):
            ext = '.dll'
        elif sys.platform.startswith('darwin'):
            ext = '.dylib'
        elif sys.platform.startswith('linux'):
            ext = '.so'
        else:
            raise Exception('Unknown operating system: %s' % sys.platform)
        return ext

    libext = get_lib_ext()
    _pyver = '{}.{}'.format(sys.version_info.major, sys.version_info.minor)
    hack_libconfig = '-{}{}'.format(_pyver, libext)

    PACKAGE_DATA = (
            ['*%s' % soconfig] +
            ['*%s' % hack_libconfig] +
            ['*%s' % libext] +
            (['*.dll'] if os.name == 'nt' else []) +
            (['Release\\*.dll'] if os.name == 'nt' else [])
            # ["LICENSE.txt", "LICENSE-3RD-PARTY.txt", "LICENSE.SIFT"]
    )
    if '--universal' in sys.argv:
        from setuptools import setup
    else:
        from skbuild import setup
        KWARGS.update(dict(
            ext_modules=EmptyListWithLength(),  # hack for including ctypes bins
            include_package_data=True,
            package_data={
                KWARGS['name']: PACKAGE_DATA,
            },
        ))
    setup(**KWARGS)
