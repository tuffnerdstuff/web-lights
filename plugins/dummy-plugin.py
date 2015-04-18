from plugins.server_plugin import ServerPlugin

class DummyPlugin(ServerPlugin):
	def get():
		print("DummyPlugin.get")
		return []
	
	def set(values):
		print("DummyPlugin.set %s" % values)
	
