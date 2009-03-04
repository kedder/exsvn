import pysvn

from error import ApplicationError

wc_status_kind_map = {
	pysvn.wc_status_kind.added: 'A',
	pysvn.wc_status_kind.conflicted: 'C',
	pysvn.wc_status_kind.deleted: 'D',
	pysvn.wc_status_kind.external: 'X',
	pysvn.wc_status_kind.ignored: 'I',
	pysvn.wc_status_kind.incomplete: '!',
	pysvn.wc_status_kind.missing: '!',
	pysvn.wc_status_kind.merged: 'G',
	pysvn.wc_status_kind.modified: 'M',
	pysvn.wc_status_kind.none: ' ',
	pysvn.wc_status_kind.normal: ' ',
	pysvn.wc_status_kind.obstructed: '~',
	pysvn.wc_status_kind.replaced: 'R',
	pysvn.wc_status_kind.unversioned: '?',
}

def get_status(ctx, dir):
	try:
		full_status = ctx.client.status(dir)
	except pysvn.ClientError, e:
		raise ApplicationError(e)

	ignore = [pysvn.wc_status_kind.none,
           pysvn.wc_status_kind.normal,
           pysvn.wc_status_kind.ignored]
	status = (s for s in full_status if s.text_status not in ignore)
	return status
	

def print_status(status):
	for item in status:
		print "  ",wc_status_kind_map[item.text_status], item.path
