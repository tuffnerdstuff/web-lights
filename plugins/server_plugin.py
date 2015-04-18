from yapsy.IPlugin import IPlugin

class ServerPlugin(IPlugin):
	def hello(self):
		return "Hello, my name is %s!" % self.__class__.__name__
