import array
dummy_mode = False
try:
    from ola.ClientWrapper import ClientWrapper
except ImportError:
    dummy_mode = True
    
from plugins.server_plugin import ServerPlugin

UNIVERSE = 1
SEGMENTS = 8
COLORS = 3
MAX_CHANNELS = 512

ATTR_RED = 'r'
ATTR_GREEN = 'g'
ATTR_BLUE = 'b'

class OlaPlugin(ServerPlugin):

    ## PLUGIN METHODS ##

    def _on_init_plugin(self):
        
        # instance variables
        self.wrapper = None
        
        # restore state
        self._restore_state()
        
        # render state
        self._render_state()
        
    def do(self,data):
        
        # save state
        self.state = data
        
        # render state
        self._render_state()
        
        # persist state
        self._save_state()
        
    def _render_state(self):
        
        # load state
        r,g,b = self.get_color(self.state)

        # send color to DMX
        self.send_color(r,g,b)
        
        
    ## OLA METHODS ##

    def stop_wrapper(self,state):
        self.wrapper.Stop()

    def get_color(self,data):
        return ( int(data[ATTR_RED][0]), int(data[ATTR_GREEN][0]), int(data[ATTR_BLUE][0]) )

    def send_color(self,r,g,b):
        if not dummy_mode:
            self.wrapper = ClientWrapper()

        # Fill RGB bar array
        data = array.array('B')
        for i in range(0,SEGMENTS):
            data.append(r)
            data.append(g)
            data.append(b)

        # Fill remaining channels with zeros
        for i in range(0,MAX_CHANNELS-SEGMENTS*COLORS):
            data.append(0)

        # send
        if not dummy_mode:
            self.wrapper.Client().SendDmx(UNIVERSE, data, self.stop_wrapper)




if __name__=="__main__":
    o = OlaPlugin()
