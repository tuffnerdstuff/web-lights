from yapsy.PluginManager import PluginManager, PluginFileLocator
from yapsy.PluginFileLocator import PluginFileAnalyzerMathingRegex
import re, os, sys

ROOT = os.path.dirname(os.path.realpath(sys.argv[0]))
PLUGIN_PATH=os.path.join(ROOT,"plugins")
PLUGIN_SUFFIX='_plugin'
PLUGIN_EXT='\.py'
PLUGIN_DUMMY_NAME='server'


class ServerPluginManager():
	def __init__(self):
		self.plugin_manager = PluginManager(plugin_locator=PluginFileLocator(analyzers=[PluginFileAnalyzerMathingRegex("regex_matcher",('^.*%s%s$' % (PLUGIN_SUFFIX,PLUGIN_EXT)))]))
		self.plugin_manager.setPluginPlaces([PLUGIN_PATH])
		self.dummy_plugin = None
		self.plugin_map = {}
		
		self.init_plugins()
		
	def init_plugins(self):
		
		# Clear plugin map
		self.plugin_map = {}
		
		# Collect plugins, activate them and add them to the map
		self.plugin_manager.collectPlugins()
		for plugin in self.plugin_manager.getAllPlugins():
			name = re.sub(PLUGIN_SUFFIX,'',plugin.name)
			# set plugin name
			plugin.plugin_object.init(name)
			print(name)
			if name == PLUGIN_DUMMY_NAME:
				self.dummy_plugin = plugin
			else:
				self.plugin_manager.activatePluginByName(plugin.name)
				self.plugin_map[name] = plugin
	
	def get_plugin_info(self,name):
		try:
			return self.plugin_map[name]
		except Exception:
			return self.dummy_plugin
			
	def get_plugin(self,name):
		return self.get_plugin_info(name).plugin_object
		
if __name__ == "__main__":	
	print("STARTING")	
	p = ServerPluginManager()
	print p.get_plugin("pups").hello()
