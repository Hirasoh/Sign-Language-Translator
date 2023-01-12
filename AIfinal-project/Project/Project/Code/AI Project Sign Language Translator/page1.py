from tkinter import *

ws = Tk()
width=ws.winfo_screenwidth()
height=ws.winfo_screenheight()
ws.geometry("%dx%d" % (width, height))
ws.title('Sign Language Translator')

img=PhotoImage(file = "1.png")



# canvas= Canvas(ws,width=200, height= 100)
# canvas.pack(expand=True, fill= BOTH)
# canvas.create_image(0,0,image=img)

f = ("Times bold", 14)

def prevPage():
    ws.destroy()

def nextPage():
    ws.destroy()
    import sign

Label(ws,text='Sign Language Translator',font=('Helvetica',18,'bold'),bd=5,bg='#E5E4E2',width=35,fg='#232224',relief=GROOVE ).place(x=410,y=20)

Label(ws,text='Developers:',font=('Helvetica',18,'bold'),bd=5,bg='#E5E4E2',width=25,fg='#232224',relief=GROOVE).place(x=490,y=180) 

Label(ws,
text=" Noor-ul-eman (2020-CE-33) \n Hareem Arshad (2020-CE-34) \n Hira Sohail (2020-CE-41) \n Palwasha Zulfiqar (2020-CE-48) \n ",
font=('Helvetica',15),bd=5,bg='#E5E4E2',width=26,fg='#232224',relief=GROOVE ).place(x=540,y=230)


Label(ws,text='Description of our project: ',font=('Helvetica',18,'bold'),bd=5,bg='#E5E4E2',width=35,fg='#232224',relief=GROOVE).place(x=410,y=420) 

Label(ws,
text="Sign language translation (SLT) bridge the communication \n  gap between deaf and hearing people. This  \n translator makes the interaction simpler and faster \n  for normal people to convey their ideas to hearing \n  impaired people.",
font=('Helvetica',11),bd=5,bg='#E5E4E2',width=50,fg='#232224',relief=GROOVE ).place(x=450,y=470)



Button(
    ws, 
    text="Start", 
    font=f,
    width=60,
    bg="#E5E4E2",
    command=nextPage,
    relief=GROOVE
    ).place(x=5,y=690)
    

Button(
    ws, 
    text="Exit", 
    font=f,
    width=60,
    bg="#E5E4E2",
    command=prevPage,
    relief=GROOVE
    ).place(x=680,y=690)

ws.mainloop()