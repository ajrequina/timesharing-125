from resource import Resource

class User(object):

	def __init__(self, name):
		self.name = name
		self.resources = {}
		self.res_index = 0
		self.time = 10

	def add_resource(self, resource, time):
		self.resources[resource] = time

	def get_time_of_resource(self, resource):
		return self.resources[resource]

	def get_status(self):
		if self.res_index < len(list(self.resources.values())):
			if self.name == list(self.resources.keys())[self.res_index].get_current_user():
				return "Ongoing"
			return "In Waiting"
		return "Free"

	def get_current_resource(self):
		if self.res_index < len(list(self.resources.values())):
			return list(self.resources.keys())[self.res_index].name

	def get_time_left(self):
		if self.res_index < len(list(self.resources.values())):
			return list(self.resources.values())[self.res_index]
		return 0

	def subtract_time(self):
		if self.res_index < len(list(self.resources.values())):
			if self.name == list(self.resources.keys())[self.res_index].get_current_user():
				curr_res = list(self.resources.keys())[self.res_index]
				self.resources[curr_res] -= 1
				if(self.resources[curr_res] <= 0):
					self.res_index += 1
