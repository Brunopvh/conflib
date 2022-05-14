#!/usr/bin/env python3


import os
import sys

try:
	from setuptools import setup
except Exception as e:
	print(e)
	sys.exit(1)

file_setup = os.path.abspath(os.path.realpath(__file__))
dir_of_project = os.path.dirname(file_setup)
sys.path.insert(0, dir_of_project)

try:
	from conflib.version import (
							__version__,
							__author__,
							__repo__,
							__online_file__,
							)
except Exception as e:
	print(e)
	sys.exit(1)


DESCRIPTION = 'Biblioteca para configuração de diretórios de aplicativos.'
LONG_DESCRIPTION = DESCRIPTION

setup(
	name='conflib',
	version=__version__,
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	author=__author__,
	author_email='brunodasill@gmail.com',
	license='MIT',
	packages=['conflib'],
	zip_safe=False,
	url=__repo__,
	project_urls = {
		'Código fonte': __repo__,
		'Download': __online_file__,
	},
)


