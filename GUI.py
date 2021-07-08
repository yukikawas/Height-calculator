import tkinter as tk
import tkinter.messagebox

def Calc():
    Height = MainWindowHeightEntry.get()
    if Height == '':
        MboxMessage = '请输入你的身高！'
        tk.messagebox.showinfo(title='怕不是来消遣我？',message=MboxMessage)
    else:
        MboxMessage = '你的身高为' + Height + 'cm!'
        tk.messagebox.showinfo(title='当当！',message=MboxMessage)

MainWindow = tk.Tk()
MainWindow.title('身高计算器')
MainWindow.geometry('300x250+500+300')

MainWindowLabelTitle = tk.Label(MainWindow, text='身高计算器')
MainWindowLabelInput = tk.Label(MainWindow, text='请输入你的身高')
MainWindowHeightEntry = tk.Entry(MainWindow,width=20)
MainWindowButton = tk.Button(MainWindow,text='计算！',command=Calc)

MainWindowLabelTitle.place(x=100,y=10)
MainWindowLabelInput.place(x=20,y=50)
MainWindowHeightEntry.place(x=110,y=50)
MainWindowButton.place(x=150,y=90)

MainWindow.mainloop()

