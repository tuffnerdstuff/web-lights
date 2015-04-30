import array
from ola.ClientWrapper import ClientWrapper
from plugins.server_plugin import ServerPlugin

UNIVERSE = 1
SEGMENTS = 8
COLORS = 3
MAX_CHANNELS = 512

ATTR_RED = 'r'
ATTR_GREEN = 'g'
ATTR_BLUE = 'b'

class OlaPlugin(ServerPlugin):

    def __init__(self):
        super(OlaPlugin,self).__init__()
        
        # instance variables
        self.wrapper = None

    def stop_wrapper(self,state):
        self.wrapper.Stop()

    def get_color(self,data):
        return ( int(data[ATTR_RED][0]), int(data[ATTR_GREEN][0]), int(data[ATTR_BLUE][0]) )

    def send_color(self,r,g,b):
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
        self.wrapper.Client().SendDmx(UNIVERSE, data, self.stop_wrapper)


    def set_action(self,data):
    	
        r,g,b = self.get_color(data)

        # send color to DMX
        self.send_color(r,g,b)
        
    def init_action(self):
        # send last light data to device
        self.set_action(self.data)

if __name__=="__main__":
    o = OlaPlugin()
