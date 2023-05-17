from io import open
from tkinter import messagebox, filedialog as f, ttk
import tkinter as tk
import re

class App(tk.Tk):
  
    def __init__(self):

        super().__init__()

        self.title('Notepad Compiler')
        self.geometry('600x600+200+10')

        self.FileRoute = "route"
        self.fontSize = 12

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
        formatMenu.add_separator()
        formatMenu.add_command(label = "Clear All", accelerator = "", command = lambda: self.clear())
        
        viewMenu = tk.Menu(menuBar, tearoff = False)

        viewMenu.add_command(label = "Zoom in", accelerator = "Ctrl +", command = lambda: self.zoomIn())
        viewMenu.add_command(label = "Zoom Out", accelerator = "Ctrl -", command = lambda: self.zoomOut())

        menuBar.add_cascade(menu = fileMenu, label = "File")
        menuBar.add_cascade(menu = formatMenu, label = "Format")
        menuBar.add_cascade(menu = viewMenu, label = "View")

        self.bind("<Control-Key-plus>", lambda _: self.zoomIn())
        self.bind("<Control-Key-minus>", lambda _: self.zoomOut())

        self.config(menu = menuBar)

        # Text Box

        self.text = tk.Text(self,font= ('Arial', self.fontSize))
        self.text.grid(column=0, row=0, sticky="nsew")
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        scrollbar = ttk.Scrollbar(self)
        scrollbar.grid(column=1, row=0, sticky="nsew")
    # Metodo para acomodar el nombre de la ruta a solo el nombre

    def fileName (self, filename):
       
        finalName = re.search(r"(\w*)\.txt$",  filename).group()

        return finalName

    def newFile (self):
       
        self.title("New File - " + self.FileRoute + " - Notepad Compiler")
        self.text.delete(1.0, "end")

    def openFile (self):
        
        self.fileRoute = f.askopenfilename(initialdir = ".", filetypes = (("Archivos de Texto", "*.txt"),), title = "Open File")

        if self.fileRoute != "":

            finalName = self.fileName(self.fileRoute)

            file = open (self.fileRoute, "r", encoding="utf-8")

            content = file.read()

            self.text.delete(1.0, "end")

            self.text.insert("insert", content)

            file.close()

            self.title(finalName + " - Notepad Compiler")

    def saveFile (self):
       
        self.title( self.FileRoute + " - Notepad Compiler")

        value = self.text.get("1.0","end")

        with open(self.fileRoute, "w",encoding="utf-8") as f:

            f.write(value)

            f.close()
        
        print(value)

    def saveAsFile (self):
       
       self.title(self.FileRoute + " - Notepad Compiler")

    def cut (self):
        
        print("cortado")

    def copy (self):

        print("Copiado")

    def clear(self):

        self.text.delete(1.0, "end")

    def paste (self):
        
        print(self.route)
        self.route = "MOOMO"

    def zoomIn (self):

        self.fontSize += 4

        self.text.config(font= ('Arial', self.fontSize))

    def zoomOut(self):

        self.fontSize -= 4

        if self.fontSize < 8:
            
            self.fontSize = 8
            messagebox.showinfo("Bitch", "bitch")
        else:

            self.text.config(font= ('Arial', self.fontSize))

   # Metodo para salir del Block de nota

    def exit (self):
      
      flag = messagebox.askokcancel(message = " Are you sure you want to exit?", title = "Notepad Compile")

      if flag == 1:
         
         self.destroy()

if __name__ == "__main__":
  
  app = App()
  app.mainloop()

  """
path = "C:/Users/John/Documents/test.txt"
print(path.split("/")[-1])


  """