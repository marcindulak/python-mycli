#!/usr/bin/env python

import os
import sys

from distutils.core import setup
from distutils.cmd import Command

name = "mycli"

rootdir = os.path.abspath(os.path.dirname(__file__))

# Restructured text project description read from file
long_description = open(os.path.join(rootdir, 'README.md')).read()

# Python 2.4 or later needed
if sys.version_info < (2, 4, 0, 'final', 0):
    raise SystemExit('Python 2.4 or later is required!')

# Build a list of all project modules
packages = []
for dirname, dirnames, filenames in os.walk(name):
        if '__init__.py' in filenames:
            packages.append(dirname.replace('/', '.'))

package_dir = {name: name}

# Data files used e.g. in tests
package_data = {name: [os.path.join(name, 'tests', 'prt.txt')]}

# The current version number - MSI accepts only version X.X.X
exec(open(os.path.join(name, 'version.py')).read())

# Scripts
scripts = []
for dirname, dirnames, filenames in os.walk('scripts'):
    for filename in filenames:
        if not filename.endswith('.bat'):
            scripts.append(os.path.join(dirname, filename))

# Provide bat executables in the tarball (always for Win)
if 'sdist' in sys.argv or os.name in ['ce', 'nt']:
    for s in scripts[:]:
        scripts.append(s + '.bat')

# Data_files (e.g. doc) needs (directory, files-in-this-directory) tuples
data_files = []
for dirname, dirnames, filenames in os.walk('doc'):
        fileslist = []
        for filename in filenames:
            fullname = os.path.join(dirname, filename)
            fileslist.append(fullname)
        data_files.append(('share/' + name + '/' + dirname, fileslist))

# python setup.py test with distutils
# https://justin.abrah.ms/python/setuppy_distutils_testing.html
class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        if sys.version_info < (2, 7, 0, 'final', 0):
            raise SystemExit(subprocess.call(['unit2', 'discover', '-s', name + '/tests', '-p',  '*.py']))
        else:
            raise SystemExit(subprocess.call([sys.executable, '-m', 'unittest', 'discover', '-s', name + '/tests', '-p',  '*.py']))

setup(name='python-' + name,
      version=version,  # PEP440
      description='mycli - shows some argparse features',
      long_description=long_description,
      url='https://github.com/marcindulak/python-mycli',
      author='Marcin Dulak',
      author_email='Marcin.Dulak@gmail.com',
      license='ASL',
      cmdclass={'test': TestCommand},
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.4',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      data_files=data_files,
      keywords='argparse distutils cli unittest RPM spec deb',
      packages=packages,
      package_dir=package_dir,
      package_data=package_data,
      scripts=scripts,
      )
