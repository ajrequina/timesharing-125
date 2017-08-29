import random

from sub.resource import Resource
from sub.user import User

class Main(object):

	def __init__(self):
		self.__users = []
		self.__resources = []
		self.__randomize()

	def __randomize(self):
		num_users = random.randint(1, 30)
		num_res = random.randint(1, 30)

		self.__set_res(num_res)
		self.__set_users(num_users)
		

	def __set_users(self, num):
		res = self.__resources[random.randint(0, len(self.__resources) - 1)]
		time = random.randint(1, 30)
		self.__users = [User("user" + str(count + 1), res, time) for count in xrange(num)]

	def __set_res(self, num):
		self.__resources = [Resource("resource" + str(count + 1)) for count in xrange(num)]

main = Main()


