from plugins.server_plugin import ServerPlugin
import subprocess, os

ATTR_BASE = "base"
ATTR_UNIT = "unit"
ATTR_STATE = "state"


class RFPowerPlugin(ServerPlugin):

    def __init__(self):
        super(RFPowerPlugin,self).__init__()
        import os
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.send_path = os.path.join(dir_path,'send')

    def set_action(self):
        base,unit,state = self.get_data()
        print("[%s] base=%s unit=%s state=%s "%(self.name, base, unit, state))
        subprocess.call(["sudo",self.send_path,base,unit,state])
        
        
    def get_data(self):
        return ( self.data[ATTR_BASE][0], self.data[ATTR_UNIT][0], ("1" if "true" == self.data[ATTR_STATE][0] else "0"))
