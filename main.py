from compiler import Compiler
from idlelib.percolator import Percolator
import idlelib.colorizer as ic
from io import open
from tkinter import messagebox, filedialog as f, ttk
import tkinter as tk
import re

class App(tk.Tk):
  
    def __init__(self):

        super().__init__()
        
        image_16 = tk.PhotoImage(file = "icons/pencil (1).png")
        image_32 = tk.PhotoImage(file = "icons/pencil32.png")

        self.iconphoto(False, image_32, image_16)
        self.title('Notepad Compiler')
        self.geometry("800x600+10+10")
        self.fontSize = 12
        self.Route = ""
        self.starGUI()

    def starGUI(self):

         # File Menu

        menuBar = tk.Menu()

        fileMenu =tk.Menu(menuBar, tearoff = False)

        fileMenu.add_command(label = "Archivos Nuevo", accelerator = "Ctrl+N", command = lambda: self.newFile())
        fileMenu.add_command(label = "Abrir Archivo", accelerator = "Ctrl+O", command = lambda: self.openFile())
        fileMenu.add_command(label = "Guardar", accelerator = "Ctrl+S", command = lambda: self.saveFile())
        fileMenu.add_command(label = "Guardar Como", accelerator = "Ctrl+G", command = lambda: self.saveAsFile())
        fileMenu.add_separator()
        fileMenu.add_command(label = "Salir", accelerator = "", command = lambda: self.exit())
        

        formatMenu = tk.Menu(menuBar, tearoff = False)

        formatMenu.add_command(label="Cortar", accelerator='Ctrl+X', command = lambda: self.focus_get().event_generate("<<Cut>>") )
        formatMenu.add_command(label="Copiar", accelerator='Ctrl+C', command = lambda: self.focus_get().event_generate("<<Copy>>"))
        formatMenu.add_command(label="Pegar", accelerator='Ctrl+V',  command = lambda: self.focus_get().event_generate("<<Paste>>"))
        formatMenu.add_separator()
        formatMenu.add_command(label = "Limpiar", accelerator = "", command = lambda: self.clear())

        viewMenu = tk.Menu(menuBar, tearoff = False)

        viewMenu.add_command(label = "Acercar", accelerator = "Ctrl +", command = lambda: self.zoomIn())
        viewMenu.add_command(label = "Alejar", accelerator = "Ctrl -", command = lambda: self.zoomOut())

        compilerMenu = tk.Menu(menuBar, tearoff = False)
        compilerMenu.add_command(label = "Run", accelerator = "Ctrl + Q", command = lambda: self.startcompiler())

        menuBar.add_cascade(menu = fileMenu, label = "Archivo")
        menuBar.add_cascade(menu = formatMenu, label = "Formato")
        menuBar.add_cascade(menu = viewMenu, label = "Ver")
        menuBar.add_cascade(menu = compilerMenu, label = "Compilador")
        
        # Comandos teclados

        self.bind("<Control-Key-plus>", lambda _: self.zoomIn())
        self.bind("<Control-Key-minus>", lambda _: self.zoomOut())
        self.bind("<Control-Key-s>", lambda _: self.saveFile())
        self.bind("<Control-Key-n>", lambda _: self.newFile())
        self.bind("<Control-Key-o>", lambda _: self.openFile())
        self.bind("<Control-Key-g>", lambda _: self.saveAsFile())

        self.config(menu = menuBar)

        # Text Box

        self.text = tk.Text(self,font= ('Arial', self.fontSize))
        self.text.grid(column=0, row=0, sticky="nsew")

        Percolator(self.text).insertfilter(ic.ColorDelegator())

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)

        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command = self.text.yview)
        scrollbar.grid(column=1, row=0, sticky="nsew")

        self.text.config(yscrollcommand=scrollbar.set)

    # Metodo para acomodar el nombre de la ruta a solo el nombre

    def fileName (self, filename):
       
        finalName = re.search(r"(\w*)\.txt$",  filename).group()

        return finalName

    # Metodo para crear un nuevo archivo

    def newFile (self):
       
        self.title("New File - Notepad Compiler")
        self.text.delete(1.0, "end")
        self.Route = ""

    # Metodo para abrir un archivo

    def openFile (self):
        
        self.Route = f.askopenfilename(initialdir = ".", filetypes = (("Archivos de Texto", "*.txt"),), title = "Abrir Archivo")

        if self.Route != "":

            finalName = self.fileName(self.Route)

            file = open (self.Route, "r", encoding="utf-8")

            content = file.read()

            self.text.delete(1.0, "end")

            self.text.insert("insert", content)

            file.close()

            self.title(finalName + " - Notepad Compiler")

    # Metodo para guardar un archivo

    def saveFile (self):
       
       if self.Route != "":
            
            name = self.fileName(self.Route)

            self.title(name + " - Notepad Compiler")

            value = self.text.get("1.0","end")

            with open(self.Route, "w",encoding="utf-8") as file:

                file.write(value)

                file.close()
       else: 
            
            self.saveAsFile()
             
    def saveAsFile (self):
       
        folderToSave = f.asksaveasfile(filetypes = (('Text Document', '*.txt'),), defaultextension = (('Text Document', '*.txt'),))

        if folderToSave == "":

                pass
                
        else:
                try:
                     
                 self.Route = folderToSave.name

                 with open(folderToSave.name, "w") as file:

                    value = self.text.get("1.0","end")
                    
                    file.write(value)
                    
                    file.close()

                    name = self.fileName(self.Route)

                    self.title(name + " - Notepad Compiler")

                except AttributeError:

                    pass

    def clear(self):

        self.text.delete(1.0, "end")

    def zoomIn (self):

        self.fontSize += 4

        self.text.config(font= ('Arial', self.fontSize))

    def zoomOut(self):

        self.fontSize -= 4

        if self.fontSize < 8:
            
            self.fontSize = 8
            
        else:

            self.text.config(font= ('Arial', self.fontSize))       

    def startcompiler(self):

        self.compilerWindow = Compiler()

   # Metodo para salir del Block de nota

    def exit (self):
      
      flag = messagebox.askokcancel(message = " Are you sure you want to exit?", title = "Notepad Compile")

      if flag == 1:

         self.destroy()

class Compiler(tk.Toplevel):

    def __init__(self):

        super().__init__()

        self.starCompiler()

    def starCompiler(self):

        self.iconbitmap("icons/settings.ico")   
        self.geometry("300x400+500+50")
        self.title("Compiler")
        self.closewindow = tk.Button(self, text="Cerrar Ventana",relief="flat",command=self.destroy,background="#e00000", foreground="White")
        self.closewindow.place(x=200,y=100)
        self.focus()
        self.grab_set()

if __name__ == "__main__":
  
  app = App()
  app.mainloop()
