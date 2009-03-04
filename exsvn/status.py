import pysvn

from error import ApplicationError

def get_status(ctx, dir):
	try:
		full_status = ctx.client.status(dir)
	except pysvn.ClientError, e:
		raise ApplicationError(e)

	ignore = [pysvn.wc_status_kind.none, pysvn.wc_status_kind.normal]
	status = (s for s in status if s.text_status not in ignore)
	return status
	

def print_status(status):
	for item in status:
		print item
