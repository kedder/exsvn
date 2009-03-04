import os
from StringIO import StringIO
from tempfile import mktemp
import pysvn

from status import get_status, format_icon
from error import ApplicationError

SEPARATOR_BEGIN = "----- BEGIN %s -----"
SEPARATOR_END = "----- END %s -----"

EDITOR = "vim"

def gen_commit_message(dir):
    """ Generate commit message prompt text
    """
    status = get_status(dir)

    if not status:
        raise ApplicationError("No files to commit")

    out = StringIO()
    print >> out
    print >> out
    print >> out
    print >> out, SEPARATOR_END % "MESSAGE"

    section = "FILES"
    print >> out, SEPARATOR_BEGIN % section
    print >> out

    for item in status:
        line = _format_status_item(item)
        print >> out, line

    print >> out
    print >> out, SEPARATOR_END % section

    return out.getvalue()

def _format_status_item(item):
    check = " "
    if item.text_status in [pysvn.wc_status_kind.modified,
                            pysvn.wc_status_kind.added]:
        check = "x"

    line = "[%s] %s   %s" % (check, format_icon(item), item.path)
    return line

def prompt_commit(message):
    """ Present user with commit prompt
    
    Return edited message
    """
    tmpfile = mktemp(prefix="commit", suffix=".exsvn")
    f = file(tmpfile, "w")
    f.write(message)
    f.close()

    cmd = "%s %s" % (EDITOR, tmpfile)
    os.system(cmd)
    
    f = file(tmpfile)
    edited = f.read()
    f.close()
    return edited
