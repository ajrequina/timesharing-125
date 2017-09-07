import random
import time
import Tkinter as tk

from sub.resource import Resource
from sub.user import User

class Main(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.table = Table(self, 31, 8)
		self.table.pack(side="top", fill="x")

	def randomize(self):
		num_users = random.randint(1, 30)
		num_res = random.randint(1, 30)

		self.__set_res(num_res)
		self.__set_users(num_users)

	def __set_users(self, num):
		self.__users = []
		user_indices = random.sample(range(0, num), num)
		for curr in user_indices:
			user = User("user" + str(curr + 1))
			self.__users.append(user)
			res_indices = random.sample(range(0, len(self.__resources)), random.randint(1, len(self.__resources)))
			for index in res_indices:
				user.add_resource(self.__resources[index], random.randint(1, 30))
				self.__resources[index].add_user(user)

	def __set_res(self, num):
		self.__resources = []
		self.__resources = [Resource("res" + str(count + 1)) for count in xrange(num)]

	def run(self):
		self.table.set(0,0,"Resources")
		self.table.set(0,1,"Status")
		self.table.set(0,2,"CurrUser")
		self.table.set(0,3,"Time Left")
		self.table.set(0,4,"Users")
		self.table.set(0,5,"Status")
		self.table.set(0,6,"CurrRes")
		self.table.set(0,7,"Time Left")

		x = 1
		y = 0
		for resource in self.__resources:
			self.table.set(x, 0, resource.name)
			self.table.set(x, 1, resource.get_status())
			self.table.set(x, 2, resource.get_current_user())
			self.table.set(x, 3, resource.get_time_left())
			resource.next_user()
			x += 1

		x = 1
		for user in self.__users:
			self.table.set(x, 4, user.name)
			self.table.set(x, 5, user.get_status())
			self.table.set(x, 6, user.get_current_resource())
			self.table.set(x, 7, user.get_time_left())
			user.subtract_time()
			x += 1

		self.after(10, self.run)



class Table(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="",
                                 borderwidth=1, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=0.5, pady=0.5)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)


main = Main()
main.randomize()
main.after(10, main.run)
main.mainloop()
