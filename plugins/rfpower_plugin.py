from plugins.server_plugin import ServerPlugin
import subprocess, os

SECT_UNITS = "units"
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

    def set_state(self,data):
        # If no units states have been set before, initialize an empty list
        if not SECT_UNITS in self.data:
            self.data[SECT_UNITS] = []
        # Try to find unit state and remove it
        for unit in self.data[SECT_UNITS]:
            if unit[ATTR_BASE][0] == data[ATTR_BASE][0] and unit[ATTR_UNIT][0] == data[ATTR_UNIT][0]:
                # Set unit state
                unit[ATTR_STATE][0] = data[ATTR_STATE][0]
                break

    def set_action(self,data):
        base = data[ATTR_BASE][0]
        unit = data[ATTR_UNIT][0]
        state = data[ATTR_STATE][0]
        print("[%s] base=%s unit=%s state=%s "%(self.name, base, unit, state))
        subprocess.call(["sudo",self.send_path,base,unit,state])
        
    def get_data(self):
        return ( self.data[ATTR_BASE][0], self.data[ATTR_UNIT][0], ("1" if "true" == self.data[ATTR_STATE][0] else "0"))
