from yapsy.PluginManager import PluginManager, PluginFileLocator
from yapsy.PluginFileLocator import PluginFileAnalyzerMathingRegex
from yapsy.IPlugin import IPlugin
import re

PLUGIN_PATH='plugins'
PLUGIN_SUFFIX='-plugin'
PLUGIN_EXT='\.py'

class ServerPluginManager():
	def __init__(self):
		self.plugin_manager = PluginManager(plugin_locator=PluginFileLocator(analyzers=[PluginFileAnalyzerMathingRegex("regex_matcher",('^.*%s%s$' % (PLUGIN_SUFFIX,PLUGIN_EXT)))]))
		self.plugin_manager.setPluginPlaces([PLUGIN_PATH])
		self.plugin_map = {}
		
		self.init_plugins()
		
	def init_plugins(self):
		
		# Clear plugin map
		self.plugin_map = {}
		
		# Collect plugins, activate them and add them to the map
		self.plugin_manager.collectPlugins()
		for plugin in self.plugin_manager.getAllPlugins():
			name = re.sub(PLUGIN_SUFFIX,'',plugin.name)
			self.plugin_manager.activatePluginByName(plugin.name)
			self.plugin_map[name] = plugin.plugin_object
	
	def get_plugin(self,plugin_name):
		try:
			return self.plugin_map[plugin_name]
		except Exception:
			return None
				
p = ServerPluginManager()
p.get_plugin("test").hello()
			
