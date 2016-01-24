from plugins.server_plugin import ServerPlugin

SECT_SCENES = "scenes"
ATTR_LOADACTION = "load"
ATTR_SAVEACTION = "save"
ATTR_DELACTION = "delete"
ATTR_NAME = "name"
ATTR_STATES = "states"
ATTR_PLUGIN = "plugin"
ATTR_DATA = "data"

class ScenePlugin(ServerPlugin):
    
    def set_state(self, data):
        # We do not have to keep track of any state
        pass
    
    def set_action(self,data):
        
        if (ATTR_LOADACTION in data):
        
            ## LOAD SCENE ##
            
            # set action data-scheme: {"load": "scenename"}
            name = data[ATTR_LOADACTION][0]
            # scene data-scheme: "scenes": [ { "name": "scenename", "states" : { "plugin": "pluginname1", "data": {... data ...} }, ...} ]
            for scene in self.data[SECT_SCENES]:
                if scene[ATTR_NAME] == name:
                    self.activate_scene(scene[ATTR_STATES])
                    break
                    
        elif (ATTR_SAVEACTION in data):
            
            ## SAVE SCENE ##
            
            # set action data-scheme: {"save": "scenename", "plugin": "plugin1", "plugin2", ... , "pluginN"}
            scenename = data[ATTR_SAVEACTION][0]
            plugins = data[ATTR_PLUGIN]
            states = []
            
            for plugin in plugins:
                plugin_obj = self.plugin_manager.get_plugin(plugin)
                if plugin_obj:
                    states.append({ATTR_PLUGIN : plugin, ATTR_DATA : plugin_obj.get()})
            
            new_scenes = []
            new_scene = {ATTR_NAME:scenename,ATTR_STATES:states}
            scene_updated = False
            for scene in self.data[SECT_SCENES]:
                if scene[ATTR_NAME] == scenename:
                    new_scenes.append(new_scene)
		    scene_updated = True
                else:
                    new_scenes.append(scene)

            if not scene_updated:
                new_scenes.append(new_scene)
            
            self.data = {SECT_SCENES:new_scenes}
            self.save_state()
                
        elif (ATTR_DELACTION in data):
            scenename = data[ATTR_DELACTION][0]
                    
            new_scenes = []

            # iterate over scenes and leave out deleted scene
            for scene in self.data[SECT_SCENES]:
                if scene[ATTR_NAME] != scenename:
                    new_scenes.append(scene)
            
            self.data = {SECT_SCENES:new_scenes}
            self.save_state()
                
                
    def activate_scene(self,states):
        for state in states:
            plugin_name = state[ATTR_PLUGIN]
            plugin_data = state[ATTR_DATA]
            plugin = self.plugin_manager.get_plugin(plugin_name)
            plugin.set(plugin_data)
            
        
            
        
    