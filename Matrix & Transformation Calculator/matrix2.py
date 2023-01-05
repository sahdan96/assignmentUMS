import sys
from tkinter.messagebox import askyesno
from tkinter import messagebox
from winsound import *
import Vector2 as Vec
import basicCalt as Cal
import matrix3by3 as mat3
import matrix4by4 as mat4
import about as ab
import main_menu as mm
import series_transform as st
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
    top = New_Toplevel (root)
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
        font10 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 10 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("600x600+500+100")
        top.title("My Vector and Matrix Calculator")

        self.bg = Label(top)
        self.bg.place(relx=0.0, rely=0.0)
        self._bg = PhotoImage(file="binary.png")
        self.bg.configure(image=self._bg)


        PlaySound('bgmusic.wav', SND_ASYNC )

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.mode = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.mode,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Mode")
        self.mode.add_command(command = lambda : self.openBasicCal(),
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Standard Calculator")

        self.allMatMenu = Menu(top, tearoff=0)
        self.mode.add_cascade(menu = self.allMatMenu,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Matrix Calculator")

        self.allMatMenu.add_command(
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Matrix 2x2")

        self.allMatMenu.add_command(command = lambda : self.to_3by3(),
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Matrix 3x3")

        self.allMatMenu.add_command(command = lambda : self.to_4by4(),
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

        self.menubar.add_command(command = lambda: self.openAbout(),
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

        self.b2menu.add_command(command = lambda : self.btoMain(),
            activebackground="#d9d9d9",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="back to main menu")

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.158, rely=0.1,height=50, relwidth=0.083)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(justify=CENTER)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.183, rely=0.033, height=26, width=62)
        self.Label1.configure(activebackground="#f0f0f0f0f0f0")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Matrix A''')

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.258, rely=0.1,height=50, relwidth=0.083)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(justify = CENTER)

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.158, rely=0.2,height=50, relwidth=0.083)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(justify=CENTER)

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.258, rely=0.2,height=50, relwidth=0.083)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(justify=CENTER)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.7, rely=0.033, height=26, width=61)
        self.Label2.configure(activebackground="#f0f0f0f0f0f0")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Matrix B''')

        self.Entry5 = Entry(top)
        self.Entry5.place(relx=0.658, rely=0.1,height=50, relwidth=0.083)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")
        self.Entry5.configure(justify=CENTER)

        self.Entry6 = Entry(top)
        self.Entry6.place(relx=0.758, rely=0.1,height=50, relwidth=0.083)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")
        self.Entry6.configure(justify=CENTER)

        self.Entry7 = Entry(top)
        self.Entry7.place(relx=0.658, rely=0.2,height=50, relwidth=0.083)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")
        self.Entry7.configure(justify=CENTER)

        self.Entry8 = Entry(top)
        self.Entry8.place(relx=0.758, rely=0.2,height=50, relwidth=0.083)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(selectforeground="black")
        self.Entry8.configure(justify=CENTER)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.45, rely=0.083, height=38, width=56)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''+''')
        self.Button1.configure(command = self.matSum)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.4, rely=0.158, height=35, width=56)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''A-B''')
        self.Button2.configure(command = self.matAminusB)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.392, rely=0.233, height=35, width=56)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''AxB''')
        self.Button3.configure(command = self.matAxB)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.392, rely=0.383, height=38, width=56)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''k x A''')
        self.Button4.configure(command = self.kxA)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.233, rely=0.467, height=40, width=155)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''determinant of A''')
        self.Button5.configure(command = self.detA)

        self.Button6 = Button(top)
        self.Button6.place(relx=0.342, rely=0.55, height=40, width=90)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font9)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''inverse A''')
        self.Button6.configure(command = self.inverseA)

        self.Entry9 = Entry(top)
        self.Entry9.place(relx=0.45, rely=0.317,height=34, relwidth=0.107)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")

        self.Label4 = Label(top)
        self.Label4.place(relx=0.267, rely=0.317, height=26, width=102)
        self.Label4.configure(activebackground="#f0f0f0")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''k constant''')

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.25, rely=0.667, relheight=0.25
                , relwidth=0.5)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font10)
        self.Labelframe1.configure(foreground="blue")
        self.Labelframe1.configure(text='''result''')
        self.Labelframe1.configure(background="tomato4")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=310)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.083, rely=0.2, height=110, width=250
                          , bordermode='ignore')
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=("Segoe UI", 15))
        self.Label3.configure(foreground="#000000")

        self.Button7 = Button(top)
        self.Button7.place(relx=0.508, rely=0.233, height=35, width=56)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font9)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''BxA''')
        self.Button7.configure(command = self.matBxA)

        self.Button8 = Button(top)
        self.Button8.place(relx=0.508, rely=0.383, height=38, width=56)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font9)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''k x B''')
        self.Button8.configure(command = self.kxB)

        self.Button9 = Button(top)
        self.Button9.place(relx=0.508, rely=0.467, height=40, width=155)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font=font9)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''determinant of B''')
        self.Button9.configure(command = self.detB)

        self.Button10 = Button(top)
        self.Button10.place(relx=0.508, rely=0.55, height=40, width=90)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(font=font9)
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")
        self.Button10.configure(pady="0")
        self.Button10.configure(text='''inverse B''')
        self.Button10.configure(command = self.inverseB)

        self.Button11 = Button(top)
        self.Button11.place(relx=0.508, rely=0.158, height=35, width=56)
        self.Button11.configure(activebackground="#d9d9d9")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(font=font9)
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''B-A''')
        self.Button11.configure(command = self.matBminusA)

    def getMatA(self):
        self.box1 = float(self.Entry1.get())
        self.box2 = float(self.Entry2.get())
        self.box3  = float(self.Entry3.get())
        self.box4 = float(self.Entry4.get())

    def getMatB(self):
        self.box5= float(self.Entry5.get())
        self.box6 = float(self.Entry6.get())
        self.box7 = float(self.Entry7.get())
        self.box8 = float(self.Entry8.get())

    def getK(self):
        self.k = float(self.Entry9.get())

    def matSum(self):
        self.getMatA()
        self.getMatB()
        ans1 = self.box1+ self.box5
        ans2 = self.box2 + self.box6
        ans3 = self.box3 + self.box7
        ans4 = self.box4 + self.box8
        self.Label3.configure(text= str(ans1)+"\t" +str(ans2)+"\n"+ str(ans3)+"\t" +str(ans4))


    def matAminusB(self):
        self.getMatA()
        self.getMatB()
        ans1 = self.box1 - self.box5
        ans2 = self.box2 - self.box6
        ans3 = self.box3 - self.box7
        ans4 = self.box4 - self.box8
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def matBminusA(self):
        self.getMatA()
        self.getMatB()
        ans1 = self.box5 - self.box1
        ans2 = self.box6 - self.box2
        ans3 = self.box7 - self.box3
        ans4 = self.box8 - self.box4
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def matAxB(self):
        self.getMatA()
        self.getMatB()
        ans1 = round((self.box1*self.box5)+(self.box2*self.box7),2)
        ans2 = round((self.box1 * self.box6) + (self.box2 * self.box8),2)
        ans3 = round((self.box3 * self.box5) + (self.box4 * self.box7),2)
        ans4 = round((self.box3 * self.box6) + (self.box4 * self.box8),2)
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def matBxA(self):
        self.getMatA()
        self.getMatB()
        ans1 = round((self.box5*self.box1)+(self.box6*self.box3),2)
        ans2 = round((self.box5 * self.box2) + (self.box6 * self.box4),2)
        ans3 = round((self.box7 * self.box1) + (self.box8 * self.box3),2)
        ans4 = round((self.box7 * self.box2) + (self.box8 * self.box4),2)
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def kxA(self):
        self.getMatA()
        self.getK()
        ans1 = self.k * self.box1
        ans2 = self.k * self.box2
        ans3 = self.k * self.box3
        ans4 = self.k * self.box4
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def kxB(self):
        self.getMatB()
        self.getK()
        ans1 = self.k * self.box5
        ans2 = self.k * self.box6
        ans3 = self.k * self.box7
        ans4 = self.k * self.box8
        self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))

    def detA(self):
        self.getMatA()
        ans=round((self.box1*self.box4)-(self.box2*self.box3),2)
        self.Label3.configure(text=str(ans) )


    def detB(self):
        self.getMatB()
        ans=(self.box5*self.box8)-(self.box6*self.box7)
        self.Label3.configure(text=str(ans))

    def inverseA(self):
        self.getMatA()
        det =(self.box1*self.box4)-(self.box2*self.box3)
        if(det !=0):
            ans1 = round((1 / det) * (self.box4), 2)
            ans2 = round((1 / det) * -(self.box2), 2)
            ans3 = round((1 / det) * -(self.box3), 2)
            ans4 = round((1 / det) * (self.box1), 2)
            self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))
        else :
            messagebox.showinfo("error", "The determinant is 0, the matrix is not invertible.")

    def inverseB(self):
        self.getMatB()
        det = (self.box5 * self.box8) - (self.box6 * self.box7)
        if (det != 0):
            ans1 = round((1 / det) * (self.box8), 2)
            ans2 = round((1 / det) * -(self.box6), 2)
            ans3 = round((1 / det) * -(self.box7), 2)
            ans4 = round((1 / det) * (self.box5), 2)
            self.Label3.configure(text=str(ans1) + "\t" + str(ans2) + "\n" + str(ans3) + "\t" + str(ans4))
        else:
            messagebox.showinfo("error", "The determinant is 0, the matrix is not invertible.")

    def openBasicCal(self):
        root.destroy()
        Cal.vp_start_gui()

    def openVector(self):
        root.destroy()
        Vec.vp_start_gui()

    def openVector3d(self):
        root.destroy()
        Vec3.vp_start_gui()

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

if __name__ == '__main__':
    vp_start_gui()






