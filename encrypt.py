# --------------- @Hidden0612 --------------- #
from tkinter import *
from tkinter import filedialog
# ------------ #
win = Tk()
win.geometry("400x200")
win.title("Encrypt")
# ------------ #
def encrypt():
    pimg = filedialog.askopenfile(mode ='r' ,filetypes=(('jpg file','*.jpg'),('png file','*.png'),('jpeg file','*.jpeg')))

    if pimg is not None:
        file_img = pimg.name
        key = code_encrypt.get(1.0,END)
        print(file_img,key)
        f = open(file_img , 'rb')
        image = f.read()
        f.close()
        image = bytearray(image)
        try:
            for i,v in enumerate(image):
                image[i] = v^int(key)
            fi = open(file_img , 'wb')
            fi.write(image)
            fi.close()
            
            lb = Label(win,text='Successfull !',font=('arial',20),fg="green")
            lb.place(x = 140 , y = 160)
            
        except:
            lb = Label(win,text='Error Number !',font=('arial',16),fg="red")
            lb.place(x = 140 , y = 160)
            print('Error Number')

    
# ------------ #
btn = Button(win,text='Open',font=('arial',16),width=8 , height= 1 ,command=encrypt)
btn.place(x = 145 , y = 50)

# ------------ #
code_encrypt = Text(win,width=20, height= 1)
code_encrypt.place(x = 120 , y = 100)

# ------------ #



# ------------ #
win.mainloop()
