import array
from ola.ClientWrapper import ClientWrapper
import storage

wrapper = None
UNIVERSE = 1
SEGMENTS = 8
COLORS = 3
MAX_CHANNELS = 512
lastR = 0
lastG = 0
lastB = 0

def DmxSent(state):
  wrapper.Stop()

def SendDMXFrame(r,g,b):
  
  global wrapper
  wrapper = ClientWrapper()

  # Fill RGB bar array
  data = array.array('B')
  global loop_count
  for i in range(0,SEGMENTS):
    data.append(r)
    data.append(g)
    data.append(b)
  
  # Fill remaining channels with zeros
  for i in range(0,MAX_CHANNELS-SEGMENTS*COLORS):
    data.append(0)

  # send
  wrapper.Client().SendDmx(UNIVERSE, data, DmxSent)
  
  # store color
  global lastR, lastG, lastB
  lastR = r
  lastG = g
  lastB = b
  storage.save_color(r,g,b)

def get_color():
    return (lastR,lastG,lastB)
  
# load defaults
lastR,lastG,lastB = storage.load_color()
SendDMXFrame(lastR,lastG,lastB)
