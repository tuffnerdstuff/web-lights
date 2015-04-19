import array
from ola.ClientWrapper import ClientWrapper
import storage
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
        # instance variables
        self.lastR = 0
        self.lastG = 0
        self.lastB = 0
        self.wrapper = None

        # restore last setting
        self.lastR,self.lastG,self.lastB = storage.load_color()
        self.send_color(self.lastR,self.lastG,self.lastB)

    def stop_wrapper(self,state):
        self.wrapper.Stop()

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



    def get(self):
        return {ATTR_RED: self.lastR, ATTR_GREEN : self.lastG, ATTR_BLUE : self.lastB}

    def set(self, values):
    	
	r = int(values[ATTR_RED][0])
	g = int(values[ATTR_GREEN][0])
	b = int(values[ATTR_BLUE][0])

        # send color to DMX
        self.send_color(r,g,b)

        # store color
        self.lastR = r
        self.lastG = g
        self.lastB = b
        storage.save_color(r,g,b)

if __name__=="__main__":
    o = OlaPlugin()
