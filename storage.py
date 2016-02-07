from os import makedirs
from os.path import expanduser, join
import json


SETTINGS_DIR = ".web-lights"

        
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
        print("[ERROR] Could not load values for %s from %s" % (name,settings_path))
        return None
    
def get_save_path(file_name):
    root_path = join(expanduser("~"),SETTINGS_DIR)
    try:
        makedirs(root_path)
    except:
        pass
    return join(root_path,file_name)

if __name__=="__main__":
    save("test",{"a":1,"b":"bla"})
