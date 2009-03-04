import sys
from setuptools import setup, find_packages

import exsvn

dependencies = []

if sys.platform == 'win32':
	dependencies.append("pyreadline>=1.6")

setup(
    name = "exsvn",
    version = exsvn.__version__,
	author = "Andrey Lebedev",
	author_email = "andrey.lebedev@gmail.com",
	description = "Extended subversion tools",
	license = "GPLv3",

    packages = find_packages(),

	install_requires = dependencies,

	entry_points = {
		'console_scripts': [
			'exsvn = exsvn.main:main'
		]
	}
)

