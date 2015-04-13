def switch(base, unit_id, switch):
	if not(base is None or unit_id is None or switch is None):
		print("unit=%i id=%i on=%s" % (base,unit_id,switch))
