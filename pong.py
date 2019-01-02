import tkinter as tk       

class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid()                       
        self.createWidgets()

    def createWidgets(self):
        self.main_canvas = tk.Canvas(self, height=600, width=1000, bg='black')
        self.main_canvas.grid()
        self.main_canvas.create_rectangle(10,200,20,270, fill='white', outline='white')
        self.main_canvas.create_rectangle(990,200,980,270, fill='white', outline='white')

"""class raquette()
    pass"""


app = Application()                       
app.master.title('Sample application')    
app.mainloop()