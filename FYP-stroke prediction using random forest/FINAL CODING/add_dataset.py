import sys
import sqlite3
import pandas as pd
import home as h
import resultUi as result
from tkinter import messagebox

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

# Create database/connect to one
connection = sqlite3.connect('patient_data.db')

# Create cursor
c = connection.cursor()

# c.execute("""CREATE TABLE patient_data(
#             id  integer,
#             gender  text,
#             age integer,
#             hypertension    integer,
#             heart_disease   integer,
#             ever_married    text,
#             work_type   text,
#             Residence_type  text,
#             avg_glucose_level   float,
#             bmi float,
#             smoking_status  text
#             )""")


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

# def destroy_Toplevel1():
#     global w
#     w.destroy()
#     w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x800+444+20")
        top.resizable(0, 0)
        top.title("Stroke Risk Prediction System")
        top.configure(background="#bddeff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Labelframe_AddDataset = tk.LabelFrame(top)
        self.Labelframe_AddDataset.place(relx=0.013, rely=0.0, relheight=1.0
                , relwidth=0.975)
        self.Labelframe_AddDataset.configure(relief='groove')
        self.Labelframe_AddDataset.configure(foreground="black")
        self.Labelframe_AddDataset.configure(text='''Add Dataset''')
        self.Labelframe_AddDataset.configure(background="#bddeff")
        self.Labelframe_AddDataset.configure(highlightbackground="#d9d9d9")
        self.Labelframe_AddDataset.configure(highlightcolor="black")

        self.Label_AddDataset = tk.Label(self.Labelframe_AddDataset)
        self.Label_AddDataset.place(relx=0.256, rely=0.038, height=40, width=400
                , bordermode='ignore')
        self.Label_AddDataset.configure(activebackground="#f9f9f9")
        self.Label_AddDataset.configure(activeforeground="black")
        self.Label_AddDataset.configure(background="#bddeff")
        self.Label_AddDataset.configure(disabledforeground="#a3a3a3")
        self.Label_AddDataset.configure(font="-family {Segoe UI} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label_AddDataset.configure(foreground="#4444ff")
        self.Label_AddDataset.configure(highlightbackground="#d9d9d9")
        self.Label_AddDataset.configure(highlightcolor="black")
        self.Label_AddDataset.configure(text='''Stroke Risk Prediction Diagnosis''')

        self.Label_Patientid = tk.Label(self.Labelframe_AddDataset)
        self.Label_Patientid.place(relx=0.026, rely=0.113, height=52, width=100
                , bordermode='ignore')
        self.Label_Patientid.configure(activebackground="#f9f9f9")
        self.Label_Patientid.configure(activeforeground="black")
        self.Label_Patientid.configure(anchor='w')
        self.Label_Patientid.configure(background="#bddeff")
        self.Label_Patientid.configure(disabledforeground="#a3a3a3")
        self.Label_Patientid.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_Patientid.configure(foreground="#000000")
        self.Label_Patientid.configure(highlightbackground="#d9d9d9")
        self.Label_Patientid.configure(highlightcolor="black")
        self.Label_Patientid.configure(text='''Patient id''')

        self.Entry_id = tk.Entry(self.Labelframe_AddDataset)
        self.Entry_id.place(relx=0.192, rely=0.125, height=30, relwidth=0.192
                , bordermode='ignore')
        self.Entry_id.configure(background="white")
        self.Entry_id.configure(disabledforeground="#a3a3a3")
        self.Entry_id.configure(font="TkFixedFont")
        self.Entry_id.configure(foreground="#000000")
        self.Entry_id.configure(highlightbackground="#d9d9d9")
        self.Entry_id.configure(highlightcolor="black")
        self.Entry_id.configure(insertbackground="black")
        self.Entry_id.configure(selectbackground="blue")
        self.Entry_id.configure(selectforeground="white")

        self.Label_Gender = tk.Label(self.Labelframe_AddDataset)
        self.Label_Gender.place(relx=0.026, rely=0.188, height=52, width=100
                , bordermode='ignore')
        self.Label_Gender.configure(activebackground="#f9f9f9")
        self.Label_Gender.configure(activeforeground="black")
        self.Label_Gender.configure(anchor='w')
        self.Label_Gender.configure(background="#bddeff")
        self.Label_Gender.configure(disabledforeground="#a3a3a3")
        self.Label_Gender.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_Gender.configure(foreground="#000000")
        self.Label_Gender.configure(highlightbackground="#d9d9d9")
        self.Label_Gender.configure(highlightcolor="black")
        self.Label_Gender.configure(text='''Gender''')

        self.TCombobox_gender = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_gender.place(relx=0.192, rely=0.2, relheight=0.038
                , relwidth=0.192, bordermode='ignore')
        self.value_list = ['Select','Male','Female',]
        self.TCombobox_gender.configure(values=self.value_list)
        self.TCombobox_gender.configure(foreground="#000000")
        self.TCombobox_gender.configure(background="#000000")
        self.TCombobox_gender.configure(takefocus="")
        self.TCombobox_gender.configure(state='readonly')
        self.TCombobox_gender.current(0)

        self.Label_Age = tk.Label(self.Labelframe_AddDataset)
        self.Label_Age.place(relx=0.513, rely=0.188, height=52, width=100
                , bordermode='ignore')
        self.Label_Age.configure(activebackground="#f9f9f9")
        self.Label_Age.configure(activeforeground="black")
        self.Label_Age.configure(anchor='w')
        self.Label_Age.configure(background="#bddeff")
        self.Label_Age.configure(disabledforeground="#a3a3a3")
        self.Label_Age.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_Age.configure(foreground="#000000")
        self.Label_Age.configure(highlightbackground="#d9d9d9")
        self.Label_Age.configure(highlightcolor="black")
        self.Label_Age.configure(text='''Age''')

        self.Entry_age = tk.Entry(self.Labelframe_AddDataset)
        self.Entry_age.place(relx=0.744, rely=0.2, height=30, relwidth=0.192
                , bordermode='ignore')
        self.Entry_age.configure(background="white")
        self.Entry_age.configure(disabledforeground="#a3a3a3")
        self.Entry_age.configure(font="TkFixedFont")
        self.Entry_age.configure(foreground="#000000")
        self.Entry_age.configure(highlightbackground="#d9d9d9")
        self.Entry_age.configure(highlightcolor="black")
        self.Entry_age.configure(insertbackground="black")
        self.Entry_age.configure(selectbackground="blue")
        self.Entry_age.configure(selectforeground="white")

        self.Label_Hypertension = tk.Label(self.Labelframe_AddDataset)
        self.Label_Hypertension.place(relx=0.026, rely=0.263, height=52
                , width=100, bordermode='ignore')
        self.Label_Hypertension.configure(activebackground="#f9f9f9")
        self.Label_Hypertension.configure(activeforeground="black")
        self.Label_Hypertension.configure(anchor='w')
        self.Label_Hypertension.configure(background="#bddeff")
        self.Label_Hypertension.configure(disabledforeground="#a3a3a3")
        self.Label_Hypertension.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_Hypertension.configure(foreground="#000000")
        self.Label_Hypertension.configure(highlightbackground="#d9d9d9")
        self.Label_Hypertension.configure(highlightcolor="black")
        self.Label_Hypertension.configure(text='''Hypertension''')

        self.TCombobox_hypertension = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_hypertension.place(relx=0.192, rely=0.275, relheight=0.038
                                          , relwidth=0.192, bordermode='ignore')
        self.value_list1 = ['Select', 'No', 'Yes', ]
        self.TCombobox_hypertension.configure(values=self.value_list1)
        self.TCombobox_hypertension.configure(takefocus="")
        self.TCombobox_hypertension.configure(state='readonly')
        self.TCombobox_hypertension.current(0)

        self.Label_HeartDisease = tk.Label(self.Labelframe_AddDataset)
        self.Label_HeartDisease.place(relx=0.026, rely=0.338, height=52
                , width=120, bordermode='ignore')
        self.Label_HeartDisease.configure(activebackground="#f9f9f9")
        self.Label_HeartDisease.configure(activeforeground="black")
        self.Label_HeartDisease.configure(anchor='w')
        self.Label_HeartDisease.configure(background="#bddeff")
        self.Label_HeartDisease.configure(disabledforeground="#a3a3a3")
        self.Label_HeartDisease.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_HeartDisease.configure(foreground="#000000")
        self.Label_HeartDisease.configure(highlightbackground="#d9d9d9")
        self.Label_HeartDisease.configure(highlightcolor="black")
        self.Label_HeartDisease.configure(text='''Heart Disease''')

        self.TCombobox_HeartDisease = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_HeartDisease.place(relx=0.192, rely=0.35, relheight=0.039
                , relwidth=0.191, bordermode='ignore')
        self.value_list = ['Select','Yes','No',]
        self.TCombobox_HeartDisease.configure(values=self.value_list)
        self.TCombobox_HeartDisease.configure(foreground="#000000")
        self.TCombobox_HeartDisease.configure(background="#000000")
        self.TCombobox_HeartDisease.configure(takefocus="")
        self.TCombobox_HeartDisease.configure(state='readonly')
        self.TCombobox_HeartDisease.current(0)

        self.Label_everMarried = tk.Label(self.Labelframe_AddDataset)
        self.Label_everMarried.place(relx=0.026, rely=0.413, height=52, width=106
                                     , bordermode='ignore')
        self.Label_everMarried.configure(activebackground="#f9f9f9")
        self.Label_everMarried.configure(activeforeground="black")
        self.Label_everMarried.configure(anchor='w')
        self.Label_everMarried.configure(background="#bddeff")
        self.Label_everMarried.configure(cursor="fleur")
        self.Label_everMarried.configure(disabledforeground="#a3a3a3")
        self.Label_everMarried.configure(
            font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_everMarried.configure(foreground="#000000")
        self.Label_everMarried.configure(highlightbackground="#d9d9d9")
        self.Label_everMarried.configure(highlightcolor="black")
        self.Label_everMarried.configure(text='''Ever Married''')

        self.TCombobox_everMarried = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_everMarried.place(relx=0.192, rely=0.425, relheight=0.04
                                         , relwidth=0.191, bordermode='ignore')
        self.value_list = ['Select', 'No', 'Yes', ]
        self.TCombobox_everMarried.configure(values=self.value_list)
        self.TCombobox_everMarried.configure(takefocus="")
        self.TCombobox_everMarried.configure(state='readonly')
        self.TCombobox_everMarried.current(0)

        self.Label_WorkType = tk.Label(self.Labelframe_AddDataset)
        self.Label_WorkType.place(relx=0.513, rely=0.413, height=52, width=120
                                  , bordermode='ignore')
        self.Label_WorkType.configure(activebackground="#f9f9f9")
        self.Label_WorkType.configure(activeforeground="black")
        self.Label_WorkType.configure(anchor='w')
        self.Label_WorkType.configure(background="#bddeff")
        self.Label_WorkType.configure(disabledforeground="#a3a3a3")
        self.Label_WorkType.configure(
            font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_WorkType.configure(foreground="#000000")
        self.Label_WorkType.configure(highlightbackground="#d9d9d9")
        self.Label_WorkType.configure(highlightcolor="black")
        self.Label_WorkType.configure(text='''Work type''')

        self.TCombobox_WorkType = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_WorkType.place(relx=0.744, rely=0.425, relheight=0.04
                                      , relwidth=0.191, bordermode='ignore')
        self.value_list = ['Select', 'Self-employed', 'Govt_job', 'Private', 'children']
        self.TCombobox_WorkType.configure(values=self.value_list)
        self.TCombobox_WorkType.configure(foreground="#000000")
        self.TCombobox_WorkType.configure(background="#000000")
        self.TCombobox_WorkType.configure(takefocus="")
        self.TCombobox_WorkType.configure(state='readonly')
        self.TCombobox_WorkType.current(0)

        self.Label_ResidenceType = tk.Label(self.Labelframe_AddDataset)
        self.Label_ResidenceType.place(relx=0.026, rely=0.488, height=52
                                       , width=120, bordermode='ignore')
        self.Label_ResidenceType.configure(activebackground="#f9f9f9")
        self.Label_ResidenceType.configure(activeforeground="black")
        self.Label_ResidenceType.configure(anchor='w')
        self.Label_ResidenceType.configure(background="#bddeff")
        self.Label_ResidenceType.configure(cursor="fleur")
        self.Label_ResidenceType.configure(disabledforeground="#a3a3a3")
        self.Label_ResidenceType.configure(
            font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_ResidenceType.configure(foreground="#000000")
        self.Label_ResidenceType.configure(highlightbackground="#d9d9d9")
        self.Label_ResidenceType.configure(highlightcolor="black")
        self.Label_ResidenceType.configure(text='''Residence Type''')

        self.TCombobox_ResidenceType = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_ResidenceType.place(relx=0.192, rely=0.5, relheight=0.04
                                           , relwidth=0.191, bordermode='ignore')
        self.value_list = ['Select', 'Urban', 'Rural', ]
        self.TCombobox_ResidenceType.configure(values=self.value_list)
        self.TCombobox_ResidenceType.configure(takefocus="")
        self.TCombobox_ResidenceType.configure(state='readonly')
        self.TCombobox_ResidenceType.current(0)

        self.Label_GlucoseLvl = tk.Label(self.Labelframe_AddDataset)
        self.Label_GlucoseLvl.place(relx=0.513, rely=0.338, height=52, width=180
                                    , bordermode='ignore')
        self.Label_GlucoseLvl.configure(activebackground="#f9f9f9")
        self.Label_GlucoseLvl.configure(activeforeground="black")
        self.Label_GlucoseLvl.configure(anchor='w')
        self.Label_GlucoseLvl.configure(background="#bddeff")
        self.Label_GlucoseLvl.configure(disabledforeground="#a3a3a3")
        self.Label_GlucoseLvl.configure(
            font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_GlucoseLvl.configure(foreground="#000000")
        self.Label_GlucoseLvl.configure(highlightbackground="#d9d9d9")
        self.Label_GlucoseLvl.configure(highlightcolor="black")
        self.Label_GlucoseLvl.configure(text='''Average Glucose Level''')

        self.Entry_glucoseLvl = tk.Entry(self.Labelframe_AddDataset)
        self.Entry_glucoseLvl.place(relx=0.744, rely=0.35, height=30
                                    , relwidth=0.192, bordermode='ignore')
        self.Entry_glucoseLvl.configure(background="white")
        self.Entry_glucoseLvl.configure(cursor="xterm")
        self.Entry_glucoseLvl.configure(disabledforeground="#a3a3a3")
        self.Entry_glucoseLvl.configure(font="TkFixedFont")
        self.Entry_glucoseLvl.configure(foreground="#000000")
        self.Entry_glucoseLvl.configure(highlightbackground="#d9d9d9")
        self.Entry_glucoseLvl.configure(highlightcolor="black")
        self.Entry_glucoseLvl.configure(insertbackground="black")
        self.Entry_glucoseLvl.configure(selectbackground="blue")
        self.Entry_glucoseLvl.configure(selectforeground="white")

        self.Label_bmi = tk.Label(self.Labelframe_AddDataset)
        self.Label_bmi.place(relx=0.513, rely=0.263, height=52, width=120
                             , bordermode='ignore')
        self.Label_bmi.configure(activebackground="#f9f9f9")
        self.Label_bmi.configure(activeforeground="black")
        self.Label_bmi.configure(anchor='w')
        self.Label_bmi.configure(background="#bddeff")
        self.Label_bmi.configure(disabledforeground="#a3a3a3")
        self.Label_bmi.configure(font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_bmi.configure(foreground="#000000")
        self.Label_bmi.configure(highlightbackground="#d9d9d9")
        self.Label_bmi.configure(highlightcolor="black")
        self.Label_bmi.configure(text='''BMI''')

        self.Entry_bmi = tk.Entry(self.Labelframe_AddDataset)
        self.Entry_bmi.place(relx=0.744, rely=0.275, height=30, relwidth=0.192
                             , bordermode='ignore')
        self.Entry_bmi.configure(background="white")
        self.Entry_bmi.configure(disabledforeground="#a3a3a3")
        self.Entry_bmi.configure(font="TkFixedFont")
        self.Entry_bmi.configure(foreground="#000000")
        self.Entry_bmi.configure(highlightbackground="#d9d9d9")
        self.Entry_bmi.configure(highlightcolor="black")
        self.Entry_bmi.configure(insertbackground="black")
        self.Entry_bmi.configure(selectbackground="blue")
        self.Entry_bmi.configure(selectforeground="white")

        self.Label_SmokingStatus = tk.Label(self.Labelframe_AddDataset)
        self.Label_SmokingStatus.place(relx=0.513, rely=0.488, height=52
                                       , width=180, bordermode='ignore')
        self.Label_SmokingStatus.configure(activebackground="#f9f9f9")
        self.Label_SmokingStatus.configure(activeforeground="black")
        self.Label_SmokingStatus.configure(anchor='w')
        self.Label_SmokingStatus.configure(background="#bddeff")
        self.Label_SmokingStatus.configure(disabledforeground="#a3a3a3")
        self.Label_SmokingStatus.configure(
            font="-family Tahoma -size 10 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label_SmokingStatus.configure(foreground="#000000")
        self.Label_SmokingStatus.configure(highlightbackground="#d9d9d9")
        self.Label_SmokingStatus.configure(highlightcolor="black")
        self.Label_SmokingStatus.configure(text='''Smoking Status''')

        self.TCombobox_SmokingStatus = ttk.Combobox(self.Labelframe_AddDataset)
        self.TCombobox_SmokingStatus.place(relx=0.744, rely=0.5, relheight=0.04
                                           , relwidth=0.191, bordermode='ignore')
        self.value_list = ['Select', 'never smoked', 'formerly smoked', 'smokes', ]
        self.TCombobox_SmokingStatus.configure(values=self.value_list)
        self.TCombobox_SmokingStatus.configure(foreground="#000000")
        self.TCombobox_SmokingStatus.configure(background="#000000")
        self.TCombobox_SmokingStatus.configure(takefocus="")
        self.TCombobox_SmokingStatus.configure(state='readonly')
        self.TCombobox_SmokingStatus.current(0)

        self.ButtonBack = tk.Button(self.Labelframe_AddDataset)
        self.ButtonBack.place(relx=0.051, rely=0.713, height=33, width=67
                              , bordermode='ignore')
        self.ButtonBack.configure(activebackground="#ececec")
        self.ButtonBack.configure(activeforeground="#000000")
        self.ButtonBack.configure(background="#d9d9d9")
        self.ButtonBack.configure(disabledforeground="#a3a3a3")
        self.ButtonBack.configure(font=font10)
        self.ButtonBack.configure(foreground="#000000")
        self.ButtonBack.configure(highlightbackground="#d9d9d9")
        self.ButtonBack.configure(highlightcolor="black")
        self.ButtonBack.configure(pady="0")
        self.ButtonBack.configure(text='''Back''')
        self.ButtonBack.configure(command=self.b2main)

        self.Button_Submit = tk.Button(self.Labelframe_AddDataset)
        self.Button_Submit.place(relx=0.449, rely=0.638, height=40, width=100
                                 , bordermode='ignore')
        self.Button_Submit.configure(activebackground="#ececec")
        self.Button_Submit.configure(activeforeground="#000000")
        self.Button_Submit.configure(background="#d9d9d9")
        self.Button_Submit.configure(disabledforeground="#a3a3a3")
        self.Button_Submit.configure(font=font10)
        self.Button_Submit.configure(foreground="#000000")
        self.Button_Submit.configure(highlightbackground="#d9d9d9")
        self.Button_Submit.configure(highlightcolor="black")
        self.Button_Submit.configure(pady="0")
        self.Button_Submit.configure(text='''Submit''')
        self.Button_Submit.configure(command=lambda: self.submit())

        self.Button_check = tk.Button(self.Labelframe_AddDataset)
        self.Button_check.place(relx=0.41, rely=0.713, height=35, width=160
                                , bordermode='ignore')
        self.Button_check.configure(activebackground="#ececec")
        self.Button_check.configure(activeforeground="#000000")
        self.Button_check.configure(background="#d9d9d9")
        self.Button_check.configure(disabledforeground="#a3a3a3")
        self.Button_check.configure(font=font10)
        self.Button_check.configure(foreground="#000000")
        self.Button_check.configure(highlightbackground="#d9d9d9")
        self.Button_check.configure(highlightcolor="black")
        self.Button_check.configure(pady="0")
        self.Button_check.configure(text='''Check Stroke''')
        self.Button_check.configure(command=lambda: self.toResultUi())

    def database_get(self):
        # Insert data to table
        c.execute(
            "INSERT INTO patient_data VALUES(:id, :gender, :age, :hypertension, :heart_disease, :ever_married, "
                                            ":work_type, :Residence_type, :avg_glucose_level, :bmi, :smoking_status)",
            {
                'id': self.Entry_id.get(),
                'gender': self.TCombobox_gender.get(),
                'age': self.Entry_age.get(),
                'hypertension': self.a,
                'heart_disease': self.b,
                'ever_married': self.TCombobox_everMarried.get(),
                'work_type': self.TCombobox_WorkType.get(),
                'Residence_type': self.TCombobox_ResidenceType.get(),
                'avg_glucose_level': self.Entry_glucoseLvl.get(),
                'bmi': self.Entry_bmi.get(),
                'smoking_status': self.TCombobox_SmokingStatus.get()
            })
        
        # convert data into CSV file
        toCSV = pd.read_sql("SELECT * FROM patient_data", connection)
        toCSV.to_csv("user_dataRecord.csv", index=False)
        # Commit changes
        connection.commit()

        # Close connection
        # connection.close()

        # Clear the text after registered
        self.Entry_id.delete(0, tk.END)
        self.Entry_age.delete(0, tk.END)
        self.Entry_bmi.delete(0, tk.END)
        self.Entry_glucoseLvl.delete(0, tk.END)
        self.TCombobox_gender.current(0)
        self.TCombobox_hypertension.current(0)
        self.TCombobox_HeartDisease.current(0)
        self.TCombobox_everMarried.current(0)
        self.TCombobox_WorkType.current(0)
        self.TCombobox_ResidenceType.current(0)
        self.TCombobox_SmokingStatus.current(0)

    def errorSelect(self):
        messagebox.showwarning("selection", "please select any of the selection")

    def submit(self):
        if self.TCombobox_WorkType.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_ResidenceType.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_gender.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_everMarried.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_SmokingStatus.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_hypertension.get() == "Select":
            self.errorSelect()
        elif self.TCombobox_HeartDisease.get() == "Select":
            self.errorSelect()
        else:
            try:
                int(self.Entry_id.get())
                float(self.Entry_bmi.get())
                float(self.Entry_glucoseLvl.get())
                int(self.Entry_age.get())
                if self.TCombobox_HeartDisease.get() == "Yes":
                    self.b = int("1")
                if self.TCombobox_HeartDisease.get() == "No":
                    self.b = int("0")
                if self.TCombobox_hypertension.get() == "Yes":
                    self.a = int("1")
                if self.TCombobox_hypertension.get() == "No":
                    self.a = int("0")
                self.database_get()
                print("success")
                messagebox.showinfo("data register", "data successfully registered!")
            except ValueError:
                print("Please input entry in number")
                messagebox.showwarning("data register", "Please input entry in number")




    def queryTable(self):
        c.execute("SELECT *, oid FROM patient_data")
        records = c.fetchall()
        print(records)
        connection.commit()
        connection.close()

    def b2main(self):
        root.destroy()
        h.vp_start_gui()

    def toResultUi(self):
        root.destroy()
        result.vp_start_gui()


if __name__ == '__main__':
    vp_start_gui()








