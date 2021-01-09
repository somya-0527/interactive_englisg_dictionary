
import pyttsx3
from tkinter import messagebox, simpledialog
from difflib import get_close_matches

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def translationSpeak():
    if n==1:
        speak("The meaning is: ")
    else:
        speak("There are %d meanings"%(n-1))
    speak(t1.get(1.0,END))

def translation(w):
    global n
    if type(w==list):
        n=1
        if len(w)>1:
            for i in w:
                t1.insert(END,str(n)+". "+i+"\n")
                n=n+1
        else:
            t1.insert(END,w[0])

def translate():
    word=e2_value.get()
    word_L=word.lower()
    word_U=word.upper()
    word_T=word.title()
    if word_L in dictionary.keys():
        t1.delete("1.0",END)
        translation(dictionary[word_L])
    elif word_U in dictionary.keys():
        t1.delete("1.0",END)
        translation(dictionary[word_U])
    elif word_T in dictionary.keys():
        t1.delete("1.0",END)
        translation(dictionary[word_T])
    
    elif len(get_close_matches(word,dictionary.keys()))>0:
        t1.delete("1.0",END)
        speak("did you mean '%s' ? "%get_close_matches(word,dictionary.keys())[0])
        yn=messagebox.askquestion("please answer","did you mean'%s'instead?"%get_close_matches(word,dictionary.keys())[0])
        
        if yn=='yes':
            translation(dictionary[get_close_matches(word,dictionary.keys())[0]])
            e2.delete(0,END)
            e2.insert(0,get_close_matches(word,dictionary.keys())[0])
        else:
            t1.insert(END,speak("word not found in the dictionary"))
    else:
        t1.delete("1.0",END)
        t1.insert(END,speak("word not found in dictionary!!"))



from tkinter import*
import json

window=Tk()
window.title('INTERACTIVE DICTIONARY')
speak("welcome to interactive dictionary")
win_height=728
win_width=1000

dictionary=json.load(open("data.json"))

dic_frame=LabelFrame(window,text='Get the meaning here', font=('Eras Medium ITC',10))
dic_frame.grid(row=0,column=win_width//2,pady=20)

e1=Label(dic_frame,text='Enter word: ',font=('Eras Medium ITC',12,'bold'))
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(dic_frame,textvariable=e2_value,font=('Eras Medium ITC',12,'bold'))
e2.grid(row=0,column=1)

b1=Button(dic_frame,text='meaning: ' ,command=translate, font=('Eras Medium ITC',12,'bold'))
b1.grid(row=0,column=2)

pic=PhotoImage(file='speaker.png')
photoimage=pic.subsample(3,3)

ListenMeaning=Button(dic_frame,image=photoimage,border=0,command=translationSpeak)
ListenMeaning.grid(row=0,column=3,padx=4)

t1=Text(dic_frame, height=10,font=('Eras Medium ITC',12,'bold'))
t1.grid(row=1,columnspan=4)

window.mainloop()