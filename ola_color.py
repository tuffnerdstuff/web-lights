import array
from ola.ClientWrapper import ClientWrapper

wrapper = None
UNIVERSE = 1
SEGMENTS = 8
COLORS = 3
MAX_CHANNELS = 512

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
                 
SendDMXFrame(0,0,0)
