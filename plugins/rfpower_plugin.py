from plugins.server_plugin import ServerPlugin
import subprocess, os

SECT_UNITS = "units"
ATTR_NAME = "name"
ATTR_BASE = "base"
ATTR_UNIT = "unit"
ATTR_STATE = "state"


class RFPowerPlugin(ServerPlugin):
    
    
    def _on_init_plugin(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.send_path = os.path.join(dir_path,'send')
        self._restore_state()
        self._render_state()


    def do(self,data):
        
        # If no units states have been set before, initialize an empty list
        if not SECT_UNITS in self.state:
            self.state[SECT_UNITS] = []
        
        # Try to find unit state and set it
        changed_unit = None
        for unit in self.state[SECT_UNITS]:

            if unit[ATTR_BASE] == data[ATTR_BASE][0] and unit[ATTR_UNIT] == data[ATTR_UNIT][0]:
                # Set unit state
                unit[ATTR_NAME] = data[ATTR_NAME][0]
                unit[ATTR_STATE] = data[ATTR_STATE][0]
                changed_unit = unit
                break
        
        if not changed_unit:
            changed_unit = {ATTR_NAME:data[ATTR_NAME][0],ATTR_BASE:data[ATTR_BASE][0],ATTR_UNIT:data[ATTR_UNIT][0],ATTR_STATE:data[ATTR_STATE][0]}
            self.state[SECT_UNITS].append(changed_unit)
        
        # Render state
        self.__switch_unit(changed_unit)
        
        # Persist data
        self._save_state()

    def _render_state(self):
        
        for unit in self.state[SECT_UNITS]:
            # switch unit state
            self.__switch_unit(unit);


    def __switch_unit(self,data):
        base = data[ATTR_BASE]
        unit = data[ATTR_UNIT]
        state = "1" if "true" == data[ATTR_STATE] else "0"
        print("[%s] base=%s unit=%s state=%s "%(self.name, base, unit, state))
        try:
            subprocess.call(["sudo",self.send_path,base,unit,state])
            pass
        except Exception:
            print("Could not send RF signal!")
        
