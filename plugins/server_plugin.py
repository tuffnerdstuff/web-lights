from yapsy.IPlugin import IPlugin
import storage, copy

class ServerPlugin(IPlugin):
    
    def __init__(self):
        self.name = "dummy"
        self.plugin_manager = None
        self.data = {}
        
    def hello(self):
        return "Hello, my name is %s!" % self.name
        
    def get(self):
        print("%s.get" % self.name)
        return copy.deepcopy(self.data)
        
    def set(self,data):
        print("%s.set %s" % (self.name,data))
        self.set_state(data)
        self.save_state()
        self.set_action(data)

    def set_state(self, data):
        self.data = data
        
    def set_action(self,data):
        pass
    
    def save_state(self):
        print("%s.save data=%s" % (self.name, self.get()))
        storage.save(self.name, self.get())
        
    def load_state(self):
        print("%s.load" % self.name)
        data = storage.load(self.name)
        if data:
            self.data = data
            
    def init(self,name,plugin_manager):
        self.name = name
        self.plugin_manager = plugin_manager
        self.load_state()
        self.init_action()
        
    def init_action(self):
        pass
