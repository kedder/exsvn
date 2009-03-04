import sys
import readline

from cmd import Cmd

from status import get_status, print_status
import context

from error import ApplicationError

class ExSvn(Cmd):
	def run(self):
		self.ctx = context.create_context()

		intro = """ExSvn command console. Type `help' for list of commands."""
		self.cmdloop(intro)

	def onecmd(self, line):
		try:
			Cmd.onecmd(self, line)
		except ApplicationError, e:
			print "Error occured: %s" % e

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
		status = get_status(self.ctx, ".")
		print_status(status)

	do_st = do_status

def main():
	prog = ExSvn()
	prog.run()

if __name__ == '__main__':
	main()
