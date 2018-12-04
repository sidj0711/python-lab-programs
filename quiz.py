from Tkinter import Tk, Frame, Label, Button 
from time import *
right=0

def check(letter, view):
        global right
        if letter == correctLetter[index]:
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000,lambda *arg: unpackView(view))


def getView(window):
        view = Frame(window,width=300, height=350)
        view.pack()
        lbl=Label(view, text=questions)
        button1=Button(view, text=answers[0], command=lambda *args: check("A", view))
        button2=Button(view, text=answers[1], command=lambda *args: check("B", view))
        button3=Button(view, text=answers[2], command=lambda *args: check("C", view))
        button4=Button(view, text=answers[3], command=lambda *args: check("D", view))
        lbl.pack()
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

def unpackView(view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global view,a,answers,answer,questions,question, window, index, button,right, number_of_questions 
    if(len(question) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions=question[index]
    answers=answer[index]
    getView(window)
    
questions=[]
question= ["Who is the captain of the indian cricket team?","Albert Einstein was awarded nobel prize for which of his work","If a moving object's velocity is changed by a factor of 1.5, what will its impact on its kinetic energy ?","Which is the most electronegative atom ?",""]
answer = [["Virat Kohli","M.S Dhoni","Rohit Sharma","Shikhar Dhawan"],["theory of relativity","Photoelectric effect","principle of wave-particle duality","theory of critical opalescence"],["1.5 times","3 times","2.25 times","6 times"]["O","F","Cl","Br"]]
correctLetter = ["A","B","C","B"]
index = -1
number_of_questions = len(question)

window = Tk()
view=Frame(window,width=300, height=350)
button = Button(view, text="Start", command=askQuestion)
view.pack()
button.pack()
window.mainloop()