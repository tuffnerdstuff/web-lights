from os.path import expanduser, join
from os import makedirs

SETTINGS_DIR = ".web-lights"
SETTINGS_FILE = "web-lights.conf"

def save_color(r,g,b):
	settings_path = get_save_path()
	print("Saving to: %s" % settings_path)
	try:
		f = open(settings_path,"w")
		f.write("%i,%i,%i"%(r,g,b))
		f.close()
	except:
		print("[ERROR] Could not save values")
		
def load_color():
	settings_path = get_save_path()
	try:
		f = open(settings_path,"r")
		color = f.read().strip().split(',')
		f.close()
		return (int(color[0]),int(color[1]),int(color[2]))
	except:
		print("[ERROR] Could not load values, falling back to defaults (0,0,0)")
		return (0,0,0)
		
	
def get_save_path():
	root_path = join(expanduser("~"),SETTINGS_DIR)
	try:
		makedirs(root_path)
	except:
		pass
	return join(root_path,SETTINGS_FILE)