
class Resource(object):

	def __init__(self, name):
		self.name = name
		self.users = []
		self.user_idx = 0

	def add_user(self, user):
		self.users.append(user)

	def __str__(self):
		return self.name

	def get_status(self):
		if self.user_idx < len(self.users):
			return "Used"
		return "Free"

	def get_current_user(self):
		if self.user_idx < len(self.users):
			name = self.users[self.user_idx].name
			return name
		return "Free"

	def get_time_left(self):
		time = 0
		for user in self.users:
			time += user.get_time_of_resource(self)
		return time

	def next_user(self):
		if self.user_idx < len(self.users):
			if self.users[self.user_idx].get_time_left() <= 0:
				self.user_idx += 1
