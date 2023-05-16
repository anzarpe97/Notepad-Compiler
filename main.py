from tkinter import messagebox, filedialog as f, ttk
import tkinter as tk



class App(tk.Tk):
  
   def __init__(self):

        super().__init__()

        self.title('Notepad Compiler')
        self.geometry('600x600+200+10')

        self.FileRoute = "route"

        # File Menu

        menuBar = tk.Menu()
        fileMenu =tk.Menu(menuBar, tearoff = False)

        fileMenu.add_command(label = "New File", accelerator = "Ctrl+N", command = lambda: self.newFile())
        fileMenu.add_command(label = "Open File", accelerator = "Ctrl+O", command = lambda: self.openFile())
        fileMenu.add_command(label = "Save File", accelerator = "Ctrl+S", command = lambda: self.saveFile())
        fileMenu.add_command(label = "Save As", accelerator = "Ctrl+G", command = lambda: self.saveAsFile())
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", accelerator = "", command = lambda: self.exit())

        formatMenu = tk.Menu(menuBar, tearoff = False)

        formatMenu.add_command(label = "Cut", accelerator = "Ctrl+x", command = lambda: self.cut())
        formatMenu.add_command(label = "Copy", accelerator = "Ctrl+c", command = lambda: self.copy())
        formatMenu.add_command(label = "Paste", accelerator = "Ctrl+V", command = lambda: self.paste())
        
        menuBar.add_cascade(menu=fileMenu, label = "File")
        menuBar.add_cascade(menu=formatMenu, label = "Format")

        self.config(menu=menuBar)

        # Text Box

        self.text = tk.Text(self)
        self.text.pack(fill="both",expand=1)
        self.text.config(border=0, padx=6, pady=5, font = ("Console",14))


   def newFile (self):
       
        self.title("New File - " + self.FileRoute + " - Notepad Compiler")
        self.text.delete(1.0, "end")

   def openFile (self):

        fileRoute = f.askopenfilename(initialdir = ".", filetypes = (("Archivos de Texto", "*.txt"),), title = "Open File")

        self.title("Open File - " + fileRoute + " - Notepad Compiler")

   def saveFile (self):
       
       self.title( self.FileRoute + " - Notepad Compiler")

   def saveAsFile (self):
       
       self.title(self.FileRoute + " - Notepad Compiler")

   def cut (self):
       
       print("cortado")

   def copy (self):

       print("Copiado")

   def paste (self):
       
       print(self.route)
       self.route = "MOOMO"

   # Metodo para salir del Block de nota

   def exit (self):
      
      flag = messagebox.askokcancel(message = " Are you sure you want to exit?", title = "Notepad Compile")

      if flag == 1:
         
         self.destroy()

if __name__ == "__main__":
  
  app = App()
  app.mainloop()