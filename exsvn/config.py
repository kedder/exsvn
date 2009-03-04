import os
from ConfigParser import ConfigParser

from error import ExsvnError

CONFIG_FILENAME = "exsvn.ini"

class Config(object):

	def __init__(self):
		self.parser = ConfigParser()
		self.read_configuration()

	def read_configuration(self):
		# check if we are in svn working dir
		if not os.path.isdir('.svn'):
			raise ExsvnError("Current directory is not a svn working directory")

		fullcfgname = os.path.join('.svn', CONFIG_FILENAME)
		if not os.path.exists(fullcfgname):
			self.create_configuration(fullcfgname)
		
		self.parser.read(fullcfgname)

	def create_configuration(self, fname):
		"""Create new configuration file"""
		print "Creating default configuration in %s" % fname
		cfg = self.get_default_configuration()

		f = file(fname, "w")
		f.write(cfg)
		f.close()

		# protect from others
		os.chmod(fname, 0600)

	def get_default_configuration(self):
		return """
[main]
; list of regexp patterns of files that should never be commited. entries are separated by spaces
;never_commit=.classpath .project

; editor to use
;editor=vim -f
"""
