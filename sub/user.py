from resource import Resource

class User(object):

	def __init__(self, name, resource=None, time=0):
		self.resource = resource
		self.name = name
		self.time = time