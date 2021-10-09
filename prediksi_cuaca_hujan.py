import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from scipy import stats
from tkinter import *
import tkinter.messagebox

df=pd.read_csv('hujan.csv')
x=df[['Bulan','Suhu','Mendung']].values
y=df['Hujan'].values

model=LogisticRegression()
model.fit(x,y)
y_pred=model.predict(x)

print(model.predict(x))
print(y)

print(model.score(x,y))
print(f"""
Accuracy\t : {accuracy_score(y,y_pred)}
Precision Score\t : {precision_score(y,y_pred)}
Recall Score\t : {recall_score(y,y_pred)}
F1 Score\t : {f1_score(y,y_pred)}
""")

slope,intercept,r,p,std_err=stats.linregress(df['Bulan'],df['Suhu'])
def myfunc(x):
    return slope*x + intercept

mymodel=list(map(myfunc,df['Bulan']))

class Cuaca:
    def __init__(self,root):
        self.root=root
        self.Labell()
        self.Entryy()
        self.Buttonn()

    def Labell(self):
        label1=Label(self.root,text="Selamat Datang",fg='blue')
        label2=Label(self.root,text="Silahkan Isi Data Berikut",fg='blue')
        label3=Label(self.root,text='')
        label4=Label(self.root,text='')

        label1.grid(columnspan=3)#baris ke-1
        label2.grid(columnspan=3)#baris ke-2
        label3.grid(columnspan=3)#baris ke-3
        label4.grid(columnspan=3)#baris ke-4

        bulan=Label(self.root,text='Bulan')
        suhu=Label(self.root,text='Suhu')
        mendung=Label(self.root,text='Mendung')
        
        bulan.grid(row=5)
        suhu.grid(row=6)
        mendung.grid(row=7)
        
    def Entryy(self):
        self.entry1=Entry(self.root)
        self.entry2=Entry(self.root)
        self.entry3=Entry(self.root)
        
        self.entry1.grid(row=5,column=1)
        self.entry2.grid(row=6,column=1)
        self.entry3.grid(row=7,column=1)
        
    def Buttonn(self):
        label_kosong=Label(self.root,text='')
        label_kosong.grid(columnspan=3)#baris ke-8
        
        button=Button(self.root,text='Predict',padx=40,pady=20,bg='red',fg='white',command=self.Predict)
        button.grid(row=9,column=1)

        button_predict=Button(self.root,text='Grafik data hujan',padx=40,pady=20,bg='yellow',command=self.grafik)
        button_predict.grid(row=10,column=1)
        
    def Predict(self):
        baru=Tk()
        baru.configure(bg="#11aadd")
        a=model.predict([[int(self.entry1.get()),int(self.entry2.get()),bool(self.entry3.get())]])
        if a==1:
            label=Label(baru,text="Hujan")
            label.pack()

        else:
            label=Label(baru,text="Tidak Hujan")
            label.pack()

    def grafik(self):
        plt.scatter(df['Bulan'],df['Suhu'],c=df['Hujan'])
        plt.plot(df['Bulan'],mymodel)
        plt.show()

root=Tk()
if __name__=='__main__':
    Cuaca(root)
    root.mainloop()
