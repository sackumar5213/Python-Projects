from tkinter import*
from PIL import Image, ImageTk
import qrcode
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+130+30")
        self.root.title("QR Generator | Developed by Sachin")
        self.root.resizable(False,False)

        #=====TITLE==========
        title=Label(self.root,text="  QR Code Generator",font=("times new roman",40),bg="#053246",fg="#FFFFFF",anchor='w').place(x=0,y=0,relwidth=1)

        #=====Employee details window===========
        #=========Variables===========
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        #=====TITLE==========
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg="#043256",fg="#FFFFFF").place(x=0,y=0,relwidth=1)

        #======LABELS=========
        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("times new roman",15,'bold'),bg="#FFFFFF").place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Name",font=("times new roman",15,'bold'),bg="#FFFFFF").place(x=20,y=100)
        lbl_department=Label(emp_Frame,text="Department",font=("times new roman",15,'bold'),bg="#FFFFFF").place(x=20,y=140)
        lbl_designation=Label(emp_Frame,text="Designation",font=("times new roman",15,'bold'),bg="#FFFFFF").place(x=20,y=180)

        #=======ENTRY Feilds=========
        lbl_emp_code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_code,bg="lightyellow").place(x=200,y=60)
        lbl_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow").place(x=200,y=100)
        lbl_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_department,bg="lightyellow").place(x=200,y=140)
        lbl_designation=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow").place(x=200,y=180)

        #=====BUTTONS ============
        self.btn_generate=Button(emp_Frame,text='QR Generate',font=("times new roman",18,'bold'),bg="#2196F3",fg='white',cursor="hand2",command=self.generate)
        self.btn_generate.place(x=90, y=250, width=180, height=30)
        #emp_Frame.bind('<Return>'self.generate)
        btn_clear=Button(emp_Frame,text='Clear',font=("times new roman",18,'bold'),bg="#607d8b",fg='white',cursor="hand2",command=self.clear).place(x=282, y=250, width=120, height=30)
        

        #======Message Box==========
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20),bg="#FFFFFF",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #=========QR Code window===========
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        #=====QR Code TITLE==========
        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20),bg="#043256",fg="#FFFFFF").place(x=0,y=0,relwidth=1)

        #=====QR code Image======
        self.qr_code=Label(qr_Frame,text='No QR \nAvailabe',font=("times new roman",15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    #=========Clear Button Funtion================
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    #======Generate button Funtion=========
    def generate(self):
        if self.var_designation.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='':
            self.msg='All Fields are Required!!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name: {self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation: {self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("D:\python projects\Student QR code generator\Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            #============QR code image update=========
            self.im=ImageTk.PhotoImage(file="D:\python projects\Student QR code generator\Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)

            #=========Updating  Notification=============
            self.msg='QR Generated Successfully!!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
        
root=Tk()
obj=Qr_Generator(root)
root.mainloop()