from tkinter import *
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog
import mediapipe as mp
import pyttsx3


win = Tk()
width=win.winfo_screenwidth()
height=win.winfo_screenheight()

global img,finalImage,finger_tips,thumb_tip,cap,mylabel1, image, rgb, hand, results, _, w, h,status,mpDraw,mpHands,hands,label1,frame_1,btn,btn2
win.geometry("%dx%d" % (width, height))
frame_1 = Frame(win, width=width, height=height, bg="#232224").place(x=0, y=0)
win.title('Sign Language Converter')
mylabel1= Label(win,text='Sign Language Converter',font=('Helvetica',24,'bold'),bd=5,bg='gray',fg='#232224',relief=GROOVE,width=5000 ).pack(pady=15,padx=300)


#####################################Initiate###################################################
def wine():
    global finger_tips,thumb_tip,mpDraw,mpHands,cap,w,h,hands,label1,frame_1,check,img
   

    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    w = 500
    h = 300
    label1 = Label(win, width=w, height=h,bg="#232224") #video on 
    label1.place(x=150, y=200)

    # First step is to initialize the Hands class and store it in a variable
    mpHands = mp.solutions.hands  
    # Now second step is to set the hands function which will hold the landmarks points
    hands = mpHands.Hands()  
    # Last step is to set up the drawing function of hands landmarks on the image
    mpDraw = mp.solutions.drawing_utils
    # Video capture 
    cap = cv2.VideoCapture(0)
    


###########################################Detection##########################################
def live():
    global v
    global upCount
    global cshow,img
    cshow=0
    upCount = StringVar()#tkinter defined variable , efficiently 
    # global img, finalImage,engine, image, rgb, hand, results, _, w, h,upCount,status,mpDraw,mpHands,hands,label1
    
    _, img = cap.read()
    
    img = cv2.resize(img, (w, h))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)  # to identiify the hands in the image 
    # checking whether the hand is detected 
    if results.multi_hand_landmarks: 
        for hand in results.multi_hand_landmarks: # working with each hand 
            lm_list = []
            for id, lm in enumerate(hand.landmark):
                lm_list.append(lm)
            finger_fold_status = []

            for tip in finger_tips:
                # x, y are normalized values(range 0-1). So, simply scale dimensions to determine the pixel-based location 
                x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)  
                if lm_list[tip].x < lm_list[tip - 2].x:   
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)
            
            print(finger_fold_status)
            x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
            print(x, y)
            # stop
            if lm_list[4].y < lm_list[2].y and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
    	                      lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                    lm_list[5].x:
                cshow = 'STOP ! Dont move.'
                upCount.set('STOP ! Dont move.')
                print('STOP ! Dont move.')
            # okay
            elif lm_list[4].y < lm_list[2].y and lm_list[8].y > lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                    lm_list[5].x:
                cshow = 'Perfect , You did  a great job.'
                print('Perfect , You did  a great job.')
                upCount.set('Perfect , You did  a great job.')
               
            # spidey
            elif lm_list[4].y < lm_list[2].y and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                    lm_list[5].x:
                cshow = 'Good to see you.'
                print(' Good to see you. ')
                upCount.set('Good to see you.')
                
            # Point
            elif lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                upCount.set('You Come here.')
                print("You Come here.")
                cshow = 'You Come here.'
            # Victory
            elif lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                upCount.set('Yes , we won.')
                print("Yes , we won.")
                cshow = 'Yes , we won.'
            # Left
            elif lm_list[4].y < lm_list[2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                    lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[5].x < lm_list[0].x:
                upCount.set('Move Left')
                print(" MOVE LEFT")
                cshow = 'Move Left'
            # Right
            elif lm_list[4].y < lm_list[2].y and lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and \
                    lm_list[16].x < lm_list[14].x and lm_list[20].x < lm_list[18].x:
                upCount.set('Move Right')
                print("Move RIGHT")
                cshow = 'Move Right'
            if all(finger_fold_status):
                # like
                if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and lm_list[0].x < lm_list[3].y:
                    print("I like it")
                    upCount.set('I Like it')
                    cshow = 'I Like it'
                # Dislike
                elif lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y and lm_list[0].x < lm_list[3].y:
                    upCount.set('I dont like it.')
                    print(" I dont like it.")
                    cshow = 'I dont like it.'

            mpDraw.draw_landmarks(rgb, hand, mpHands.HAND_CONNECTIONS)
        cv2.putText(rgb, f'{cshow}', (10, 50),
                cv2.FONT_HERSHEY_COMPLEX, .75, (0, 255, 255), 2)



    image = Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    win.after(1, live)
    crr=Label(win,text='Current Status :',font=('Helvetica',18,'bold'),bd=5,bg='gray',width=15,fg='#232224',relief=GROOVE )
    status = Label(win,textvariable=upCount,font=('Helvetica',18,'bold'),bd=5,bg='gray',width=30,fg='#232224',relief=GROOVE )
  
    status.place(x=300,y=600)
    crr.place(x=20,y=600)
#################################################################################################

#####################################VOICE###############################################################################
# def voice():
    
#     engine = pyttsx3.init()
#     engine.say((upCount.get()))
#     engine.runAndWait()

def voice():
    # init function to get an engine instance for the speech synthesis (the process of generating spoken language by machine on the basis of written input ) 
    engine = pyttsx3.init()

    volume = engine.getProperty('volume')
    print(volume) #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)

    voices = engine.getProperty('voices')
    print(voices)

    #changing index, changes voices, 1 for female
    engine.setProperty('voice', voices[1].id)
    # say method on the engine that passing input text to be spoken
    engine.say((upCount.get()))
    # run and wait method, it processes the voice commands.
    engine.runAndWait()

##########################################################################################################################
def video():
    global cap,ex,label1
    # initialdir = the directory that the dialog starts in 
    # filetypes = apply filter on type of files 
    filename =filedialog.askopenfilename(initialdir="/", title="Select file ",
                                               filetypes=(("mp4 files", ".mp4"), ("all files", ".")))
    cap = cv2.VideoCapture(filename)
    w = 500
    h = 400
    label1 = Label(win, width=w, height=h,relief=GROOVE)
    label1.place(x=40, y=200)
    live()
###############################################################################################


wine()

#################################################BUTTONS############################################################################################
btn2 = Button(win, text='Live',padx=95,bg='gray',fg='#232224',relief=GROOVE ,width=7,bd=5,font=('Helvetica',14,'bold'),command=live).place(x=1000,y=500)
btn = Button(win, text='Video',padx=95,bg='gray',fg='#232224',relief=GROOVE,width=7,bd=5,font=('Helvetica',14,'bold') ,command= video).place(x=1000,y=550)
ex=Button(win,text='Exit',padx=95,bg='gray',fg='#232224',relief=GROOVE,width=7,bd=5,font=('Helvetica',14,'bold') ,command=win.destroy).place(x=1000,y=650)
vc=Button(win,text='Sound',padx=95,bg='gray',fg='#232224',relief=GROOVE,width=7,bd=5,font=('Helvetica',14,'bold') ,command=voice).place(x=1000,y=600)
win.mainloop()