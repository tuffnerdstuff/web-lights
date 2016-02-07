from plugins.server_plugin import ServerPlugin
from thread import start_new_thread
from scapy.all import srp
from scapy.all import Ether, ARP, conf

import sys, time

class ARPingPlugin(ServerPlugin):
    
    def _on_init_plugin(self):
        self.macs = ("84:8e:df:59:8c:c3")
        start_new_thread(self.__scan_loop,())
    
    def do(self,args):
        pass
        
    def __scan_loop(self):
        while True:
            for ip, mac in arping():
                if mac in self.macs:
                    print("%s went online!")
                    break
            time.sleep(5)
            
        

def arping(iprange="192.168.1.*"):
    """Arping function takes IP Address or Network, returns nested mac/ip list"""

    #conf, verb = 0
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=iprange), timeout=4)

    collection = []
    for snd, rcv in ans:
        result = rcv.sprintf(r"%ARP.psrc% %Ether.src%").split()
        collection.append(result)
    return collection

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            print "arping", ip
            print arping(ip)

    else:
        print arping()
