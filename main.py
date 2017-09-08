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
		user_indices = list(range(0, 30))
		for curr in user_indices:
			res_index = random.randint(0, len(self.__resources) - 1)
			print(res_index)
			print(len(self.__resources))
			time = random.randint(1, 31)
			user = User("user" + str(curr + 1), self.__resources[res_index], time)
			self.__users.append(user)
			self.__resources[res_index].add_user(user)

	def __set_res(self, num):
		self.__resources = []
		self.__resources = [Resource("res" + str(count + 1)) for count in xrange(num)]

	def run(self):
		fg = "white"
		bg = "#3498db"
		bg2 = "#9b59b6"
		self.table.set(0,0,"Resources", foreground=fg, background=bg)
		self.table.set(0,1,"Status", foreground=fg, background=bg)
		self.table.set(0,2,"CurrUser", foreground=fg, background=bg)
		self.table.set(0,3,"Time Left", foreground=fg, background=bg)
		self.table.set(0,4,"Users", foreground=fg, background=bg2)
		self.table.set(0,5,"Status", foreground=fg, background=bg2)
		self.table.set(0,6,"CurrRes", foreground=fg, background=bg2)
		self.table.set(0,7,"Time Left", foreground=fg, background=bg2)

		x = 1
		y = 0
		for resource in self.__resources:
			self.table.set(x, 0, resource.name)
			if resource.get_status() == "Free":
				self.table.set(x, 1, resource.get_status(), foreground="white", background="#27ae60")
			else:
				self.table.set(x, 1, resource.get_status(), foreground="white", background="red")
			self.table.set(x, 2, resource.get_current_user())
			self.table.set(x, 3, resource.get_time_left())
			resource.next_user()
			x += 1

		x = 1
		for user in self.__users:
			self.table.set(x, 4, user.name)
			if user.get_status() == "Free":
				self.table.set(x, 5, user.get_status(), foreground="white", background="#27ae60")
			elif user.get_status() == "Ongoing":
				self.table.set(x, 5, user.get_status(), foreground="white", background="red")
			else:
				self.table.set(x, 5, user.get_status(), foreground="black", background="#f1c40f")
 			self.table.set(x, 6, user.get_resource())
			self.table.set(x, 7, user.get_time())
			user.subtract_time()
			x += 1

		self.after(1000, self.run)



class Table(tk.Frame):
    def __init__(self, parent, rows=10, columns=2):
        tk.Frame.__init__(self, parent, background="#34495e")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text="",
                                 borderwidth=1, width=10, foreground="black", background="white")
                label.grid(row=row, column=column, sticky="nsew", padx=0.5, pady=0.5)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value, foreground="black", background="white"):
        widget = self._widgets[row][column]
        widget.configure(text=value, foreground=foreground, background=background)


main = Main()
main.randomize()
main.after(10, main.run)
main.mainloop()
