from tkinter import *
from .controllers import *
from .models import *
from .views import *

root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

base = Core(root)

root.mainloop()

