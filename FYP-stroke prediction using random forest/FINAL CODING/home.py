import sys
import time
import user_list as tableAdmin
import add_dataset as addData
import resultUi as result

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

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 14"
        font11 = "-family {Segoe UI} -size 15"
        font15 = "-family {Segoe UI} -size 19 -weight bold"
        font16 = "-family {Segoe UI} -size 16 -weight bold"

        top.geometry("600x500+400+100")
        top.resizable(0, 0)
        top.title("Stroke Risk Prediction System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        # define frame
        self.mainFrame = tk.Frame(top)
        self.adminFrame = tk.Frame(top)
        self.userFrame = tk.Frame(top)

        self.frameList = [self.mainFrame, self.adminFrame, self.userFrame]
        for frame in self.frameList:
            frame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
            frame.configure(background='#bddeff')

        # main page
        render = tk.PhotoImage(file="mainGui.png")
        img = tk.Label(self.mainFrame, image=render)
        img.image = render
        img.place(x=-3, y=-3)

        self.Button_Admin = tk.Button(self.mainFrame)
        self.Button_Admin.place(relx=0.375, rely=0.526, height=40, width=150)
        self.Button_Admin.configure(activebackground="#ffff80")
        self.Button_Admin.configure(activeforeground="#0000ff")
        self.Button_Admin.configure(background="#d9d9d9")
        self.Button_Admin.configure(disabledforeground="#8000ff")
        self.Button_Admin.configure(font="-family {Microsoft Himalaya} -size 19 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button_Admin.configure(foreground="#0000ff")
        self.Button_Admin.configure(highlightbackground="#d9d9d9")
        self.Button_Admin.configure(highlightcolor="black")
        self.Button_Admin.configure(pady="0")
        self.Button_Admin.configure(text='''Admin Login''')
        self.Button_Admin.configure(command=self.to_admin)

        self.Button_User = tk.Button(self.mainFrame)
        self.Button_User.place(relx=0.375, rely=0.66, height=40, width=150)
        self.Button_User.configure(activebackground="#ffff80")
        self.Button_User.configure(activeforeground="#0000ff")
        self.Button_User.configure(background="#d9d9d9")
        self.Button_User.configure(disabledforeground="#8000ff")
        self.Button_User.configure(font="-family {Microsoft Himalaya} -size 19 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Button_User.configure(foreground="#0000ff")
        self.Button_User.configure(highlightbackground="#d9d9d9")
        self.Button_User.configure(highlightcolor="black")
        self.Button_User.configure(pady="0")
        self.Button_User.configure(text='''User Login''')
        self.Button_User.configure(command=self.to_user)

        # admin page
        adminBg = tk.PhotoImage(file="admin.png")
        img = tk.Label(self.adminFrame, image=adminBg)
        img.image = adminBg
        img.place(x=-3, y=-3)

        self.Entry_userAdmin = tk.Entry(self.adminFrame)
        self.Entry_userAdmin.place(relx=0.414, rely=0.265, height=35
                                   , relwidth=0.345, bordermode='ignore')
        self.Entry_userAdmin.configure(background="white")
        self.Entry_userAdmin.configure(disabledforeground="#a3a3a3")
        self.Entry_userAdmin.configure(font="TkFixedFont")
        self.Entry_userAdmin.configure(foreground="#000000")
        self.Entry_userAdmin.configure(insertbackground="black")

        self.Entry_passAdmin = tk.Entry(self.adminFrame)
        self.Entry_passAdmin.place(relx=0.414, rely=0.406, height=35
                                   , relwidth=0.345, bordermode='ignore')
        self.Entry_passAdmin.configure(background="white")
        self.Entry_passAdmin.configure(disabledforeground="#a3a3a3")
        self.Entry_passAdmin.configure(font="TkFixedFont")
        self.Entry_passAdmin.configure(foreground="#000000")
        self.Entry_passAdmin.configure(insertbackground="black")
        self.Entry_passAdmin.configure(show='*')

        self.Button_loginAdmin = tk.Button(self.adminFrame)
        self.Button_loginAdmin.place(relx=0.345, rely=0.667, height=50, width=200
                                     , bordermode='ignore')
        self.Button_loginAdmin.configure(activebackground="#ececec")
        self.Button_loginAdmin.configure(activeforeground="#000000")
        self.Button_loginAdmin.configure(background="#00ff00")
        self.Button_loginAdmin.configure(disabledforeground="#a3a3a3")
        self.Button_loginAdmin.configure(font=font15)
        self.Button_loginAdmin.configure(foreground="#ffffff")
        self.Button_loginAdmin.configure(highlightbackground="#d9d9d9")
        self.Button_loginAdmin.configure(highlightcolor="black")
        self.Button_loginAdmin.configure(pady="0")
        self.Button_loginAdmin.configure(text='''Login''')
        self.Button_loginAdmin.configure(command = self.adminValidate)

        self.Button_backA2M = tk.Button(self.adminFrame)
        self.Button_backA2M.place(relx=0.345, rely=0.792, height=50
                                       , width=200, bordermode='ignore')
        self.Button_backA2M.configure(activebackground="#ececec")
        self.Button_backA2M.configure(activeforeground="#000000")
        self.Button_backA2M.configure(background="#00ff00")
        self.Button_backA2M.configure(disabledforeground="#a3a3a3")
        self.Button_backA2M.configure(font=font16)
        self.Button_backA2M.configure(foreground="#ffffff")
        self.Button_backA2M.configure(highlightbackground="#d9d9d9")
        self.Button_backA2M.configure(highlightcolor="black")
        self.Button_backA2M.configure(pady="0")
        self.Button_backA2M.configure(text='''Back''')
        self.Button_backA2M.configure(command = self.backtoMain)

        self.Label_incorrectAdmin = tk.Label(self.adminFrame)
        self.Label_incorrectAdmin.place(relx=0.207, rely=0.542, height=36, width = 362, bordermode = 'ignore')
        self.Label_incorrectAdmin.configure(background="#bddeff")
        self.Label_incorrectAdmin.configure(disabledforeground="#a3a3a3")
        self.Label_incorrectAdmin.configure(font=font9)
        self.Label_incorrectAdmin.configure(foreground="#ff0000")

        # user page
        userBg = tk.PhotoImage(file="h1.png")
        img = tk.Label(self.userFrame, image=userBg)
        img.image = userBg
        img.place(x=-3, y=-3)

        self.Button_Register = tk.Button(self.userFrame)
        self.Button_Register.place(relx=0.353, rely=0.313, height=40, width=190
                                   , bordermode='ignore')
        self.Button_Register.configure(activebackground="#808000")
        self.Button_Register.configure(activeforeground="white")
        self.Button_Register.configure(activeforeground="#0000ff")
        self.Button_Register.configure(background="#ffff80")
        self.Button_Register.configure(disabledforeground="#a3a3a3")
        self.Button_Register.configure(font=font11)
        self.Button_Register.configure(foreground="#0000ff")
        self.Button_Register.configure(highlightbackground="#d9d9d9")
        self.Button_Register.configure(highlightcolor="black")
        self.Button_Register.configure(pady="0")
        self.Button_Register.configure(text='''Register Data''')
        self.Button_Register.configure(command=self.to_register)

        self.Button_CheckUser = tk.Button(self.userFrame)
        self.Button_CheckUser.place(relx=0.259, rely=0.438, height=40, width=300
                                    , bordermode='ignore')
        self.Button_CheckUser.configure(activebackground="#808000")
        self.Button_CheckUser.configure(activeforeground="white")
        self.Button_CheckUser.configure(activeforeground="#0000ff")
        self.Button_CheckUser.configure(background="#ffff80")
        self.Button_CheckUser.configure(disabledforeground="#a3a3a3")
        self.Button_CheckUser.configure(
            font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Button_CheckUser.configure(foreground="#0000ff")
        self.Button_CheckUser.configure(highlightbackground="#d9d9d9")
        self.Button_CheckUser.configure(highlightcolor="black")
        self.Button_CheckUser.configure(pady="0")
        self.Button_CheckUser.configure(text='''Check Stroke Prediction''')
        self.Button_CheckUser.configure(command=self.toResultUi)

        self.Button_BackUser = tk.Button(self.userFrame)
        self.Button_BackUser.place(relx=0.353, rely=0.563, height=40, width=190
                                   , bordermode='ignore')
        self.Button_BackUser.configure(activebackground="#808000")
        self.Button_BackUser.configure(activeforeground="white")
        self.Button_BackUser.configure(activeforeground="#0000ff")
        self.Button_BackUser.configure(background="#ffff80")
        self.Button_BackUser.configure(disabledforeground="#a3a3a3")
        self.Button_BackUser.configure(
            font="-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Button_BackUser.configure(foreground="#0000ff")
        self.Button_BackUser.configure(highlightbackground="#d9d9d9")
        self.Button_BackUser.configure(highlightcolor="black")
        self.Button_BackUser.configure(pady="0")
        self.Button_BackUser.configure(text='''Back''')
        self.Button_BackUser.configure(command=self.backtoMain)

        self.raiseFrame(self.mainFrame)

    def raiseFrame(self, frame):
        frame.tkraise()

    def to_admin(self):
        self.adminFrame.tkraise()

    def to_user(self):
        return self.userFrame.tkraise()

    def backtoMain(self):
        self.mainFrame.tkraise()

    def to_register(self):
        root.destroy()
        addData.vp_start_gui()

    def toResultUi(self):
        root.destroy()
        result.vp_start_gui()

    def adminValidate(self):
        username = 'Admin'
        password = 'Admin'
        if self.Entry_userAdmin.get() == username:
            if self.Entry_passAdmin.get() == password:
                root.destroy()
                tableAdmin.vp_start_gui()
            else:
                self.Label_incorrectAdmin.configure(text='''Incorrect password! Please try again.''')
                root.update()
                time.sleep(1)
                self.Label_incorrectAdmin.configure(text="")
        else:
            self.Label_incorrectAdmin.configure(text='''Incorrect Username! Please try again.''')
            root.update()
            time.sleep(1)
            self.Label_incorrectAdmin.configure(text="")

if __name__ == '__main__':
    vp_start_gui()






