from plugins.server_plugin import ServerPlugin

class DummyPlugin(ServerPlugin):
	def get(self):
		print("DummyPlugin.get")
		return []
	
	def set(self,values):
		print("DummyPlugin.set %s" % values)
	
