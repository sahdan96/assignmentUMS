import sys
from tkinter.messagebox import askyesno
from winsound import *
import Vector2 as Vec
import matrix2 as mat2
import matrix3by3 as mat3
import matrix4by4 as mat4
import about as ab
import main_menu as mm
import  series_transform as st
import CompositeTransform as ct
import Vector3d as Vec3
import rotation_3d as r3d

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
    top = New_Toplevel(root)
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", top.when_closing)
    PlaySound('OpeningSound.wav', SND_ASYNC)
    root.iconbitmap("icon.ico")
    root.mainloop()



w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
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
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family System -size 16 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 22 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font9 = "-family {Times New Roman} -size 13 -weight bold " \
                "-slant roman -underline 0 -overstrike 0"

        top.geometry("600x600+500+100")
        top.title("My Vector and Matrix Calculator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

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
        self.mode.add_command(
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

        self.allMatMenu.add_command(command=lambda: self.to_r3d(),
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

        self.trans_menu.add_command(command = lambda : self.to_st(),
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
                                 font=font9,
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
        self.Labelframe1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#000000")
        self.Labelframe1.configure(
            text='''CASIO                                                                                                         fx-570ES PLUS''')
        self.Labelframe1.configure(background="#c7f9f1")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=580)

        self.Entry1 = Entry(self.Labelframe1)
        self.Entry1.insert(0, "0")
        self.Entry1.place(relx=0.083, rely=0.067, height=50, relwidth=0.833
                          , bordermode='ignore')
        self.Entry1.configure(background="gray49")
        self.Entry1.configure(borderwidth="0")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=('system', '20' , 'bold'))
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.083, rely=0.15, height=50, width=500
                          , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="grey49")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=('system', '20' , 'bold'))
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify=CENTER)
        self.Label1.configure(relief=SUNKEN)
        self.Label1.configure(anchor = E)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.05, rely=0.283, height=70, width=90
                           , bordermode='ignore')
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''7''')
        self.Button1.configure(command=lambda: (self.buttontoDisplay('7'), self.clickSound()))


        self.Button2 = Button(self.Labelframe1)
        self.Button2.place(relx=0.233, rely=0.283, height=70, width=90
                           , bordermode='ignore')
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffffff")
        self.Button2.configure(borderwidth="5")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font10)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''8''')
        self.Button2.configure(command=lambda: (self.buttontoDisplay('8'), self.clickSound()))

        self.Button3 = Button(self.Labelframe1)
        self.Button3.place(relx=0.417, rely=0.283, height=70, width=90
                           , bordermode='ignore')
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ffffff")
        self.Button3.configure(borderwidth="5")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font10)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''9''')
        self.Button3.configure(command=lambda: (self.buttontoDisplay('9'), self.clickSound()))


        self.Button4 = Button(self.Labelframe1)
        self.Button4.place(relx=0.6, rely=0.283, height=70, width=90
                           , bordermode='ignore')
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="OrangeRed")
        self.Button4.configure(borderwidth="5")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font10)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''DEL''')
        self.Button4.configure(command= lambda: (self.delete(), self.clickSound()))

        self.Button5 = Button(self.Labelframe1)
        self.Button5.place(relx=0.783, rely=0.283, height=70, width=90
                           , bordermode='ignore')
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="OrangeRed")
        self.Button5.configure(borderwidth="5")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font10)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''AC''')
        self.Button5.configure(command = lambda: (self.clearAll(), self.clickSound()))


        self.Button6 = Button(self.Labelframe1)
        self.Button6.place(relx=0.05, rely=0.417, height=70, width=90
                           , bordermode='ignore')
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#ffffff")
        self.Button6.configure(borderwidth="5")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font10)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''4''')
        self.Button6.configure(command=lambda: (self.buttontoDisplay('4'), self.clickSound()))


        self.Button7 = Button(self.Labelframe1)
        self.Button7.place(relx=0.233, rely=0.417, height=70, width=90
                           , bordermode='ignore')
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#ffffff")
        self.Button7.configure(borderwidth="5")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font10)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''5''')
        self.Button7.configure(command=lambda: (self.buttontoDisplay('5'), self.clickSound()))


        self.Button8 = Button(self.Labelframe1)
        self.Button8.place(relx=0.417, rely=0.417, height=70, width=90
                           , bordermode='ignore')
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#ffffff")
        self.Button8.configure(borderwidth="5")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font10)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''6''')
        self.Button8.configure(command=lambda: (self.buttontoDisplay('6'), self.clickSound()))

        self.Button9 = Button(self.Labelframe1)
        self.Button9.place(relx=0.6, rely=0.417, height=70, width=90
                           , bordermode='ignore')
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="lemon chiffon")
        self.Button9.configure(borderwidth="5")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font=font10)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''*''')
        self.Button9.configure(command=lambda: (self.buttontoDisplay('*'), self.clickSound()))


        self.Button10 = Button(self.Labelframe1)
        self.Button10.place(relx=0.783, rely=0.417, height=70, width=90
                            , bordermode='ignore')
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="lemon chiffon")
        self.Button10.configure(borderwidth="5")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(font=font10)
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''/''')
        self.Button10.configure(command=lambda: (self.buttontoDisplay('/'), self.clickSound()))

        self.Button11 = Button(self.Labelframe1)
        self.Button11.place(relx=0.05, rely=0.55, height=70, width=90
                            , bordermode='ignore')
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#ffffff")
        self.Button11.configure(borderwidth="5")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(font=font10)
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''1''')
        self.Button11.configure(command=lambda: (self.buttontoDisplay('1'), self.clickSound()))


        self.Button12 = Button(self.Labelframe1)
        self.Button12.place(relx=0.233, rely=0.55, height=70, width=90
                            , bordermode='ignore')
        self.Button12.configure(activebackground="#d9d9d9")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#ffffff")
        self.Button12.configure(borderwidth="5")
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(font=font10)
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''2''')
        self.Button12.configure(command=lambda: (self.buttontoDisplay('2'), self.clickSound()))


        self.Button13 = Button(self.Labelframe1)
        self.Button13.place(relx=0.417, rely=0.55, height=70, width=90
                            , bordermode='ignore')
        self.Button13.configure(activebackground="#d9d9d9")
        self.Button13.configure(activeforeground="#000000")
        self.Button13.configure(background="#ffffff")
        self.Button13.configure(borderwidth="5")
        self.Button13.configure(disabledforeground="#a3a3a3")
        self.Button13.configure(font=font10)
        self.Button13.configure(foreground="#000000")
        self.Button13.configure(highlightbackground="#d9d9d9")
        self.Button13.configure(highlightcolor="black")
        self.Button13.configure(pady="0")
        self.Button13.configure(text='''3''')
        self.Button13.configure(command=lambda: (self.buttontoDisplay('3'), self.clickSound()))


        self.Button14 = Button(self.Labelframe1)
        self.Button14.place(relx=0.6, rely=0.55, height=70, width=90
                            , bordermode='ignore')
        self.Button14.configure(activebackground="#d9d9d9")
        self.Button14.configure(activeforeground="#000000")
        self.Button14.configure(background="lemon chiffon")
        self.Button14.configure(borderwidth="5")
        self.Button14.configure(disabledforeground="#a3a3a3")
        self.Button14.configure(font=font10)
        self.Button14.configure(foreground="#000000")
        self.Button14.configure(highlightbackground="#d9d9d9")
        self.Button14.configure(highlightcolor="black")
        self.Button14.configure(pady="0")
        self.Button14.configure(text='''+''')
        self.Button14.configure(command=lambda: (self.buttontoDisplay('+'), self.clickSound()))

        self.Button15 = Button(self.Labelframe1)
        self.Button15.place(relx=0.783, rely=0.55, height=70, width=90
                            , bordermode='ignore')
        self.Button15.configure(activebackground="#d9d9d9")
        self.Button15.configure(activeforeground="#000000")
        self.Button15.configure(background="lemon chiffon")
        self.Button15.configure(borderwidth="5")
        self.Button15.configure(disabledforeground="#a3a3a3")
        self.Button15.configure(font=font10)
        self.Button15.configure(foreground="#000000")
        self.Button15.configure(highlightbackground="#d9d9d9")
        self.Button15.configure(highlightcolor="black")
        self.Button15.configure(pady="0")
        self.Button15.configure(text='''-''')
        self.Button15.configure(command=lambda: (self.buttontoDisplay('-'), self.clickSound()))


        self.Button16 = Button(self.Labelframe1)
        self.Button16.place(relx=0.05, rely=0.683, height=70, width=90
                            , bordermode='ignore')
        self.Button16.configure(activebackground="#d9d9d9")
        self.Button16.configure(activeforeground="#000000")
        self.Button16.configure(background="#ffffff")
        self.Button16.configure(borderwidth="5")
        self.Button16.configure(disabledforeground="#a3a3a3")
        self.Button16.configure(font=font10)
        self.Button16.configure(foreground="#000000")
        self.Button16.configure(highlightbackground="#d9d9d9")
        self.Button16.configure(highlightcolor="black")
        self.Button16.configure(pady="0")
        self.Button16.configure(text='''0''')
        self.Button16.configure(command=lambda: (self.buttontoDisplay('0'), self.clickSound()))

        self.Button17 = Button(self.Labelframe1)
        self.Button17.place(relx=0.233, rely=0.683, height=70, width=90
                            , bordermode='ignore')
        self.Button17.configure(activebackground="#d9d9d9")
        self.Button17.configure(activeforeground="#000000")
        self.Button17.configure(background="#ffffff")
        self.Button17.configure(borderwidth="5")
        self.Button17.configure(disabledforeground="#a3a3a3")
        self.Button17.configure(font=font10)
        self.Button17.configure(foreground="#000000")
        self.Button17.configure(highlightbackground="#d9d9d9")
        self.Button17.configure(highlightcolor="black")
        self.Button17.configure(pady="0")
        self.Button17.configure(text='''.''')
        self.Button17.configure(command=lambda: (self.buttontoDisplay('.'), self.clickSound()))


        self.Button18 = Button(self.Labelframe1)
        self.Button18.place(relx=0.417, rely=0.683, height=70, width=90
                            , bordermode='ignore')
        self.Button18.configure(activebackground="#d9d9d9")
        self.Button18.configure(activeforeground="#000000")
        self.Button18.configure(background="black")
        self.Button18.configure(borderwidth="5")
        self.Button18.configure(disabledforeground="#a3a3a3")
        self.Button18.configure(font=font10)
        self.Button18.configure(foreground="white")
        self.Button18.configure(highlightbackground="#d9d9d9")
        self.Button18.configure(highlightcolor="black")
        self.Button18.configure(pady="0")
        self.Button18.configure(text='''(''')
        self.Button18.configure(command=lambda: (self.buttontoDisplay('('), self.clickSound()))

        self.Button19 = Button(self.Labelframe1)
        self.Button19.place(relx=0.6, rely=0.683, height=70, width=90
                            , bordermode='ignore')
        self.Button19.configure(activebackground="#d9d9d9")
        self.Button19.configure(activeforeground="#000000")
        self.Button19.configure(background="black")
        self.Button19.configure(borderwidth="5")
        self.Button19.configure(disabledforeground="#a3a3a3")
        self.Button19.configure(font=font10)
        self.Button19.configure(foreground="white")
        self.Button19.configure(highlightbackground="#d9d9d9")
        self.Button19.configure(highlightcolor="black")
        self.Button19.configure(pady="0")
        self.Button19.configure(text=''')''')
        self.Button19.configure(command=lambda: (self.buttontoDisplay(')'), self.clickSound()))


        self.Button20 = Button(self.Labelframe1)
        self.Button20.place(relx=0.783, rely=0.683, height=70, width=90
                            , bordermode='ignore')
        self.Button20.configure(activebackground="#d9d9d9")
        self.Button20.configure(activeforeground="#000000")
        self.Button20.configure(background="plum1")
        self.Button20.configure(borderwidth="5")
        self.Button20.configure(disabledforeground="#a3a3a3")
        self.Button20.configure(font=font10)
        self.Button20.configure(foreground="#000000")
        self.Button20.configure(highlightbackground="#d9d9d9")
        self.Button20.configure(highlightcolor="black")
        self.Button20.configure(pady="0")
        self.Button20.configure(text='''=''')
        self.Button20.configure(command=lambda:self.calculateAll())

    def buttontoDisplay(self, text):
        self.textInput = self.Entry1.get()
        self.textLength = len(self.textInput)
        if self.textInput == "0":
            self.replaceText(text)
        else:
            self.Entry1.insert(self.textLength, text)

    def replaceText(self, text):
        self.Entry1.delete(0, END)
        self.Entry1.insert(0, text)

    def calculateAll(self):
        self.expression = self.Entry1.get()

        try:
            self.result = eval(self.expression)
            self.Label1.configure(text=str(self.result))
        except:
            self.Label1.configure(text="Syntax Error")
            play = PlaySound('Suspense Strike.wav', SND_ASYNC)

    def delete(self):
        self.replaceText(self.Entry1.get()[0:-1])
        self.Label1.configure(text="")

    def clearAll(self):
        self.replaceText("0")
        self.Label1.configure(text ="")

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

    def to_r3d(self):
        root.destroy()
        r3d.vp_start_gui()

    def when_closing(self):
        if askyesno('My Vector and Matrix Calculator', 'Do you really want to quit?'):
            sys.exit()
        else:
            pass

    def clickSound(self):
        PlaySound('ClickSound.wav', SND_ASYNC)





if __name__ == '__main__':
    vp_start_gui()
