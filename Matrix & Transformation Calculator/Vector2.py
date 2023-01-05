import sys
from tkinter.messagebox import*
from winsound import*
import basicCalt as Cal
import matrix2 as mat2
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


from math import*

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Basic_CG_Calculator (root)
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", top.when_closing)
    PlaySound(None, SND_PURGE) #stop all sound,no sound for vector :(
    root.iconbitmap("icon.ico")
    root.mainloop()

w = None
def create_Basic_CG_Calculator(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Basic_CG_Calculator (w)
    return (w, top)

def destroy_Basic_CG_Calculator():
    global w
    w.destroy()
    w = None


class Basic_CG_Calculator:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 30 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 36 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font17 = "-family {Times New Roman} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font18 = "-family Tahoma -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x600+500+100")
        top.title("My Vector and Matrix Calculator")
        top.configure(background="orange")
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

        self.vector_menu.add_command(
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
        self.Labelframe1.place(relx=0.067, rely=0.0, relheight=0.408
                , relwidth=0.867)
        self.Labelframe1.configure(relief=RIDGE)
        self.Labelframe1.configure(font=font14)
        self.Labelframe1.configure(foreground="#4400ff")
        self.Labelframe1.configure(relief=RIDGE)
        self.Labelframe1.configure(text='''Enter your vector:''')
        self.Labelframe1.configure(background="#bababa")
        self.Labelframe1.configure(width=520)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.212, rely=0.204, height=30, width=50
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f0f0f0")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#bababa")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''v1=''')

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.308, rely=0.082, height=87, width=28
                , bordermode='ignore')
        self.Label2.configure(background="#bababa")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''(''')

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.5, rely=0.163, height=73, width=20
                , bordermode='ignore')
        self.Label3.configure(background="#bababa")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text=''',''')

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.673, rely=0.082, height=87, width=28
                , bordermode='ignore')
        self.Label4.configure(background="#bababa")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text=''')''')

        self.Entry1 = Entry(self.Labelframe1)
        self.Entry1.place(relx=0.365, rely=0.184, height=50, relwidth=0.135
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=44)
        self.Entry1.configure(justify=CENTER)

        self.Entry2 = Entry(self.Labelframe1)
        self.Entry2.place(relx=0.538, rely=0.184, height=50, relwidth=0.135
                , bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=44)
        self.Entry2.configure(justify=CENTER)

        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.212, rely=0.531, height=30, width=50
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f0f0f0")
        self.Label5.configure(activeforeground="#000000")
        self.Label5.configure(background="#bababa")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''v2=''')

        self.Label6 = Label(self.Labelframe1)
        self.Label6.place(relx=0.308, rely=0.408, height=87, width=28
                , bordermode='ignore')
        self.Label6.configure(background="#bababa")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font12)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''(''')

        self.Label7 = Label(self.Labelframe1)
        self.Label7.place(relx=0.5, rely=0.49, height=73, width=20
                , bordermode='ignore')
        self.Label7.configure(background="#bababa")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font11)
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text=''',''')

        self.Label8 = Label(self.Labelframe1)
        self.Label8.place(relx=0.673, rely=0.408, height=87, width=28
                , bordermode='ignore')
        self.Label8.configure(background="#bababa")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font12)
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text=''')''')
        self.Label8.configure(width=52)

        self.Entry3 = Entry(self.Labelframe1)
        self.Entry3.place(relx=0.365, rely=0.51, height=50, relwidth=0.135
                , bordermode='ignore')
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(justify=CENTER)

        self.Entry4 = Entry(self.Labelframe1)
        self.Entry4.place(relx=0.538, rely=0.51, height=50, relwidth=0.135
                , bordermode='ignore')
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(justify=CENTER)

        self.Label9 = Label(self.Labelframe1)
        self.Label9.place(relx=0.25, rely=0.776, height=34, width=97
                , bordermode='ignore')
        self.Label9.configure(background="#bababa")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font13)
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''scalar,k =''')

        self.Entry5 = Entry(self.Labelframe1)
        self.Entry5.place(relx=0.442, rely=0.776, height=40, relwidth=0.135
                , bordermode='ignore')
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(justify=CENTER)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.067, rely=0.417, relheight=0.358
                , relwidth=0.867)
        self.Labelframe2.configure(relief=RIDGE)
        self.Labelframe2.configure(borderwidth="3")
        self.Labelframe2.configure(font=font13)
        self.Labelframe2.configure(foreground="#4400ff")
        self.Labelframe2.configure(labelanchor="n")
        self.Labelframe2.configure(relief=RIDGE)
        self.Labelframe2.configure(text='''option''')
        self.Labelframe2.configure(background="#e0e0e0")
        self.Labelframe2.configure(width=520)

        self.Button1 = Button(self.Labelframe2)
        self.Button1.place(relx=0.106, rely=0.14, height=37, width=200
                , bordermode='ignore')
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="orange red")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font17)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Addition of v1 and v2''')
        self.Button1.configure(command = self.sum_v1_v2)

        self.Button2 = Button(self.Labelframe2)
        self.Button2.place(relx=0.51, rely=0.14, height=37, width=200
                , bordermode='ignore')
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="orange red")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font17)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Subtraction of v1 and v2''')
        self.Button2.configure(command=self.diff_v1_v2)

        self.Button3 = Button(self.Labelframe2)
        self.Button3.place(relx=0.038, rely=0.372, height=37, width=150
                , bordermode='ignore')
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="orange red")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font17)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Magnitude of v1''')
        self.Button3.configure(command = self.magnitude_v1)

        self.Button4 = Button(self.Labelframe2)
        self.Button4.place(relx=0.356, rely=0.372, height=37, width=150
                , bordermode='ignore')
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="orange red")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font17)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Magnitude of v2''')
        self.Button4.configure(command=self.magnitude_v2)

        self.Button5 = Button(self.Labelframe2)
        self.Button5.place(relx=0.663, rely=0.372, height=37, width=150
                , bordermode='ignore')
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="orange red")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font17)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Total Magnitude''')
        self.Button5.configure(command = self.total_mag)

        self.Button6 = Button(self.Labelframe2)
        self.Button6.place(relx=0.029, rely=0.558, height=37, width=240
                , bordermode='ignore')
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="orange red")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font17)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''scalar and v1 multiplication''')
        self.Button6.configure(command = self.scalar_v1)

        self.Button7 = Button(self.Labelframe2)
        self.Button7.place(relx=0.51, rely=0.558, height=37, width=240
                , bordermode='ignore')
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="orange red")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font17)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''scalar and v2 multiplication''')
        self.Button7.configure(command=self.scalar_v2)

        self.Button8 = Button(self.Labelframe2)
        self.Button8.place(relx=0.51, rely=0.767, height=37, width=220
                , bordermode='ignore')
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="orange red")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font17)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Angle between v1 and v2''')
        self.Button8.configure(command = self.angle_v1v2)

        self.Button9 = Button(self.Labelframe2)
        self.Button9.place(relx=0.067, rely=0.767, height=37, width=220
                , bordermode='ignore')
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="orange red")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(font=font17)
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(text='''Dot product of v1 and v 2''')
        self.Button9.configure(command = self.dotProduct)


        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.067, rely=0.783, relheight=0.192
                , relwidth=0.867)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(font=font13)
        self.Labelframe3.configure(foreground="#4400ff")
        self.Labelframe3.configure(labelanchor="n")
        self.Labelframe3.configure(text='''answer''')
        self.Labelframe3.configure(background="#efefef")
        self.Labelframe3.configure(width=460)

        self.Label10 = Label(self.Labelframe3)
        self.Label10.place(relx=0.0, rely=0.261, height=80, width=520
                           , bordermode='ignore')
        self.Label10.configure(activebackground="#f0f0f0")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#efefef")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font18)
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(width=120)

    def vector1_input(self):
        self.v1_x = float(self.Entry1.get())
        self.v1_y = float(self.Entry2.get())

    def vector2_input(self):
        self.v2_x = float(self.Entry3.get())
        self.v2_y = float(self.Entry4.get())

    def scalar_k_input(self):
        self.k = float(self.Entry5.get())

    def sum_v1_v2(self):
        self.vector1_input()
        self.vector2_input()
        ans1 = self.v1_x + self.v2_x
        ans2 = self.v1_y + self.v2_y
        self.Label10.configure(text="v =(" + str(ans1) + " , " + str(ans2) + ")")

    def diff_v1_v2(self):
        self.vector1_input()
        self.vector2_input()
        ans1 = self.v1_x - self.v2_x
        ans2 = self.v1_y - self.v2_y
        self.Label10.configure(text="v =(" + str(ans1) + " , " + str(ans2) + ")")

    def magnitude_v1(self):
        self.vector1_input()
        ans =round((self.v1_x**2+self.v1_y**2)**(1/2),2)
        self.Label10.configure(text= "the magnitude of v1 is " + str(ans))

    def magnitude_v2(self):
        self.vector2_input()
        ans = round((self.v2_x ** 2 + self.v2_y ** 2) ** (1 / 2), 2)
        self.Label10.configure(text="the magnitude of v2 is " + str(ans))

    def total_mag(self):
        self.vector1_input()
        self.vector2_input()
        ans = round((self.v1_x**2+self.v1_y**2)**(1/2)+(self.v2_x ** 2 + self.v2_y ** 2) ** (1 / 2),2)
        self.Label10.configure(text="the total magnitude of vector is " + str(ans))

    def scalar_v1(self):
        self.vector1_input()
        self.scalar_k_input()
        ans1 = self.k * self.v1_x
        ans2 = self.k * self.v1_y
        self.Label10.configure(text = "k×v1=("+str(ans1)+" , "+str(ans2)+")")

    def scalar_v2(self):
        self.vector1_input()
        self.scalar_k_input()
        ans1 = self.k * self.v2_x
        ans2 = self.k * self.v2_y
        self.Label10.configure(text = "k×v2=("+str(ans1)+" , "+str(ans2)+")")

    def dotProduct(self):
        self.vector1_input()
        self.vector2_input()
        dotProductAns = (self.v1_x * self.v2_x) + (self.v1_y * self.v2_y)
        self.Label10.configure(text="the dot product is "+str(dotProductAns))

    def angle_v1v2(self):
        self.vector1_input()
        self.vector2_input()
        dotProduct  =(self.v1_x*self.v2_x) + (self.v1_y*self.v2_y)
        magnitudeProduct = round(((self.v1_x**2+self.v1_y**2)**(1/2))*((self.v2_x ** 2 + self.v2_y ** 2) ** (1 / 2)),2)
        ans = degrees(acos(dotProduct / magnitudeProduct))
        self.Label10.configure(text="the angle between vector is "+str(round(ans,2))+"°")

    def openBasicCal(self):
        root.destroy()
        Cal.vp_start_gui()

    def to_2by2(self):
        root.destroy()
        mat2.vp_start_gui()

    def to_3by3(self):
        root.destroy()
        mat3.vp_start_gui()

    def to_4by4(self):
        root.destroy()
        mat4.vp_start_gui()

    def openVector3d(self):
        root.destroy()
        Vec3.vp_start_gui()

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



