import sys
from winsound import *
import numpy as np
from math import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
import basicCalt as Cal
import Vector2 as Vec
import matrix2 as mat2
import matrix3by3 as mat3
import matrix4by4 as mat4
import  series_transform as st
import CompositeTransform as ct
import Vector3d as Vec3
import main_menu as mm
import about as ab

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    PlaySound(None, SND_PURGE)
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", top.when_closing)
    root.iconbitmap("icon.ico")
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.font13 = "-family {Courier New} -size 11 -weight normal -slant" \
                      " roman -underline 0 -overstrike 0"
        self.font10 = "-family {Courier New} -size 13 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.font11 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.font12 = "-family {Courier New} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.font9 = "-family {Segoe UI} -size 15 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("538x500+450+212")
        top.title("My Vector and Matrix Calculator")
        top.configure(background="linen")

        self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.mode = Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.mode,
                                 activebackground="#d9d9d9",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="Mode")
        self.mode.add_command(command=lambda: self.openBasicCal(),
                              activebackground="#d9d9d9",
                              activeforeground="#000000",
                              background="#d9d9d9",
                              font="TkMenuFont",
                              foreground="#000000",
                              label="Standard Calculator")

        self.allMatMenu = Menu(top, tearoff=0)
        self.mode.add_cascade(menu=self.allMatMenu,
                              activebackground="#d9d9d9",
                              activeforeground="#000000",
                              background="#d9d9d9",
                              font="TkMenuFont",
                              foreground="#000000",
                              label="Matrix Calculator")

        self.allMatMenu.add_command(command=lambda: self.to_2by2(),
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Matrix 2x2")

        self.allMatMenu.add_command(command=lambda: self.to_3by3(),
                                    activebackground="#d9d9d9",
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    font="TkMenuFont",
                                    foreground="#000000",
                                    label="Matrix 3x3")

        self.allMatMenu.add_command(command=lambda: self.to_4by4(),
                                    activebackground="#d9d9d9",
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    font="TkMenuFont",
                                    foreground="#000000",
                                    label="Matrix 4x4")

        self.allMatMenu.add_command(
                                    activebackground="#d9d9d9",
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    font="TkMenuFont",
                                    foreground="#000000",
                                    label="3D rotation")

        self.vector_menu = Menu(top, tearoff=0)
        self.mode.add_cascade(menu=self.vector_menu,
                              activebackground="#d9d9d9",
                              activeforeground="#000000",
                              background="#d9d9d9",
                              font="TkMenuFont",
                              foreground="#000000",
                              label="Vector Calculator")

        self.vector_menu.add_command(command=lambda: self.openVector(),
                                     activebackground="#d9d9d9",
                                     activeforeground="#000000",
                                     background="#d9d9d9",
                                     font="TkMenuFont",
                                     foreground="#000000",
                                     label="2D vector")

        self.vector_menu.add_command(command=lambda: self.openVector3d(),
                                     activebackground="#d9d9d9",
                                     activeforeground="#000000",
                                     background="#d9d9d9",
                                     font="TkMenuFont",
                                     foreground="#000000",
                                     label="3D vector")

        self.trans_menu = Menu(top, tearoff=0)
        self.mode.add_cascade(menu=self.trans_menu,
                              activebackground="#d9d9d9",
                              activeforeground="#000000",
                              background="#d9d9d9",
                              font="TkMenuFont",
                              foreground="#000000",
                              label="Transformation")

        self.trans_menu.add_command(command=lambda: self.to_st(),
                                    activebackground="#d9d9d9",
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    font="TkMenuFont",
                                    foreground="#000000",
                                    label="series transformation")

        self.trans_menu.add_command(command=lambda: self.to_ct(),
                                    activebackground="#d9d9d9",
                                    activeforeground="#000000",
                                    background="#d9d9d9",
                                    font="TkMenuFont",
                                    foreground="#000000",
                                    label="composite transformation")

        self.menubar.add_command(command=lambda: self.openAbout(),
                                 activebackground="#d8d8d8",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="About")

        self.b2menu = Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.b2menu,
                                 activebackground="#d9d9d9",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="Navigate")

        self.b2menu.add_command(command=lambda: self.btoMain(),
                                activebackground="#d9d9d9",
                                activeforeground="#000000",
                                background="#d9d9d9",
                                font="TkMenuFont",
                                foreground="#000000",
                                label="back to main menu")

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.037, rely=0.02, relheight=0.96
                , relwidth=0.929)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=self.font9)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(labelanchor="n")
        self.Labelframe1.configure(text='''3D rotation''')
        self.Labelframe1.configure(background="khaki1")
        self.Labelframe1.configure(width=500)

        self.Entry1 = Entry(self.Labelframe1)
        self.Entry1.place(relx=0.08, rely=0.083, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=self.font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(justify=CENTER)

        self.Entry2 = Entry(self.Labelframe1)
        self.Entry2.place(relx=0.18, rely=0.083, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=self.font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(justify=CENTER)
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Entry3 = Entry(self.Labelframe1)
        self.Entry3.place(relx=0.28, rely=0.083, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=self.font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(justify=CENTER)
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Entry4 = Entry(self.Labelframe1)
        self.Entry4.place(relx=0.08, rely=0.188, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=self.font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(justify=CENTER)
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Entry5 = Entry(self.Labelframe1)
        self.Entry5.place(relx=0.18, rely=0.188, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=self.font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(justify=CENTER)
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.Entry6 = Entry(self.Labelframe1)
        self.Entry6.place(relx=0.28, rely=0.188, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=self.font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(justify=CENTER)
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Entry7 = Entry(self.Labelframe1)
        self.Entry7.place(relx=0.08, rely=0.292, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font=self.font10)
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(justify=CENTER)
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")

        self.Entry8 = Entry(self.Labelframe1)
        self.Entry8.place(relx=0.18, rely=0.292, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font=self.font10)
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(justify=CENTER)
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(selectforeground="black")

        self.Entry9 = Entry(self.Labelframe1)
        self.Entry9.place(relx=0.28, rely=0.292, height=40, relwidth=0.08
                , bordermode='ignore')
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font=self.font10)
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(justify=CENTER)
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")

        self.TCombobox1 = ttk.Combobox(self.Labelframe1)
        self.TCombobox1.place(relx=0.45, rely=0.104, relheight=0.063, relwidth=0.36
                , bordermode='ignore')
        self.value_list = ["XYZ","XZY","YXZ","YZX","ZXY","ZYX",]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(font=self.font11)
        self.TCombobox1.configure(justify=CENTER)
        READONLY = 'readonly'
        self.TCombobox1.configure(state=READONLY)
        self.TCombobox1.configure(takefocus="")
        self.TCombobox1.set("choose rotation order")

        self.ButtonSelect = Button(self.Labelframe1)
        self.ButtonSelect.place(relx=0.84, rely=0.104, height=30, width=50
                , bordermode='ignore')
        self.ButtonSelect.configure(activebackground="#d9d9d9")
        self.ButtonSelect.configure(activeforeground="#000000")
        self.ButtonSelect.configure(background="#d9d9d9")
        self.ButtonSelect.configure(disabledforeground="#a3a3a3")
        self.ButtonSelect.configure(foreground="#000000")
        self.ButtonSelect.configure(highlightbackground="#d9d9d9")
        self.ButtonSelect.configure(highlightcolor="black")
        self.ButtonSelect.configure(pady="0")
        self.ButtonSelect.configure(text='''select''')
        self.ButtonSelect.configure(command =self.selection)

        self.Answerbox = Label(self.Labelframe1)
        self.Answerbox.place(relx=0.25, rely=0.479, height=180, width=240
                , bordermode='ignore')
        self.Answerbox.configure(background="cyan")
        self.Answerbox.configure(disabledforeground="#a3a3a3")
        self.Answerbox.configure(font=self.font12)
        self.Answerbox.configure(foreground="#000000")
        self.Answerbox.configure(width=272)

        self.ButtonClear = Button(self.Labelframe1)
        self.ButtonClear.place(relx=0.78, rely=0.835, height=30, width=85
                               , bordermode='ignore')
        self.ButtonClear.configure(activebackground="#d9d9d9")
        self.ButtonClear.configure(activeforeground="#000000")
        self.ButtonClear.configure(background="#d9d9d9")
        self.ButtonClear.configure(disabledforeground="#a3a3a3")
        self.ButtonClear.configure(font=self.font11)
        self.ButtonClear.configure(foreground="#000000")
        self.ButtonClear.configure(highlightbackground="#d9d9d9")
        self.ButtonClear.configure(highlightcolor="black")
        self.ButtonClear.configure(pady="0")
        self.ButtonClear.configure(text='''Clear All''')
        self.ButtonClear.configure(command = self.clearAll)



    def matrix(self):
        self.A = np.zeros((3,3))

        self.Entry = [[self.Entry1.get(), self.Entry2.get(), self.Entry3.get()], [self.Entry4.get(), self.Entry5.get(), self.Entry6.get()], [self.Entry7.get(), self.Entry8.get(), self.Entry9.get()]]
        for i in range(3):
            for j in range(3):
                self.A[i][j] = float(self.Entry[i][j])


    def selection(self):
        self.LabelX = Label(self.Labelframe1)
        self.LabelX.configure(background="khaki1")
        self.LabelX.configure(disabledforeground="#a3a3a3")
        self.LabelX.configure(font=self.font11)
        self.LabelX.configure(foreground="#000000")
        self.LabelX.configure(text='''X''')

        self.EntryX = Entry(self.Labelframe1)
        self.EntryX.configure(background="white")
        self.EntryX.configure(disabledforeground="#a3a3a3")
        self.EntryX.configure(font=self.font13)
        self.EntryX.configure(foreground="#000000")
        self.EntryX.configure(highlightbackground="#d9d9d9")
        self.EntryX.configure(highlightcolor="black")
        self.EntryX.configure(insertbackground="black")
        self.EntryX.configure(justify=CENTER)
        self.EntryX.configure(selectbackground="#c4c4c4")
        self.EntryX.configure(selectforeground="black")

        self.LabelY = Label(self.Labelframe1)
        self.LabelY.configure(activebackground="#f9f9f9")
        self.LabelY.configure(activeforeground="black")
        self.LabelY.configure(background="khaki1")
        self.LabelY.configure(disabledforeground="#a3a3a3")
        self.LabelY.configure(font=self.font11)
        self.LabelY.configure(foreground="#000000")
        self.LabelY.configure(highlightbackground="#d9d9d9")
        self.LabelY.configure(highlightcolor="black")
        self.LabelY.configure(text='''Y''')

        self.EntryY = Entry(self.Labelframe1)
        self.EntryY.configure(background="white")
        self.EntryY.configure(disabledforeground="#a3a3a3")
        self.EntryY.configure(font=self.font13)
        self.EntryY.configure(foreground="#000000")
        self.EntryY.configure(highlightbackground="#d9d9d9")
        self.EntryY.configure(highlightcolor="black")
        self.EntryY.configure(insertbackground="black")
        self.EntryY.configure(justify=CENTER)
        self.EntryY.configure(selectbackground="#c4c4c4")
        self.EntryY.configure(selectforeground="black")

        self.EntryZ = Entry(self.Labelframe1)
        self.EntryZ.configure(background="white")
        self.EntryZ.configure(disabledforeground="#a3a3a3")
        self.EntryZ.configure(font=self.font13)
        self.EntryZ.configure(foreground="#000000")
        self.EntryZ.configure(highlightbackground="#d9d9d9")
        self.EntryZ.configure(highlightcolor="black")
        self.EntryZ.configure(insertbackground="black")
        self.EntryZ.configure(justify=CENTER)
        self.EntryZ.configure(selectbackground="#c4c4c4")
        self.EntryZ.configure(selectforeground="black")

        self.LabelZ = Label(self.Labelframe1)
        self.LabelZ.configure(activebackground="#f9f9f9")
        self.LabelZ.configure(activeforeground="black")
        self.LabelZ.configure(background="khaki1")
        self.LabelZ.configure(disabledforeground="#a3a3a3")
        self.LabelZ.configure(font=self.font11)
        self.LabelZ.configure(foreground="#000000")
        self.LabelZ.configure(highlightbackground="#d9d9d9")
        self.LabelZ.configure(highlightcolor="black")
        self.LabelZ.configure(text='''Z''')

        self.LabelEATR = Label(self.Labelframe1)
        self.LabelEATR.place(relx=0.46, rely=0.198, height=26, width=212
                             , bordermode='ignore')
        self.LabelEATR.configure(background="khaki1")
        self.LabelEATR.configure(disabledforeground="#a3a3a3")
        self.LabelEATR.configure(font=self.font11)
        self.LabelEATR.configure(foreground="#000000")
        self.LabelEATR.configure(text='''enter angle to rotate:''')
        self.LabelEATR.configure(width=212)

        self.ButtonRotate = Button(self.Labelframe1)
        self.ButtonRotate.place(relx=0.64, rely=0.375, height=33, width=70
                                , bordermode='ignore')
        self.ButtonRotate.configure(activebackground="#d9d9d9")
        self.ButtonRotate.configure(activeforeground="#000000")
        self.ButtonRotate.configure(background="#d9d9d9")
        self.ButtonRotate.configure(disabledforeground="#a3a3a3")
        self.ButtonRotate.configure(font=self.font11)
        self.ButtonRotate.configure(foreground="#000000")
        self.ButtonRotate.configure(highlightbackground="#d9d9d9")
        self.ButtonRotate.configure(highlightcolor="black")
        self.ButtonRotate.configure(pady="0")
        self.ButtonRotate.configure(text='''rotate''')
        self.ButtonRotate.configure(command = self.operate)


        if self.TCombobox1.get()=="XYZ":
            self.LabelX.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelY.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelZ.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        elif self.TCombobox1.get()=="XZY":
            self.LabelX.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelZ.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelY.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        elif self.TCombobox1.get()=="YXZ":
            self.LabelY.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelX.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelZ.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        elif self.TCombobox1.get()=="YZX":
            self.LabelY.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelZ.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelX.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        elif self.TCombobox1.get()=="ZXY":
            self.LabelZ.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelX.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelY.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        elif self.TCombobox1.get()=="ZYX":
            self.LabelZ.place(relx=0.44, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryZ.place(relx=0.5, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelY.place(relx=0.6, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryY.place(relx=0.66, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
            self.LabelX.place(relx=0.76, rely=0.281, height=30, width=30
                              , bordermode='ignore')
            self.EntryX.place(relx=0.82, rely=0.271, height=40, relwidth=0.08
                              , bordermode='ignore')
        else:
            messagebox.showerror("error", "no selection selected")

    def getX(self):
        if float(self.EntryX.get())>90 or float(self.EntryX.get())<-90:
            messagebox.showinfo("Angle Limit", "According to General Rules Euler Angles, \nlimit pitch(x) is  ±90°.")
        else:
            thetax = radians(float(self.EntryX.get()))
            self.Rx = [[1, 0, 0], [0, cos(thetax), -sin(thetax)], [0, sin(thetax), cos(thetax)]]


    def getY(self):
        if float(self.EntryY.get())>180 or float(self.EntryY.get())<-180:
            messagebox.showinfo("Angle Limit", "According to General Rules Euler Angles, \nlimit yaw(y) is  ±180°.")
        else:
            thetay = radians(float(self.EntryY.get()))
            self.Ry = [[cos(thetay), 0, sin(thetay)], [0, 1, 0], [-sin(thetay), 0, cos(thetay)]]

    def getZ(self):
        if float(self.EntryZ.get())>180 or float(self.EntryZ.get())<-180:
            messagebox.showinfo("Angle Limit", "According to General Rules Euler Angles, \nlimit roll(z) is  ±180°.")
        else:
            thetaz = radians(float(self.EntryZ.get()))
            self.Rz = [[cos(thetaz), -sin(thetaz), 0], [sin(thetaz), cos(thetaz), 0], [0, 0, 1]]

    def operate(self):
        self.matrix(), self.getX(), self.getY(), self.getZ()
        if self.TCombobox1.get()=="XYZ":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Rx, self.Ry), self.Rz), self.A),2)
            self.Answerbox.configure(text = ans)
        elif self.TCombobox1.get()=="XZY":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Rx, self.Rz), self.Ry), self.A),2)
            self.Answerbox.configure(text = ans)
        elif self.TCombobox1.get()=="YXZ":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Ry, self.Rx), self.Rz), self.A),2)
            self.Answerbox.configure(text = ans)
        elif self.TCombobox1.get()=="YZX":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Ry, self.Rz), self.Rx), self.A),2)
            self.Answerbox.configure(text = ans)
        elif self.TCombobox1.get()=="ZXY":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Rz, self.Rx), self.Ry), self.A),2)
            self.Answerbox.configure(text = ans)
        elif self.TCombobox1.get()=="ZYX":
            ans = np.matrix.round(np.matmul(np.matmul(np.matmul(self.Rz, self.Ry), self.Rx), self.A),2)
            self.Answerbox.configure(text = ans)
        else:
            pass

    def clearAll(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)
        self.Entry7.delete(0, END)
        self.Entry8.delete(0, END)
        self.Entry9.delete(0, END)
        self.EntryX.delete(0, END)
        self.EntryY.delete(0, END)
        self.EntryZ.delete(0, END)
        self.Answerbox.configure(text ="")

    def openBasicCal(self):
        root.destroy()
        Cal.vp_start_gui()

    def openVector(self):
        root.destroy()
        Vec.vp_start_gui()

    def openVector3d(self):
        root.destroy()
        Vec3.vp_start_gui()

    def to_2by2(self):
        root.destroy()
        mat2.vp_start_gui()

    def to_3by3(self):
        root.destroy()
        mat3.vp_start_gui()

    def to_4by4(self):
        root.destroy()
        mat4.vp_start_gui()

    def openAbout(self):
        ab.vp_start_gui()

    def btoMain(self):
        root.destroy()
        mm.vp_start_gui()

    def to_st(self):
        root.destroy()
        st.vp_start_gui()

    def to_ct(self):
        root.destroy()
        ct.vp_start_gui()

    def when_closing(self):
        if askyesno('My Vector and Matrix Calculator', 'Do you really want to quit?'):
            sys.exit()
        else:
            pass




















if __name__ == '__main__':
    vp_start_gui()



