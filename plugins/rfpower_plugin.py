from plugins.server_plugin import ServerPlugin

ATTR_BASE = "base"
ATTR_UNIT = "unit"
ATTR_STATE = "state"


class RFPowerPlugin(ServerPlugin):

    def __init__(self):
        super(RFPowerPlugin,self).__init__()

    def set_action(self):
        base,unit,state = self.get_data()
        print("[%s] base=%i unit=%i state=%s "%(self.name, base, unit, state))
        
    def get_data(self):
        return ( int(self.data[ATTR_BASE][0]), int(self.data[ATTR_UNIT][0]), "true" == self.data[ATTR_STATE][0] )
