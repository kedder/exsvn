import pysvn

class Context(object):
	def __init__(self):
		self.client = pysvn.Client()


def create_context():
	return Context()
