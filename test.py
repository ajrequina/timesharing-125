import Tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = SimpleTable(self, 31, 8)
        t.pack(side="top", fill="x")



if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
