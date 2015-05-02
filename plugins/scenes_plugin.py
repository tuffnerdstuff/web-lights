from plugins.server_plugin import ServerPlugin

SECT_SCENES = "scenes"
ATTR_NAME = "name"
ATTR_STATES = "states"
ATTR_PLUGIN = "plugin"
ATTR_DATA = "data"

class ScenePlugin(ServerPlugin):
    
    def save_state(self): 
        # This plugin can only be configured server-side
        pass
    
    def set_state(self, data):
        # We do not have to keep track of any state
        pass
    
    def set_action(self,data):
        # set action data-scheme: {"name": "scenename"}
        name = data[ATTR_NAME][0]
        # scene data-scheme: "scenes": [ { "name": "scenename", "states" : { "name": "pluginname1", "data": {... data ...} }, ...} ]
        for scene in self.data[SECT_SCENES]:
            if scene[ATTR_NAME] == name:
                self.activate_scene(scene[ATTR_STATES])
                break
                
    def activate_scene(self,states):
        for state in states:
            plugin_name = state[ATTR_PLUGIN]
            plugin_data = state[ATTR_DATA]
            plugin = self.plugin_manager.get_plugin(plugin_name)
            plugin.set(plugin_data)
        
            
        
    
