import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

from MySQL import MySQL

class GUI(): 
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add title
        self.win.title("MySQL GUI")
        self.win.resizable(0, 0)
        self.createWidgets()

        # Create the database instance
        self.mySQL = MySQL()
    
    # Callback function for quit
    def _quit(self):
        self.win.quit()
        self.win.destroy()

    # Callback function for about
    def _msgBox(self):
        mBox.showinfo('Python Message Info Box', 'MySQL Python GUI created using tkinter\nThe year is 2018')

    def _insertQuote(self):
        print('insert quote')
        title = self.titleInsert.get()
        page = self.pageInsert.get()
        quote = self.scr.get(1.0, tk.END)
        print(title)
        print(page)
        print(quote)
        self.mySQL.insertBooks(title, page, quote)
    
    def _getQuote(self):
        print('get quote')
        allBooks = self.mySQL.showBooks()
        print(allBooks)
        self.scr.insert(tk.INSERT, allBooks)


    def _modyQuote(self):
        print('mody quote')
        raise NotImplementedError("This still needs to be implemented for the SQL command.")

    # Create all widgets in this GUI
    def createWidgets(self):
        # Create tab control
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = "MySQL")
        tabControl.pack(expand = 1, fill = "both")

        # Create Menu bar
        menuBar = Menu(self.win)
        self.win.config(menu = menuBar)

        # ---- Menu -----
        
        # Adding a file menu
        fileMenu = Menu(menuBar, tearoff = 0)
        fileMenu.add_command(label = "New")
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = self._quit)

        # Adding a help menu
        helpMenu = Menu(menuBar, tearoff = 0)
        helpMenu.add_command(label = "About", command = self._msgBox)

        menuBar.add_cascade(label = "File", menu = fileMenu)
        menuBar.add_cascade(label = "Help", menu = helpMenu)

        # ---- Input Frame ----
        inputFrame = ttk.LabelFrame(tab1, text = ' Python Database ')
        inputFrame.grid(column = 0, row = 0, padx = 4, pady = 4)

        # Adding Labels
        # Label for book title
        Label1 = ttk.Label(inputFrame, text = 'Book Title:')
        Label1.grid(column = 0, row = 0, sticky = 'W', padx = 4, pady = 4)

        # Label for page
        Label2 = ttk.Label(inputFrame, text = 'Page:')
        Label2.grid(column = 1, row = 0, sticky = 'W', padx = 4, pady = 4)

        # Adding entry boxes
        
        # Entry boxes for insert quote
        # Title
        self.titleInsert = tk.StringVar()
        self.titleToInsert = ttk.Entry(inputFrame, width = 48, textvariable = self.titleInsert)
        self.titleToInsert.grid(column = 0, row = 1, padx = 4, pady = 4, sticky = 'W')

        # Page
        self.pageInsert = tk.StringVar()
        self.pageToInsert = ttk.Entry(inputFrame, width = 6, textvariable = self.pageInsert)
        self.pageToInsert.grid(column = 1, row = 1, padx = 4, pady = 4, sticky = 'W')

        # Entry boxes for get quote
        # Title
        self.titleGet = tk.StringVar()
        self.titleToGet = ttk.Entry(inputFrame, width = 48, textvariable = self.titleGet)
        self.titleToGet.grid(column = 0, row = 2, padx = 4, pady = 4, sticky = 'W')

        # Page
        self.pageGet = tk.StringVar()
        self.pageToGet = ttk.Entry(inputFrame, width = 6, textvariable = self.pageGet)
        self.pageToGet.grid(column = 1, row = 2, padx = 4, pady = 4, sticky = 'W')

        # Entry boxes for modify quote
        # Title
        self.titleModify = tk.StringVar()
        self.titleToModify = ttk.Entry(inputFrame, width = 48, textvariable = self.titleModify)
        self.titleToModify.grid(column = 0, row = 3, padx = 4, pady = 4, sticky = 'W')

        # Page
        self.pageModify = tk.StringVar()
        self.pageToModify = ttk.Entry(inputFrame, width = 6, textvariable = self.pageModify)
        self.pageToModify.grid(column = 1, row = 3, padx = 4, pady = 4, sticky = 'W')

        # Adding buttons
        # button for insert quote
        self.insertQuote = ttk.Button(inputFrame, text = 'Insert Quote', command = self._insertQuote)
        self.insertQuote.grid(column = 2, row = 1)
       
        # button for get quote
        self.getQuote = ttk.Button(inputFrame, text = 'Get Quote', command = self._getQuote)
        self.getQuote.grid(column = 2, row = 2)
        
        # button for modify quote
        self.modyQuote = ttk.Button(inputFrame, text = 'Mody Quote', command = self._modyQuote)
        self.modyQuote.grid(column = 2, row = 3)
        
        # ---- Text Frame ----
        textFrame = ttk.LabelFrame(tab1, text = ' Book Quotation ')
        textFrame.grid(column = 0, row = 1, padx = 4, pady = 4)

        # Adding a scrolled text
        scrolW = 58
        scrolH = 10
        self.scr = scrolledtext.ScrolledText(textFrame, width=scrolW, height=scrolH, wrap = tk.WORD)
        self.scr.grid(column = 0, row = 0, sticky='WE')

gui = GUI()
gui.win.mainloop()