import sys
import readline

from cmd import Cmd

from exsvn.status import get_status, print_status
from exsvn.commit import gen_commit_message, prompt_commit
from exsvn import context

from error import ApplicationError

class ExSvn(Cmd):
    def run(self):
        context.init_context()

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
        status = get_status(".")
        print_status(status)

    do_st = do_status

    def do_commit(self, arg):
        """Commit changes to central repository
        """
        msg = gen_commit_message(".")
        edited = prompt_commit(msg)
        print edited

    do_ci = do_commit
        

def main():
    prog = ExSvn()
    prog.run()

if __name__ == '__main__':
    main()
