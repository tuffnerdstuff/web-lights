from plugins.server_plugin import ServerPlugin
from thread import start_new_thread

import os, time, subprocess

TRIGGER_ON = "Alles an"
TRIGGER_OFF = "Alles aus"


class ARPingPlugin(ServerPlugin):
    
    def _on_init_plugin(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        self.arping_path = os.path.join(dir_path,'arping')
        
        self.was_on = True
        
        start_new_thread(self.__scan_loop,())
    
    def do(self,args):
        pass
        
    def __scan_loop(self):
        while True:
            
            plugin = self.plugin_manager.get_plugin("scenes")
            #print(plugin.get_state())
            
            if plugin:
                print("SCANNING")
                is_device_online = subprocess.call(self.arping_path) == 0
                #print(is_device_online)
                if is_device_online and not self.was_on:
                    self.was_on = True
                    plugin.do({"load":[TRIGGER_ON]})
                    print("TRIGGER ON!!!")
                elif not is_device_online and self.was_on:
                    self.was_on = False
                    plugin.do({"load":[TRIGGER_OFF]})
                    print("TRIGGER OFF!!!")
            time.sleep(5)
