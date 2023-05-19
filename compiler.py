from tkinter import messagebox, filedialog as f, ttk
import tkinter as tk

class Compiler (tk.Tk):
  
    def __init__(self):
       super().__init__()


       self.starGUI()
       

    def starGUI(self):
       
       self.title("Compiler")
       self.geometry("600x600")

if __name__ == "__main__":
  
  app = Compiler()
  app.mainloop()