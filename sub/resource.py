
class Resource(object):

	def __init__(self, name):
		self.name = name
		self.users = []

	def add_user(self, user):
		self.users.append(user)
		
	def __str__(self):
		return self.name
