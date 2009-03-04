import sys
import readline

from cmd import Cmd

class ExSvn(Cmd):
	def run(self):
		intro = """ExSvn command console. Type `help' for list of commands."""
		self.cmdloop(intro)

	def exit(self):
		print "Good bye."
		exit(0)
	
	## Command implementation
	def do_EOF(self, arg):
		self.exit()

	def do_quit(self, arg):
		self.exit()

	def do_status(self, arg):
		"""Show current working directory status"""



if __name__ == '__main__':
	prog = ExSvn()
	prog.run()
