from plugins.server_plugin import ServerPlugin
import subprocess, os

SECT_UNITS = "units"
ATTR_BASE = "base"
ATTR_UNIT = "unit"
ATTR_STATE = "state"


class RFPowerPlugin(ServerPlugin):

    def __init__(self):
        super(RFPowerPlugin,self).__init__()
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.send_path = os.path.join(dir_path,'send')

    def set_state(self,data):
        
        # TODO: this is bad, change plugin workflow
        # We set data for all units (e.g. persistence)
        if SECT_UNITS in data:
            self.data = data
        
        # We set data for one unit
        else:
            
            # If no units states have been set before, initialize an empty list
            if not SECT_UNITS in self.data:
                self.data[SECT_UNITS] = []
            
            # Try to find unit state and set it
            for unit in self.data[SECT_UNITS]:
                if unit[ATTR_BASE][0] == data[ATTR_BASE][0] and unit[ATTR_UNIT][0] == data[ATTR_UNIT][0]:
                    # Set unit state
                    unit[ATTR_STATE][0] = data[ATTR_STATE][0]
                    break
        
        import pdb; pdb.set_trace()

    def set_action(self,data):
        
        # TODO: set_action should always operate on self.data. Change Interface
        
        for unit in self.data[SECT_UNITS]:
            # switch unit state
            self.switch_unit(unit);


    def switch_unit(self,data):
        base = data[ATTR_BASE][0]
        unit = data[ATTR_UNIT][0]
        state = "1" if "true" == data[ATTR_STATE][0] else "0"
        print("[%s] base=%s unit=%s state=%s "%(self.name, base, unit, state))
        #subprocess.call(["sudo",self.send_path,base,unit,state])
        
