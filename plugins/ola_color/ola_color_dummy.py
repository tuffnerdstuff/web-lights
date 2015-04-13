import storage


def SendDMXFrame(r,g,b):
	print ("R:%i G:%i B:%i" % (r,g,b))
	storage.save_color(r,g,b)
	
def get_color():
	return storage.load_color()
