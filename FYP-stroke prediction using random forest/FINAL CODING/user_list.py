import sys
import home as home
import sqlite3
import pandas as pd
from tkinter import messagebox

connection = sqlite3.connect('patient_data.db')
c = connection.cursor()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.deleteVar = None
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 12"
        fontTitle= "-family {Segoe UI} -size 14"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1200x700+200+57")
        top.resizable(0, 0)
        top.title("Stroke Risk Prediction System")
        top.configure(background="#d9d9d9")

        # define frame
        self.tableFrame = tk.Frame(top)
        self.deleteFrame = tk.Frame(top)

        self.frameList = [self.tableFrame, self.deleteFrame]
        for frame in self.frameList:
            frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
            frame.configure(background='#bddeff')

        self.style.configure('Treeview', font="TkDefaultFont")
        self.Scrolledtreeview_admin = ScrolledTreeView(self.tableFrame)
        self.Scrolledtreeview_admin.place(relx=0.038, rely=0.129, relheight=0.643
                                          , relwidth=0.917)
        self.Scrolledtreeview_admin.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7 Col8 Col9 Col10 Col11")
        # build_treeview_support starting.
        self.Scrolledtreeview_admin.heading("#0", text=" ", anchor="center")
        self.Scrolledtreeview_admin.column("#0", width="1", minwidth="1", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col1", text="patient's id", anchor="center")
        self.Scrolledtreeview_admin.column("Col1", width="96", minwidth="96", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col2", text="gender", anchor="center")
        self.Scrolledtreeview_admin.column("Col2", width="86", minwidth="86", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col3", text="age", anchor="center")
        self.Scrolledtreeview_admin.column("Col3", width="83", minwidth="83", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col4", text="hypertension", anchor="center")
        self.Scrolledtreeview_admin.column("Col4", width="103", minwidth="103", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col5", text="heart disease", anchor="center")
        self.Scrolledtreeview_admin.column("Col5", width="100", minwidth="100", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col6", text="ever married", anchor="center")
        self.Scrolledtreeview_admin.column("Col6", width="101", minwidth="101", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col7", text="work type", anchor="center")
        self.Scrolledtreeview_admin.column("Col7", width="96", minwidth="96", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col8", text="residence type", anchor="center")
        self.Scrolledtreeview_admin.column("Col8", width="112", minwidth="112", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col9", text="avg glucose lvl", anchor="center")
        self.Scrolledtreeview_admin.column("Col9", width="112", minwidth="112", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col10", text="bmi", anchor="center")
        self.Scrolledtreeview_admin.column("Col10", width="73", minwidth="73", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col11", text="smoking status", anchor="center")
        self.Scrolledtreeview_admin.column("Col11", width="108", minwidth="108", stretch="1", anchor="center")

        self.Label_tablePage = tk.Label(self.tableFrame)
        self.Label_tablePage.place(relx=0.433, rely=0.043, height=26, width=162)
        self.Label_tablePage.configure(background="#bddeff")
        self.Label_tablePage.configure(disabledforeground="#a3a3a3")
        self.Label_tablePage.configure(foreground="#000000")
        self.Label_tablePage.configure(font = fontTitle)
        self.Label_tablePage.configure(text='''Patient's Records''')

        self.Button_backtable = tk.Button(self.tableFrame)
        self.Button_backtable.place(relx=0.042, rely=0.814, height=40, width=60)
        self.Button_backtable.configure(activebackground="#ececec")
        self.Button_backtable.configure(activeforeground="#000000")
        self.Button_backtable.configure(background="#d9d9d9")
        self.Button_backtable.configure(disabledforeground="#a3a3a3")
        self.Button_backtable.configure(font=font9)
        self.Button_backtable.configure(foreground="#000000")
        self.Button_backtable.configure(highlightbackground="#d9d9d9")
        self.Button_backtable.configure(highlightcolor="black")
        self.Button_backtable.configure(pady="0")
        self.Button_backtable.configure(text='''Back''')
        self.Button_backtable.configure(command=self.backToMain)

        self.Button_delete = tk.Button(self.tableFrame)
        self.Button_delete.place(relx=0.383, rely=0.814, height=40
                                 , width=200)
        self.Button_delete.configure(activebackground="#ececec")
        self.Button_delete.configure(activeforeground="#000000")
        self.Button_delete.configure(background="#d9d9d9")
        self.Button_delete.configure(disabledforeground="#a3a3a3")
        self.Button_delete.configure(
            font="-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Button_delete.configure(foreground="#000000")
        self.Button_delete.configure(highlightbackground="#d9d9d9")
        self.Button_delete.configure(highlightcolor="black")
        self.Button_delete.configure(pady="0")
        self.Button_delete.configure(text='''Delete''')
        self.Button_delete.configure(command=self.delete)

        # query the data
        c.execute("SELECT *, oid FROM patient_data")
        records = c.fetchall()

        for i in records:
            self.Scrolledtreeview_admin.insert("", "end", text="",
                                               values=(
                                                   i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))

        cc = pd.read_sql("SELECT * FROM patient_data", connection)
        cc.to_csv("user_dataRecord.csv", index=False)

        self.deleteVar = tk.StringVar()


        try:
            # list data to be delete
            idList = []
            c.execute("""SELECT id,gender FROM patient_data""")
            myresults2 = c.fetchall()
            for i in myresults2:
                # name = str(i[0])+"_"+ str(i[1])
                idList.append(i[0])
            searchOM = tk.OptionMenu(self.tableFrame, self.deleteVar, *idList)
            # searchOM.grid(row=10, column=2)
            searchOM.place(relx=0.300, rely=0.820)
        except:
            print("error2")

        self.raiseFrame1(self.tableFrame)


    def raiseFrame1(self, frame):
        frame.tkraise()

    def backToMain(self):
        root.destroy()
        home.vp_start_gui()

    # def to_deletePage(self):
    #     idList = []
    #     c.execute("""SELECT id,gender FROM patient_data""")
    #     myresults2 = c.fetchall()
    #     for i in myresults2:
    #         # name = str(i[0])+"_"+ str(i[1])
    #         idList.append(i[0])
    #     if len(idList) == 0:
    #         print("zero")
    #     else:
    #         self.deleteFrame.tkraise()

    def delete(self):
        idList = []
        c.execute("""SELECT id,gender FROM patient_data""")
        myresults2 = c.fetchall()
        for i in myresults2:
            idList.append(i[0])
        if len(idList) == 0:
            print("nothing")
            messagebox.showinfo("zero data","No data to be delete.")
        else:
            id = self.deleteVar.get().split(" ")
            deleteSQL = """DELETE FROM patient_data WHERE id=?"""
            c.execute(deleteSQL, (id))

            c.execute("SELECT *, oid FROM patient_data")
            records = c.fetchall()
            for i in self.Scrolledtreeview_admin.get_children():
                self.Scrolledtreeview_admin.delete(i)
            for i in records:
                self.Scrolledtreeview_admin.insert("", "end", text="",
                                                   values=(
                                                   i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
            cc = pd.read_sql("SELECT * FROM patient_data", connection)
            cc.to_csv("user_dataRecord.csv", index=False)
            connection.commit()

            pass
            idList = []
            c.execute("""SELECT id,gender FROM patient_data""")
            myresults3 = c.fetchall()
            for i in myresults3:
                idList.append(i[0])
            searchOM1 = tk.OptionMenu(self.tableFrame, self.deleteVar, *idList)
            searchOM1.place(relx=0.300, rely=0.820)




# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





