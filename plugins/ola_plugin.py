import array, noise
from thread import start_new_thread
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

MODE_SOLID = 0
MODE_PULSE = 1
MODE_FIRE = 2

TICK_INTERVAL = 10

wrapper = None
instance = None
tick = 0
mode = MODE_FIRE

data = None

class OlaPlugin(ServerPlugin):

    ## PLUGIN METHODS ##

    def _on_init_plugin(self):
        
        # set instance
        global instance
        instance = self
        
        # restore state
        self._restore_state()
        
        # start render loop
        if not dummy_mode:
            start_new_thread(start_loop,())
        
    def do(self,data):
        
        # save state
        self.state = data
        
        # persist state
        self._save_state()

    def get_color(self):
        return ( int(self.state[ATTR_RED][0]), int(self.state[ATTR_GREEN][0]), int(self.state[ATTR_BLUE][0]) )

## OLA METHODS ##

def stop_wrapper(state):
    if not state.Succeeded():
        wrapper.Stop()
        
def start_loop():
    global wrapper
    wrapper = ClientWrapper()
    wrapper.AddEvent(TICK_INTERVAL, update_color)
    wrapper.Run()

def update_color():
    
    # Schedule tick
    wrapper.AddEvent(TICK_INTERVAL, update_color)

    # Get next color
    
    _tick()
    
    # Fill RGB bar array
    

    # Fill remaining channels with zeros
    intData = array.array('B')
    for i in data:
        intData.append(int(i))

    # send
    if wrapper:
        wrapper.Client().SendDmx(UNIVERSE, intData, stop_wrapper)

def _tick():
    if mode == MODE_SOLID:
        pass
    elif mode == MODE_PULSE:
        phase = tick / 255.0
        print("phase", phase)
        
        origR,origG,origB = instance.get_color()
        r = int(round(int(origR) * phase))
        g = int(round(int(origG) * phase))
        b = int(round(int(origB) * phase))
        
        global data
        data = array.array('B')
        for i in range(0,SEGMENTS):
            data.append(r)
            data.append(g)
            data.append(b)
        
    elif mode == MODE_FIRE:
        #r,g,b = instance.get_color()
        
        r1 = 255.0
        g1 = 180.0
        b1 = 0.0
        
        r2 = 40.0
        g2 = 0.0
        b2 = 0.0
        
        dataNew = []
        for i in range(0,SEGMENTS):
            
            brightness = noise.pnoise2(i/8.0,tick/64.0)/2.0+0.5
            
            newR = r1 * (1-brightness) + r2 * brightness
            newG = g1 * (1-brightness) + g2 * brightness
            newB = b1 * (1-brightness) + b2 * brightness
            
            print(newR,newG,newB)
            
            dataNew.append(newR)
            dataNew.append(newG)
            dataNew.append(newB)
        
        data = dataNew

    
    global tick
    tick = (tick + 1) % 99999


if __name__=="__main__":
    o = OlaPlugin()
