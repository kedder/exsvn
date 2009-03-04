import pysvn

from config import Config

class Context(object):
	def __init__(self):
		self.config = Config()
		self.client = pysvn.Client()


__context = None

def create_context():
	return Context()

def init_context():
    global __context
    __context = create_context()
    return __context

def get_context():
    if __context is None:
        raise ExsvnError("Context is not initialized")
    return __context
    
