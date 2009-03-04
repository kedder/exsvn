import pysvn

from config import Config

class Context(object):
	def __init__(self):
		self.config = Config()
		self.client = pysvn.Client()


def create_context():
	return Context()
