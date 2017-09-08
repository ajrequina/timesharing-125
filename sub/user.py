from resource import Resource

class User(object):

	def __init__(self, name, resource=None, time=0):
		self.name = name
		self.resource = resource
		self.time = time

	def get_time(self):
		return self.time

	def get_status(self):
		if self.time:
			if self.name == self.resource.get_current_user():
				return "Ongoing"
			return "In Waiting"
		return "Free"

	def get_resource(self):
		if self.time:
			return self.resource.name
		return "Free"

	def subtract_time(self):
		if self.time:
			if self.name == self.resource.get_current_user():
				self.time -= 1
