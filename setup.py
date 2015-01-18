#!/usr/bin/env python
from distutils.core import setup, Command

from pyguard import VERSION

# you can also import from setuptools

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


with open('README.rst', 'rb') as fin:
    README = fin.read()

PACKAGE_NAME = 'pyguard'

requires = [
    'filewatch==0.1.5',
]

tests_require = [
    'pytest',
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      cmdclass = {'test': PyTest},
      description='Python auto test runner',
      package_data={PACKAGE_NAME: ['{}.ini'.format(PACKAGE_NAME), ], },
      long_description=README,
      author='Ben Emery',
      url='https://github.com/benemery/%s' % PACKAGE_NAME,
      download_url='https://github.com/benemery/%s/tarball/%s' % (VERSION, PACKAGE_NAME),
      packages=[PACKAGE_NAME, ],
      install_requires=requires,
      extras_require={
        'tests': tests_require,
    },
)