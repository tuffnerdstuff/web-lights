from yapsy.IPlugin import IPlugin
import storage

class ServerPlugin(IPlugin):
	
	def __init__(self):
		self.name = self.__class__.__name__
	def hello(self):
		return "Hello, my name is %s!" % self.name
	def get(self):
		return {}
	def set(self):
		pass
	def save_state(self):
		storage.save(self.name, self.get())
	def load_state(self):
		self.set(storage.load())
	def set_name(name):
		self.name = name
		
