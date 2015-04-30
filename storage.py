from os import makedirs
from os.path import expanduser, join
import json


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
        
def save(name,data):
    settings_path = get_save_path(name+".conf")
    try:
        f = open(settings_path,"w")
        json.dump(data,f,indent=4,sort_keys=True)
        f.close()
        print("[OK] Stored values for %s in %s" % (name,settings_path))
    except:
        print("[ERROR] Could not store values for %s in %s" % (name,settings_path))
        
def load(name):
    settings_path = get_save_path(name+".conf")
    try:
        f = open(settings_path,"r")
        data = json.load(f)
        f.close()
        return data
    except:
        print("[ERROR] Could not load values for %s" % name)
        return None
        
def get_save_path():
    return get_save_path(SETTINGS_FILE)     
    
def get_save_path(file_name):
    root_path = join(expanduser("~"),SETTINGS_DIR)
    try:
        makedirs(root_path)
    except:
        pass
    return join(root_path,file_name)

if __name__=="__main__":
    save("test",{"a":1,"b":"bla"})
