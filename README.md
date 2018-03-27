[![Build Status](https://travis-ci.org/marcindulak/python-mycli.svg?branch=master)](https://travis-ci.org/marcindulak/python-mycli)

Example usage of argparse
=========================

A Python program that demonstrates usage of argparse.


Description
-----------

Based on https://docs.python.org/2/howto/argparse.html.
The program accepts command line arguments and runs different functions based
on those arguments.

The program is packaged (more or less) according to the recommendations
from https://packaging.python.org/en/latest/distributing.html
The exception is that distutils are used instead of setuptools.

The code is licensed under the Apache License, Version 2.0,
as recommended for small projects at
https://www.gnu.org/licenses/license-recommendations.html

Note: for older Python versions (Python < 2.7 or < 3.2) get argparse from
https://pypi.python.org/pypi/argparse

Run the unit tests from the project root directory
(only for Python >= 2.7 and >= 3.2)::

    python setup.py test

or, explicitly with:

    python -m unittest discover -s mycli/tests -p '*.py'

For a similar project, making use of several additional libraries see
http://nvie.com/posts/writing-a-cli-in-python-in-under-60-seconds/

Installation
------------

The contrib directory contains the RPM spec file
and the deb directory structure for building on build.opensuse.org.
The binaries are available at download.opensuse.org.

Install the binaries with the software package manager of your Linux
distribution. Only Python2 is packaged.

The currently supported systems include:

- RHEL/CentOS 7::

        su -c "yum -y install wget"
        su -c "wget https://build.opensuse.org/project/repository_state/home:marcindulak/RHEL_7/home:marcindulak.repo -O /etc/yum.repos.d/home:marcindulak.repo"
        su -c "yum -y install python-mycli"

- openSUSE Tumbleweed (as root)::

        zypper ar -f https://download.opensuse.org/repositories/home:/marcindulak/openSUSE_Tumbleweed/home:marcindulak.repo
        yast -i python-mycli

- Debian 9.0::

        sudo bash -c 'echo "deb https://download.opensuse.org/repositories/home:/marcindulak/Debian_9.0 /" > /etc/apt/sources.list.d/home_marcindulak.sources.list'
        wget https://download.opensuse.org/repositories/home:/marcindulak/Debian_9.0/Release.key && sudo apt-key add Release.key && rm Release.key
        sudo apt-get update
        sudo apt-get install python-mycli

- Ubuntu 14.04::

        sudo bash -c 'echo "deb https://download.opensuse.org/repositories/home:/marcindulak/xUbuntu_14.04 /" > /etc/apt/sources.list.d/home_marcindulak.sources.list'
        wget https://download.opensuse.org/repositories/home:/marcindulak/xUbuntu_14.04/Release.key && sudo apt-key add Release.key && rm Release.key
        sudo apt-get update
        sudo apt-get install python-mycli

For the full list of supported distributions check
https://build.opensuse.org/package/show/home:marcindulak/python-mycli

Usage
-----

For help::

    mycli -h
