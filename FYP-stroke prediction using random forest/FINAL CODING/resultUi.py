import sys
import sqlite3
from tkinter import messagebox
import pandas as pd
import numpy as np
import home as h
from sklearn.preprocessing import LabelEncoder
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, auc, roc_auc_score, precision_score, recall_score, f1_score, roc_curve


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
    top = Toplevel (root)
    root.mainloop()

w = None
def create_Toplevel(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel (w)
    return (w, top)

def destroy_Toplevel():
    global w
    w.destroy()
    w = None

class Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font16 = "-family {Segoe UI} -size 13 -weight bold"
        font13 = "-family {Segoe UI} -size 11 -weight bold"

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x800+350+0")
        top.minsize(800, 800)
        top.maxsize(1924, 1055)
        top.resizable(0, 0)
        top.title("Stroke Risk Prediction System")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        render = tk.PhotoImage(file="result.png")
        img = tk.Label(top, image=render)
        img.image = render
        img.place(x=-3, y=-3)

        self.resultPatient_id = tk.Entry(top)
        self.resultPatient_id.place(relx=0.300, rely=0.160, height=30, relwidth=0.150
                , bordermode='ignore')
        self.resultPatient_id.configure(background="white")
        self.resultPatient_id.configure(disabledforeground="#a3a3a3")
        self.resultPatient_id.configure(font="TkFixedFont")
        self.resultPatient_id.configure(foreground="#000000")
        self.resultPatient_id.configure(highlightbackground="#d9d9d9")
        self.resultPatient_id.configure(highlightcolor="black")
        self.resultPatient_id.configure(insertbackground="black")
        self.resultPatient_id.configure(selectbackground="blue")
        self.resultPatient_id.configure(selectforeground="white")

        self.buttonCheck = tk.Button(top)
        self.buttonCheck.place(relx=0.500, rely=0.150, height=43, width=66)
        self.buttonCheck.configure(activebackground="#ececec")
        self.buttonCheck.configure(activeforeground="#000000")
        self.buttonCheck.configure(background="#d9d9d9")
        self.buttonCheck.configure(disabledforeground="#a3a3a3")
        self.buttonCheck.configure(foreground="#000000")
        self.buttonCheck.configure(highlightbackground="#d9d9d9")
        self.buttonCheck.configure(highlightcolor="black")
        self.buttonCheck.configure(pady="0")
        self.buttonCheck.configure(text='''check''')
        self.buttonCheck.configure(command=self.checkResult)

        # table
        self.style.configure('Treeview', font="TkDefaultFont")
        self.Scrolledtreeview_admin = ScrolledTreeView(top)
        self.Scrolledtreeview_admin.place(relx=0.020, rely=0.300, relheight=0.070
                                          , relwidth=0.955)
        self.Scrolledtreeview_admin.configure(columns="Col2 Col3 Col4 Col5 Col6 Col7 Col8 Col9 Col10 Col11")
        # build_treeview_support starting.
        self.Scrolledtreeview_admin.heading("#0", text=" ", anchor="center")
        self.Scrolledtreeview_admin.column("#0", width="1", minwidth="1", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col2", text="gender", anchor="center")
        self.Scrolledtreeview_admin.column("Col2", width="60", minwidth="60", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col3", text="age", anchor="center")
        self.Scrolledtreeview_admin.column("Col3", width="40", minwidth="40", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col4", text="hypertension", anchor="center")
        self.Scrolledtreeview_admin.column("Col4", width="80", minwidth="80", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col5", text="heart disease", anchor="center")
        self.Scrolledtreeview_admin.column("Col5", width="80", minwidth="80", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col6", text="ever married", anchor="center")
        self.Scrolledtreeview_admin.column("Col6", width="80", minwidth="80", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col7", text="work type", anchor="center")
        self.Scrolledtreeview_admin.column("Col7", width="70", minwidth="70", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col8", text="residence type", anchor="center")
        self.Scrolledtreeview_admin.column("Col8", width="85", minwidth="85", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col9", text="avg glucose lvl", anchor="center")
        self.Scrolledtreeview_admin.column("Col9", width="90", minwidth="90", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col10", text="bmi", anchor="center")
        self.Scrolledtreeview_admin.column("Col10", width="50", minwidth="50", stretch="1", anchor="center")
        self.Scrolledtreeview_admin.heading("Col11", text="smoking status", anchor="center")
        self.Scrolledtreeview_admin.column("Col11", width="90", minwidth="90", stretch="1", anchor="center")

        self.resultLabel = tk.Label(top)
        self.resultLabel.place(relx=0.230, rely=0.50, height=50, width=280)
        self.resultLabel.configure(activebackground="#f9f9f9")
        self.resultLabel.configure(activeforeground="black")
        self.resultLabel.configure(font=font16)
        self.resultLabel.configure(background="#87cefa")
        self.resultLabel.configure(disabledforeground="#a3a3a3")
        self.resultLabel.configure(foreground="#000000")
        self.resultLabel.configure(highlightbackground="#d9d9d9")
        self.resultLabel.configure(highlightcolor="black")
        self.resultLabel.configure(text='''Your Stroke Risk Probability is: ''')

        self.resultLabel_2 = tk.Label(top)
        self.resultLabel_2.place(relx=0.580, rely=0.50, height=50, width=100)
        self.resultLabel_2.configure(font=font16)
        self.resultLabel_2.configure(background="#ffffff")
        self.resultLabel_2.configure(foreground="#000000")
        self.resultLabel_2.configure(text=''' ''')

        # benchmarking_UI
        self.labelTitle = tk.LabelFrame(top)
        self.labelTitle.place(relx=0.1, rely=0.688, relheight=0.170
                , relwidth=0.759)
        self.labelTitle.configure(relief='groove')
        self.labelTitle.configure(foreground="black")
        self.labelTitle.configure(text='''Evaluation metrics''')
        self.labelTitle.configure(background="#87cefa")
        self.labelTitle.configure(font=font16)
        self.labelTitle.configure(highlightbackground="#d9d9d9")
        self.labelTitle.configure(highlightcolor="black")

        self.Label_accu = tk.Label(self.labelTitle)
        self.Label_accu.place(relx=0.22, rely=0.160, height=26, width=350
                , bordermode='ignore')
        self.Label_accu.configure(activebackground="#f9f9f9")
        self.Label_accu.configure(activeforeground="black")
        self.Label_accu.configure(anchor='sw')
        self.Label_accu.configure(background="#87cefa")
        self.Label_accu.configure(font=font13)
        self.Label_accu.configure(disabledforeground="#a3a3a3")
        self.Label_accu.configure(foreground="#000000")
        self.Label_accu.configure(highlightbackground="#d9d9d9")
        self.Label_accu.configure(highlightcolor="black")
        self.Label_accu.configure(text='''Accuracy\t\t:\t''')

        self.Label_pre = tk.Label(self.labelTitle)
        self.Label_pre.place(relx=0.22, rely=0.360, height=26, width=350
                , bordermode='ignore')
        self.Label_pre.configure(activebackground="#f9f9f9")
        self.Label_pre.configure(activeforeground="black")
        self.Label_pre.configure(anchor='sw')
        self.Label_pre.configure(background="#87cefa")
        self.Label_pre.configure(font=font13)
        self.Label_pre.configure(disabledforeground="#a3a3a3")
        self.Label_pre.configure(foreground="#000000")
        self.Label_pre.configure(highlightbackground="#d9d9d9")
        self.Label_pre.configure(highlightcolor="black")
        self.Label_pre.configure(text='''Precision\t\t:\t''')

        self.Label_recall = tk.Label(self.labelTitle)
        self.Label_recall.place(relx=0.22, rely=0.560, height=26, width=350
                , bordermode='ignore')
        self.Label_recall.configure(activebackground="#f9f9f9")
        self.Label_recall.configure(activeforeground="black")
        self.Label_recall.configure(anchor='sw')
        self.Label_recall.configure(background="#87cefa")
        self.Label_recall.configure(font=font13)
        self.Label_recall.configure(disabledforeground="#a3a3a3")
        self.Label_recall.configure(foreground="#000000")
        self.Label_recall.configure(highlightbackground="#d9d9d9")
        self.Label_recall.configure(highlightcolor="black")
        self.Label_recall.configure(text='''Recall\t\t:\t''')

        self.Label_f1 = tk.Label(self.labelTitle)
        self.Label_f1.place(relx=0.22, rely=0.760, height=26, width=350
                , bordermode='ignore')
        self.Label_f1.configure(activebackground="#f9f9f9")
        self.Label_f1.configure(activeforeground="black")
        self.Label_f1.configure(anchor='sw')
        self.Label_f1.configure(background="#87cefa")
        self.Label_f1.configure(font=font13)
        self.Label_f1.configure(disabledforeground="#a3a3a3")
        self.Label_f1.configure(foreground="#000000")
        self.Label_f1.configure(highlightbackground="#d9d9d9")
        self.Label_f1.configure(highlightcolor="black")
        self.Label_f1.configure(text='''F1 score\t\t:\t''')

        self.buttonBack = tk.Button(top)
        self.buttonBack.place(relx=0.020, rely=0.900, height=43, width=66)
        self.buttonBack.configure(activebackground="#ececec")
        self.buttonBack.configure(activeforeground="#000000")
        self.buttonBack.configure(background="#d9d9d9")
        self.buttonBack.configure(disabledforeground="#a3a3a3")
        self.buttonBack.configure(foreground="#000000")
        self.buttonBack.configure(highlightbackground="#d9d9d9")
        self.buttonBack.configure(highlightcolor="black")
        self.buttonBack.configure(pady="0")
        self.buttonBack.configure(text='''Back''')
        self.buttonBack.configure(command=self.b2main)

    def checkResult(self):
        id_input = int(self.resultPatient_id.get())
        connection = sqlite3.connect('patient_data.db')
        c = connection.cursor()
        c.execute("SELECT * FROM patient_data WHERE id=?", (id_input,))
        data = c.fetchall()
        self.Scrolledtreeview_admin.delete(*self.Scrolledtreeview_admin.get_children())
        for i in data:
            self.Scrolledtreeview_admin.insert("", "end", text="",
                                                   values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))



        data_path = 'train_2v.csv'
        path_test = 'user_dataRecord.csv'

        data = pd.read_csv(data_path)
        test = pd.read_csv(path_test)
        id_input = int(self.resultPatient_id.get())
        ids = test['id']
        if id_input in ids.values:
            test = test.loc[test['id'] == id_input]
            print(test)

            # fill na/nan values
            data['bmi'] = data['bmi'].fillna(data['bmi'].mean())

            # drop row with na/nan values
            data.dropna(axis=0, inplace=True)

            # drop id column
            data.drop(columns='id', inplace=True)

            # Encode target labels with value between 0 and n_classes-1 for categorical column
            encode_gender = LabelEncoder()
            encode_marry = LabelEncoder()
            encode_work = LabelEncoder()
            encode_residence = LabelEncoder()
            encode_smoking = LabelEncoder()
            data['gender'] = encode_gender.fit_transform(data['gender'])
            data['ever_married'] = encode_marry.fit_transform(data['ever_married'])
            data['work_type'] = encode_work.fit_transform(data['work_type'])
            data['Residence_type'] = encode_residence.fit_transform(data['Residence_type'])
            data['smoking_status'] = encode_smoking.fit_transform(data['smoking_status'])

            test['gender'] = encode_gender.transform(test['gender'])
            test['ever_married'] = encode_marry.transform(test['ever_married'])
            test['work_type'] = encode_work.transform(test['work_type'])
            test['Residence_type'] = encode_residence.transform(test['Residence_type'])
            test['smoking_status'] = encode_smoking.transform(test['smoking_status'])
            test.drop(columns='id', inplace=True)

            x = data.drop('stroke', axis=1)
            y = data.stroke

            X_train, X_test, y_train, y_test = train_test_split(x, y,
                                                                                test_size=0.2)

            rus = RandomUnderSampler(random_state=0)
            X_resampled_rus, Y_resampled_rus = rus.fit_resample(X_train, y_train)



            rf_model = RandomForestClassifier(bootstrap=True, max_depth=None,
                                              max_features='auto', max_leaf_nodes=None,
                                              min_impurity_decrease=0.0, min_impurity_split=None,
                                              min_samples_leaf=1, min_samples_split=2,
                                              min_weight_fraction_leaf=0.0,
                                              n_estimators=5, random_state=0,
                                              n_jobs=None, oob_score=False,
                                              verbose=0, warm_start=False)
            rf_model.fit(X_resampled_rus, Y_resampled_rus)

            y_predicted_rus = rf_model.predict(X_test)

            self.Label_accu.configure(text='''Accuracy\t\t:\t'''+str(accuracy_score(y_test, y_predicted_rus)))
            self.Label_pre.configure(text='''Precision\t\t:\t'''+str(precision_score(y_test, y_predicted_rus)))
            self.Label_recall.configure(text='''Recall\t\t:\t'''+str(recall_score(y_test, y_predicted_rus)))
            self.Label_f1.configure(text='''F1 Score\t\t:\t'''+str(f1_score(y_test, y_predicted_rus)))


            predicted_test = rf_model.predict_proba(test)[:,1]
            print(predicted_test[0])
            a = float(predicted_test[0])*100
            print(str(a)+"%")
            self.resultLabel_2.configure(text = str(a)+"%")
            # if predicted_test ==1:
            #     print("yes")
            #     self.resultLabel_2.configure(text="Yes")
            # else:
            #     print("no")
            #     self.resultLabel_2.configure(text="No")
        else:
            print('no data found')
            messagebox.showwarning("stroke prediction", "Please enter valid id to check!")
            self.resultLabel_2.configure(text=" ")

    def b2main(self):
        root.destroy()
        h.vp_start_gui()



class ScrolledTreeView(ttk.Treeview):
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)


if __name__ == '__main__':
    vp_start_gui()





