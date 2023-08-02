from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from sqlite3 import Error
import os
import sys
py = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'Photos/logo.ico')
        self.maxsize(500,500)
        self.minsize(500,500)
        self.title('Ajouter une voiture')
        carBrand = StringVar()  # Variable la marque de la voiture
        carNumber = StringVar()  # Variable pour le maticule de la voiture
        carStatus = StringVar()  # Variable pour le status d'une voiture
        carPhoto = StringVar()  # Variable pour le chemin du fichier image

        #uploading image
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
#verifying input
        def asi():
            if len(carBrand.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Class Roll Number")
            elif len(carNumber.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Student Name")
            elif len(carStatus.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Student Id")
            elif len(carPhoto.get()) < 1:
                messagebox.showinfo("Oop's", "Please Select a Image")
            else:
                try:
                    self.conn = sqlite3.connect('CarDatabase.db')
                    self.myCursor = self.conn.cursor()
                    request = self.myCursor.execute("Insert into Cars('carBrand','carNumber','carStatus','carPhoto') values (?,?,?,?)",[carBrand.get(),carNumber.get(),carStatus.get(),convertToBinaryData(carPhoto.get())])
                    self.conn.commit()
                    if request:
                        messagebox.showinfo("Done","Student Inserted Successfully")
                        ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                        if ask:
                            self.destroy()
                            os.system('%s %s' % (py, 'Add_Student.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showerror("Error","Something goes wrong")
                    self.myCursor.close()
                    self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")

        # label and input box
        label4 = Label(self, text='Ajouter une voiture', fg='green', font=('Roboto', 20, 'bold')).pack()
        lbl = Label(self, text='Marque de voiture:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=82)
        S_name = Entry(self, textvariable=carBrand, width=30).place(x=200, y=84)
        label = Label(self, text='Matricule de voiture:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=130)
        S_name = Entry(self, textvariable=carNumber, width=30).place(x=200, y=132)
        label5 = Label(self, text='Status de la voiture:', font=('Comic Scan Ms', 10, 'bold')).place(x=70, y=180)
        S_name = Entry(self, textvariable=carStatus, width=30).place(x=200, y=182)

        def fileDialog():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype = (("jpeg","*.jpg"),("png","*.png"),("All Files","*.*")))
            carPhoto.set(filename)
        label8 = Label(self,text="Upload image", font=('Comic Scan Ms', 10, 'bold')).place(x=70,y=330)
        upload_image = Entry(self,textvariable = carPhoto,width = 30).place(x=200,y=330)
        butt=Button(self,text="Browse",width=7,command=fileDialog).place(x=400,y=328)
        S_butt = Button(self, text="Submit",width = 15,command=asi).place(x=230, y=390)

Add().mainloop()