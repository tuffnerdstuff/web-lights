from yapsy.IPlugin import IPlugin
import storage, copy

class ServerPlugin(IPlugin):
    
    def __init__(self):
        self.name = "dummy"
        self.plugin_manager = None
        self.state = {}
    
    """ General initialization to be done for each plugin. 
        Do not override, use _on_init_plugin() instead. """
    def _init_plugin(self,name,plugin_manager):
        self.name = name
        self.plugin_manager = plugin_manager
        self._on_init_plugin()
    
    """ restore state from persistency """
    def _restore_state(self):
        print("%s._restore_state" % self.name)
        self.state = storage.load(self.name)

    """ Saves the state of the plugin """
    def _save_state(self):
        print("%s._save_state" % self.name)
        storage.save(self.name,self.state)
    
    """ Initialization specific for subclass """
    def _on_init_plugin(self):
        self._restore_state()
        pass

         
    """ Realizes the current state (switch on light, wake up PC, nuke planet, etc.) """
    def _render_state(self):
        pass
      
    """ Alters the state of the plugin based on the arguments """
    def do(self,args):
        pass
    
    """ Returns the current state of the plugin """
    def get_state(self):
        return copy.deepcopy(self.state)
    
    def hello(self):
        return "Hello, my name is %s!" % self.name
