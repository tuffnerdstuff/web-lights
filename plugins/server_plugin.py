from yapsy.IPlugin import IPlugin
import storage

class ServerPlugin(IPlugin):
	
    def __init__(self):
        self.name = self.__class__.__name__
    def hello(self):
        return "Hello, my name is %s!" % self.name
    def get(self):
        return {}
    def set(self,data):
        pass
    def save_state(self):
        storage.save(self.name, self.get())
    def load_state(self):
        print("load %s" % self.name)
        data = storage.load(self.name)
	if data:
            self.set(data)
    def set_name(self,name):
        self.name = name
		
