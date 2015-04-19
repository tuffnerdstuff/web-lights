import array
from ola.ClientWrapper import ClientWrapper
import storage

from plugins.server_plugin import ServerPlugin



class OlaPlugin(ServerPlugin):
    
    UNIVERSE = 1
    SEGMENTS = 8
    COLORS = 3
    MAX_CHANNELS = 512
    
    ATTR_RED = 'r'
    ATTR_GREEN = 'g'
    ATTR_BLUE = 'b'
    
    def __init__(self):
        # instance variables
        self.lastR = 0
        self.lastG = 0
        self.lastB = 0
        self.wrapper = None
        
        # restore last setting
        data = storage.load_color()
        self.lastR = data[ATTR_RED]
        self.lastG = data[ATTR_GREEN]
        self.lastB = data[ATTR_BLUE]
        self.send_color(lastR,lastG,lastB)
    
    def stop_wrapper(self,state):
        wrapper.Stop()

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
        wrapper.Client().SendDmx(UNIVERSE, data, stop_wrapper)
      
      
    
    def get(self):
        return {ATTR_RED: self.lastR, ATTR_GREEN : self.lastG, ATTR_BLUE : self.lastB}
        
    def set(self, values):
        
        # send color to DMX
        send_color(values[ATTR_RED], values[ATTR_GREEN], values[ATTR_BLUE])
        
        # store color
        self.lastR = r
        self.lastG = g
        self.lastB = b
        storage.save_state()
