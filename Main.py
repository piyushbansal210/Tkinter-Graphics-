import tkinter as tk    #pip install tkinter 
import sqlite3    #pip install sqlite3
import webbrowser    #pip install webbrowser
from datetime import datetime    #pip install datetime
import time    #pip install time
from tkinter import *
from os import path
from tkinter import filedialog
from better_profanity import profanity
from tkinter.ttk import * 
import speech_recognition as sr    #pip install speech_recognition
from tkinter import ttk   
import tkinter.font as tkfont   
import youtube_dl    #pip install youtube_dl
from tkinter import scrolledtext
from tkinter import messagebox   
import random    #pip install random
import pygame, sys    #pip install pygame
from pygame.locals import *   
import pyjokes    #pip install pyjokes
from wikipedia import *    #pip install wikipedia
import wikipedia
from textblob import TextBlob    #pip install textblob
from PIL import Image,ImageTk    #pip install PIL
import covid    #pip install covid
import pytesseract    #pip install pytesseract
import cv2     #pip install cv2
import PIL  
import pyshorteners    #pip install pyshorteners
import os    #pip install os
from win32com.client import Dispatch    #pip install win32com
from googletrans import Translator    #pip install googletrans
from langdetect import detect    #pip install langdetect
from tkcalendar import Calendar, DateEntry    #pip install tkcalendar
from tkcalendar import DateEntry 


def god():
    profanity.load_censor_words()
    #Setting the geometry and title of the gui
    good_words =Tk()
    good_words.title("Only good words")
    good_words.geometry("289x433")

    #Setting the geometry and background of the canvas
    canvas1 = tk.Canvas(good_words,height = 433,width = 289,bg = "#17A589")
    canvas1.pack()

    #this function will do the auto correction
    def button_correct():
        output.delete('1.0', END)
        inputValue=e.get("1.0","end")
        solution=profanity.censor(inputValue)
        
    # output.delete(0,END)
        for word in solution:
            output.insert(END, word)
    
    #this text area will the part where we will enter the text to be corrected
    e=tk.Text(good_words, width=24, borderwidth=3, height=7)
    e.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(145,90,window=e)
    
    #this button runs the function button_correct
    correct=tk.Button(good_words, text="Convert to good" ,width=37,bg = "#617C58",borderwidth=3,height=1,command=lambda: button_correct())
    canvas1.create_window(145,195,window=correct)
    
    #this function auto corrects the text using function(button_correct)
    output=tk.Text(good_words, width=24, borderwidth=5, height=9)
    output.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(144,320,window=output)

    #this is the loop that runs the grammer gui
    good_words.mainloop()

def joking():

    #running the function that gives the joke
    def tell():
        textarea.delete('1.0', END)
        global joke
        joke=pyjokes.get_joke()
        textarea.insert(END,joke)

    #selecting the geometry and title of the joke gui
    jokes=tk.Tk()
    jokes.geometry("289x433")
    jokes.title("Jokes Corner")

    #introducing canvas for the design of the page
    canvas=Canvas(jokes,width=289,height=433,bg="#a62b49")
    canvas.pack()

    #on clicking this button the functoin is run that makes the joke and put it in the textarea
    button=tk.Button(jokes,width=35,text="Tell a Joke",height=2,command=tell,bg="#D92625")
    canvas.create_window(145,40,window=button)

    #area where joke is printed
    textarea=tk.Text(jokes,height=12,width=22)
    canvas.create_window(145,250,window=textarea)
    textarea.config(font=("arial 15 bold"))

    #running the loop for gui
    jokes.mainloop()


def yt():

    #this statement opens the youtube
    webbrowser.open("youtube.com")

def gg():

    #this statement opens the google
    webbrowser.open("google.com")

def note():

    #after clicking save we need to choose the location and the default is set to txt
    def save_file():
        new_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', title="Save File")
        if new_file:
            text_to_save = txt.get('1.0', 'end-1c')
            new_file.write(text_to_save)
            new_file.close()
        else:
            messagebox.showinfo("Error", "Cancelled")

    #after clcking new all saved information wil be deleted
    def new_file():
        #root.destroy()
        #import note.py
        notes.title("Notes")
        file=None
        txt.delete(1.0,END)

    #this opens an already build note
    def open_file():

        #dir=filedialog.askdirnectory()
        global filename
        filename = filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("All files","*.*")), initialdir="/", title="Open File")
        txt.delete('1.0', tk.END)
        try:

            #the name of the root is set to the name of the file opened
            notes.title(filename)
            if filename:
                the_file=open(filename)
                for line in the_file.readlines():
                    text_line=line
                    txt.insert(tk.END, text_line + '\n')

                the_file.close()
            elif filename == '':
                messagebox.showinfo("Cancel", "Program been cancelled")  
        except IOError:

            #for any error
            messagebox.showinfo("Error", "Failed")  
    
    #for case of cut
    def cut():
        txt.event_generate("<<Cut>>")

    #for case of copy
    def copy():
        txt.event_generate("<<Copy>>")

    #for case of paste
    def paste():
        txt.event_generate("<<Paste>>")

    #introducing the gui for notes app
    notes = Tk()
    menu = Menu(notes)

    #for drop down menu
    list0=Menu(menu, tearoff=0)
    list1=Menu(menu, tearoff=0)

    #creating buttons in menu
    list0.add_command(label='New', command=new_file)
    list0.add_separator()
    list0.add_command(label='Open',command=open_file)
    list0.add_separator()
    list0.add_command(label='Save',command=save_file)
    list0.add_separator()
    list0.add_command(label='Quit',command=notes.quit)
    list1.add_command(label='Cut', command=cut)
    list1.add_separator()
    list1.add_command(label='Copy', command=copy)
    list1.add_separator()
    list1.add_command(label='Paste', command=paste)
    menu.add_cascade(label='File', menu=list0)
    menu.add_cascade(label='Edit', menu=list1)
    notes.config(menu=menu)

    #t4ext area for notes
    txt=tk.Text(notes, height=40, width=40, wrap=tk.NONE)
    txt.insert(tk.END, "")
    txt.configure(bg = "#2E86C1",fg='white',font='Arabic')
    txt.focus()
    txt.pack()

    #setting the geometry and title for notes app
    notes.geometry('289x412')
    notes.title('Notes')
    notes.mainloop()


def calci():

    #defining the geometry  and title of the GUI
    calculator=tk.Tk()
    calculator.title("Calculator")
    calculator.geometry("289x433")
    calculator.config(bg = "#BFC9CA")

    #the number is entered here
    e=tk.Entry(calculator, width=40, borderwidth=2)
    e.grid(row=0,column=0,columnspan=3,ipady=11)
    e.configure(font=("Cambria",8,"bold"))

    #defining this button to get the entered number in form of a string
    def button_click(number):
        #e.delete(0,END)
        current=e.get()
        e.delete(0,END)
        e.insert(0,str(current) + str(number))

    #Defining the clear button to clear the Entry area
    def button_clear():
        e.delete(0,END)

    #defining the add button's work
    def button_add():
        first_number=e.get()
        global f_num
        global math
        math="addition"
        f_num=float(first_number)  
        e.delete(0,END)

    #defining the subtract button's work
    def button_subtract():
        first_number=e.get()
        global f_num
        global math
        math="subtraction"
        f_num=float(first_number)
        e.delete(0,END)

    #defining the multiply button's work
    def button_multiply():
        first_number=e.get()
        global f_num
        global math
        math="multiplication"
        f_num=float(first_number)
        e.delete(0,END)

    #defining the divide button's work
    def button_divide():
        first_number=e.get()
        global f_num
        global math
        math="division"
        f_num=float(first_number)
        e.delete(0,END)

    #defining the equal button's work
    def button_equal():
        second_number=e.get()
        e.delete(0,END)

        if math=="addition":
            e.insert(0,f_num +float(second_number))
        if math=="multiplication":
            e.insert(0,f_num *float(second_number))
        if math=="division":
            e.insert(0,f_num /float(second_number))
        if math=="subtraction":
            e.insert(0,f_num -float(second_number))

    #on pressing the buttons the value is directed to the button_click function
    button_1=tk.Button(calculator,text="1" ,padx=40,pady=20,command=lambda: button_click(1),bg = "#869192",borderwidth=3).grid(row=3,column=2)
    button_2=tk.Button(calculator,text="2" ,padx=40,pady=20,command=lambda: button_click(2),bg = "#869192",borderwidth=3).grid(row=3,column=1)
    button_3=tk.Button(calculator,text="3" ,padx=40,pady=20,command=lambda: button_click(3),bg = "#869192",borderwidth=3).grid(row=3,column=0)
    button_4=tk.Button(calculator,text="4" ,padx=40,pady=20,command=lambda: button_click(4),bg = "#869192",borderwidth=3).grid(row=2,column=2)
    button_5=tk.Button(calculator,text="5" ,padx=40,pady=20,command=lambda: button_click(5),bg = "#869192",borderwidth=3).grid(row=2,column=1)
    button_6=tk.Button(calculator,text="6" ,padx=40,pady=20,command=lambda: button_click(6),bg = "#869192",borderwidth=3).grid(row=2,column=0)
    button_7=tk.Button(calculator,text="7" ,padx=40,pady=20,command=lambda: button_click(7),bg = "#869192",borderwidth=3).grid(row=1,column=2)
    button_8=tk.Button(calculator,text="8" ,padx=40,pady=20,command=lambda: button_click(8),bg = "#869192",borderwidth=3).grid(row=1,column=1)
    button_9=tk.Button(calculator,text="9" ,padx=40,pady=20,command=lambda: button_click(9),bg = "#869192",borderwidth=3).grid(row=1,column=0)
    button_0=tk.Button(calculator,text="0" ,padx=40,pady=20,command=lambda: button_click(0),bg = "#869192",borderwidth=3).grid(row=4,column=0)

    #these are the operation buttons. this counts the function 
    button_clear=tk.Button(calculator,text="Clear" ,padx=77,pady=20, command= button_clear,bg = "#869192",borderwidth=3).grid(row=4,column=1,columnspan=2)
    button_add=tk.Button(calculator,text="+" ,padx=39,pady=20,command=button_add,bg = "#869192",borderwidth=3).grid(row=5,column=0)
    button_subtract=tk.Button(calculator,text="-" ,padx=41,pady=24,command= button_subtract,bg = "#869192",borderwidth=3).grid(row=6,column=0)
    button_divide=tk.Button(calculator,text="/" ,padx=41,pady=24, command= button_divide,bg = "#869192",borderwidth=3).grid(row=6,column=1)
    button_multiply=tk.Button(calculator,text="*", padx=40,pady=24, command= button_multiply,bg = "#869192",borderwidth=3).grid(row=6,column=2)
    button_equal=tk.Button(calculator,text="=" ,padx=86,pady=20,command=button_equal,bg = "#869192",borderwidth=3).grid(row=5,column=1,columnspan=2)

    #running the GUI
    calculator.mainloop()

def shorten():
    
    #inserting the title and geometry of the url shorten gui
    short =tk.Tk()
    short.title("Url Shortener")
    short.geometry("289x433")

    #this function will shorten the url
    def button_correct():
        output.delete('1.0', END)
        inputValue=e.get("1.0","end")
        x= pyshorteners.Shortener().clckru.short(inputValue)  
        for word in x:
            output.insert(END, word)
 
    #setting the background of canvas and area of canvas
    canvas1 = tk.Canvas(short,height = 433,width = 289,bg = "#F7DC6F")
    canvas1.pack()

    #here we are supposed to enter the link that we want to shorten
    e=tk.Text(short, width=24, borderwidth=3, height=4)
    e.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(145,56,window=e)
    
    #this button will run the button_correct functin that will shorten the link
    correct=tk.Button(short, text="Shorten The Url" ,width=37,bg = "#D4AC0D",borderwidth=3,height=1,command=button_correct)
    canvas1.create_window(145,125,window=correct)
    
    output=tk.Text(short, width=24, borderwidth=5, height=12)
    output.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(144,285,window=output)
    short.mainloop()

def cale():

    #setting the geometry, title and background color of the guiof the calendar gui
    cal =tk.Tk()
    cal.geometry("289x433")
    cal.title("Calendar")
    cal.configure(bg="#F4F6F7")

    #styling the calendar's color 
    style = ttk.Style()
    style.configure('my.DateEntry',
                            fieldbackground='light green',
                            background='dark green',
                            foreground='dark blue',
                            arrowcolor='white')

    #inserting the calendar
    cal = Calendar(cal,font="Times 14", year=2020,style="my.DateEntry",pady=30)
    cal.pack(fill="both",expand=False)
    
    #this runs the loop
    cal.mainloop()

def dik():

    #setting the title ad geometry of the encyclopedia 
    Encyclopedia=tk.Tk()
    Encyclopedia.title("Encyclopedia")
    Encyclopedia.geometry("289x433")

    #setting the background of canvas and area of canvas
    canvas1 = tk.Canvas(Encyclopedia,height = 433,width = 289,bg = "#979A9A")
    canvas1.pack()

    #this function finds the word and insert the meaning into the output
    def button_correct():
        output.delete('1.0', END)
        inputValue=e.get("1.0","end")
        inputValue=inputValue.lower()
        text=wikipedia.summary(inputValue,sentences=2)   
        for word in text:
            output.insert(END, word)

    #this text area scnas the word 
    e=tk.Text(Encyclopedia, width=24, borderwidth=3, height=2)
    e.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(145,35,window=e)

    #this button runs the function button_correct
    correct=tk.Button(Encyclopedia, text="Meaning" ,width=37,bg = "#515A5A",borderwidth=3,height=1,command=lambda: button_correct())
    canvas1.create_window(145,83,window=correct)

    #this function shows the meaning calculated by the function(button_correct)
    output=tk.Text(Encyclopedia, width=24, borderwidth=5, height=14)
    output.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(144,265,window=output)
    Encyclopedia.mainloop()
 


def yts():
    
    #setting the title and geometry of the youtuber downloader
    ytd = tk.Tk()
    ytd.title("YouTube Video Downloader")
    ytd.geometry("289x433")

    #setting canvas to insert the size of the insertion area
    canvas1 = tk.Canvas(ytd,height = 433,width = 289,bg = "#A93226")
    canvas1.pack()

    #setting the font family ,size and weight
    bold_font = tkfont.Font(family = "Helvetica", size = 20,weight = "bold")

    #label for entering the url
    label1 = tk.Label(ytd,text = "Enter the URL",width = 14,bg = "#b4a7d6")
    label1.config(font = bold_font)
    canvas1.create_window(150,100,window = label1)

    #in download_entry we insert the youtube link
    download_entry = tk.Entry(ytd,width=40,borderwidth=3)
    canvas1.create_window(150,160,window = download_entry)

    #this function downloads the youtube video
    def get_video_url():
      search_item = download_entry.get()
      ydl_opts = {'format': 'best','noplaylist':True,'extract-  audio':True,}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_item])
    
    #label for clicking download button
    bold_font2 = tkfont.Font(family="Helvetica",size=10,weight="bold")
    label2 =tk.Label(ytd,text="Click Download",width=20,bg = "#b4a7d6")
    label2.config(font=bold_font2)
    canvas1.create_window(150,300,window=label2)

    #this button runs the get_video_url function and downoads the video
    download = tk.Button(ytd,text= "Download", padx=5,pady=5,fg = "white",bg = "#D4AC0D",command = get_video_url,borderwidth=3)
    canvas1.create_window(150,230,window=download)

    #this runs the youtube downloader function
    ytd.mainloop()

def gram():

    #Setting the geometry and title of the gui
    grammer =Tk()
    grammer.title("Auto Correct")
    grammer.geometry("289x433")

    #Setting the geometry and background of the canvas
    canvas1 = tk.Canvas(grammer,height = 433,width = 289,bg = "#17A589")
    canvas1.pack()

    #this function will do the auto correction
    def button_correct():
        output.delete('1.0', END)
        inputValue=e.get("1.0","end")
        inputValue=inputValue.lower()
        text=TextBlob(inputValue)
        solution=text.correct()
        
    # output.delete(0,END)
        for word in solution:
            output.insert(END, word)
    
    #this text area will the part where we will enter the text to be corrected
    e=tk.Text(grammer, width=24, borderwidth=3, height=7)
    e.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(145,90,window=e)
    
    #this button runs the function button_correct
    correct=tk.Button(grammer, text="Meaning" ,width=37,bg = "#196F3D",borderwidth=3,height=1,command=lambda: button_correct())
    canvas1.create_window(145,195,window=correct)
    
    #this function auto corrects the text using function(button_correct)
    output=tk.Text(grammer, width=24, borderwidth=5, height=9)
    output.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(144,320,window=output)

    #this is the loop that runs the grammer gui
    grammer.mainloop()

def transposter():

    #setting the title and geometry of the translator gui
    Translato=tk.Tk()
    Translato.title("Translator")
    Translato.geometry("289x433")

    #this function is used for conversion
    def show():

        #this scans the entered value
        answer.delete('1.0', END)
        p=clicked.get()
        trans=Translator()
        x=e.get("1.0","end")
        
        #converts the text into african
        if p=="Afrikans":
            t=trans.translate(
                x,src=detect(x), dest='af'
            )
            for word in t.text:
                    answer.insert(END, word)
            
        #converts the text into armenian
        if p=="Armenian":
            t=trans.translate(
                x,src=detect(x), dest='hy'
            )

            for word in t.text:
                    answer.insert(END, word)

        #converts the text into dutch
        if p=="Dutch":
            t=trans.translate(
                x,src=detect(x), dest='nl'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into english
        if p=="English":
            t=trans.translate(
                x,src=detect(x), dest='en'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into french
        if p=="French":
            t=trans.translate(
                x,src=detect(x), dest='fr'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into german
        if p=="German":
            t=trans.translate(
                x,src=detect(x), dest='de'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into gujrati
        if p=="Gujarati":
            t=trans.translate(
                x,src=detect(x), dest='gu'
            )
            for word in t.text:
                    answer.insert(END, word)
            
        #converts the text into italian
        if p=="Italian":
            t=trans.translate(
                x,src=detect(x), dest='it'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into japnese
        if p=="Japanese":
            t=trans.translate(
                x,src=detect(x), dest='ja'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into kannada
        if p=="Kannada":
            t=trans.translate(
                x,src=detect(x), dest='kn'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into malyalam
        if p=="Malayalam":
            t=trans.translate(
                x,src=detect(x), dest='ml'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into punjabi
        if p=="Punjabi":
            t=trans.translate(
                x,src=detect(x), dest='pa'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into spanish
        if p=="Spanish":
            t=trans.translate(
                x,src=detect(x), dest='es'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into polish     
        if p=="Polish":
            t=trans.translate(
                x,src=detect(x), dest='pl'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into czech
        if p=="Czech":
            t=trans.translate(
                x,src=detect(x), dest='cs'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into filipino
        if p=="Filipino":
            t=trans.translate(
            x,src=detect(x), dest='tl'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into telugu
        if p=="Telugu":
            t=trans.translate(
            x,src=detect(x), dest='te'
            )
            for word in t.text:
                    answer.insert(END, word)

        #converts the text into swedish
        if p=="Swedish":
            t=trans.translate(
                x,src=detect(x), dest='sv'
            )
            for word in t.text:
                    answer.insert(END, word)

    #Setting the geometry and background of the canvas
    canvas1 = tk.Canvas(Translato,height = 433,width = 289,bg = "#D98880")
    canvas1.pack()

    #the value is scanned here
    e=tk.Text(Translato, width=24, borderwidth=3, height=7)
    e.configure(font=("Cambria", 14, "bold"))
    canvas1.create_window(143,90,window=e)
    
    clicked=StringVar()
    clicked.set("English")
    #drop down send the choosen language to the function
    drop=tk.OptionMenu(Translato, clicked,"Afrikans","Armenian","Dutch","English","French","German","Gujarati","Italian","Japanese","Kannada","Malayalam","Punjabi","Spanish","Polish","Czech","Filipino","Telugu","Swedish")
    canvas1.create_window(50,195,window=drop)
    
    #this button runs the function
    button=tk.Button(Translato, width=24,text="Translate",command=show,bg = "#C0392B")
    canvas1.create_window(190,195,window=button)

    #after the text is processed in the function the text is send to this text area
    answer=Text(Translato, width=24, borderwidth=3, height=9)
    canvas1.create_window(143,320,window=answer)
    answer.configure(font=("Cambria", 14, "bold"))
    Translato.mainloop()

def tictactoe():
    global bclick
    global flag
    tic = tk.Tk()
    tic.geometry("289x433")
    tic.title("TicTacToe")
    tic.config(bg = "#B7950B")
    pa = StringVar();
    playerb = StringVar()
    p1 = StringVar()
    p2 = StringVar()
    player1_name = tk.Entry(tic, textvariable=p1, bd=5)
    player1_name.grid(row=1, column=1, columnspan=2,padx=2)
    player2_name = tk.Entry(tic, textvariable=p2, bd=5)
    player2_name.grid(row=2, column=1, columnspan=2)
    bclick = True
    flag = 0

    def disableButton():
        button1.configure(state=DISABLED)
        button2.configure(state=DISABLED)
        button3.configure(state=DISABLED)
        button4.configure(state=DISABLED)
        button5.configure(state=DISABLED)
        button6.configure(state=DISABLED)
        button7.configure(state=DISABLED)
        button8.configure(state=DISABLED)
        button9.configure(state=DISABLED)

    def btnclick(buttons):
        global bclick, flag, player2_name, player1_name, playerb, pa
        if buttons["text"] == " " and bclick == True:
            buttons["text"] = "x"
            bclick = False
            playerb = p2.get() + " Wins!"
            pa = p1.get() + " Wins!"
            checkForWin()
            flag += 1

        elif buttons["text"] == " " and bclick == False:
            buttons["text"] = "o"
            bclick = True
            checkForWin()
            flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")

    def checkForWin():
        if(button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x' or button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x' or button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x' or button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x' or button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x' or button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x' or button7['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x'):
            disableButton()
            messagebox.showinfo("Tic-Tac-Toe", pa)

        elif(flag == 8):
            tk.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

        elif (button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
            button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o' or
            button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o' or
            button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o' or
            button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o' or
            button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
            button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o' or
            button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o' or
            button7['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o'):
            disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

    buttons = StringVar()

    lable1 = tk.Label( tic, text="player 1:", font='Times 20 bold', bg='White', fg='red', height=1, width=6)
    lable1.grid(row=1, column=0)

    lable2 = tk.Label( tic, text="player 2:", font='Times 20 bold', bg='White', fg='blue', height=1, width=6)
    lable2.grid(row=2, column=0)


    button1 = tk.Button(tic, text=" ", font='Times 20 bold', fg='White', height=2, width=6,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button1))
    button1.grid(row=4, column=0)

    button2 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=5,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button2))
    button2.grid(row=4, column=1)

    button3 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=5,padx=2,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button3))
    button3.grid(row=4, column=2)

    button4 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=6,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button4))
    button4.grid(row=5, column=0)

    button5 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=5,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button5))
    button5.grid(row=5, column=1)

    button6 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=5,padx=2,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button6))
    button6.grid(row=5, column=2)

    button7 = tk.Button(tic, text=' ', font='Times 20 bold', fg='White', height=2, width=5,padx=9,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button7))
    button7.grid(row=6, column=0)

    button8 = tk.Button(tic, text=' ', font='Times 20 bold',  fg='White', height=2, width=5,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button8))
    button8.grid(row=6, column=1)

    button9 = tk.Button(tic, text=' ', font='Times 20 bold',  fg='White', height=2, width=5,padx=2,bg = "#9A7D0A",borderwidth=3,
    command=lambda: btnclick(button9))
    button9.grid(row=6, column=2)

    tic.mainloop()
    



def ttgame():
    pygame.init()
    fps = pygame.time.Clock()

    #colors
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLACK = (0,0,0)

    #globals
    WIDTH = 289
    HEIGHT = 433     
    BALL_RADIUS = 20
    PAD_WIDTH = 8
    PAD_HEIGHT = 80
    HALF_PAD_WIDTH = PAD_WIDTH // 2
    HALF_PAD_HEIGHT = PAD_HEIGHT // 2
    ball_pos = [0,0]
    ball_vel = [0,0]
    paddle1_vel = 0
    paddle2_vel = 0
    l_score = 0
    r_score = 0

    #canvas declaration
    window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    pygame.display.set_caption('Table Tennis')

    # helper function that spawns a ball, returns a position vector and a velocity vector
    # if right is True, spawn to the right, else spawn to the left
    def ball_init(right):
        global ball_pos, ball_vel # these are vectors stored as lists
        ball_pos = [WIDTH//2,HEIGHT//2]
        horz = random.randrange(2,4)
        vert = random.randrange(1,3)
        
        if right == False:
            horz = - horz
            
        ball_vel = [horz,-vert]
    # define event handlers
    def init():
        global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,l_score,r_score  # these are floats
        global score1, score2  # these are ints
        paddle1_pos = [HALF_PAD_WIDTH - 1,HEIGHT//2]
        paddle2_pos = [WIDTH +1 - HALF_PAD_WIDTH,HEIGHT//2]
        l_score = 0
        r_score = 0
        if random.randrange(0,2) == 0:
            ball_init(True)
        else:
            ball_init(False)


    #draw function of canvas
    def draw(canvas):
        global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score
            
        canvas.fill(BLACK)
        pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
        pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
        pygame.draw.line(canvas, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
        pygame.draw.circle(canvas, WHITE, [WIDTH//2, HEIGHT//2], 70, 1)

        # update paddle's vertical position, keep paddle on the screen
        if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
            paddle1_pos[1] += paddle1_vel
        
        if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
            paddle2_pos[1] += paddle2_vel

        #update ball
        ball_pos[0] += int(ball_vel[0])
        ball_pos[1] += int(ball_vel[1])

        #draw paddles and ball
        pygame.draw.circle(canvas, RED, ball_pos, 20, 0)
        pygame.draw.polygon(canvas, GREEN, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
        pygame.draw.polygon(canvas, GREEN, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

        #ball collision check on top and bottom walls
        if int(ball_pos[1]) <= BALL_RADIUS:
            ball_vel[1] = - ball_vel[1]
        if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
            ball_vel[1] = -ball_vel[1]
        
        #ball collison check on gutters or paddles
        if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,paddle1_pos[1] + HALF_PAD_HEIGHT,1):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
            r_score += 1
            ball_init(True)
            
        if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(paddle2_pos[1] - HALF_PAD_HEIGHT,paddle2_pos[1] + HALF_PAD_HEIGHT,1):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
            l_score += 1
            ball_init(False)

        #update scores
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render("Score "+str(l_score), 1, (255,255,0))
        canvas.blit(label1, (50,20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render("Score "+str(r_score), 1, (255,255,0))
        canvas.blit(label2, (470, 20))  
        
        
    #keydown handler
    def keydown(event):
        global paddle1_vel, paddle2_vel
        
        if event.key == K_UP:
            paddle2_vel = -8
        elif event.key == K_DOWN:
            paddle2_vel = 8
        elif event.key == K_a:
            paddle1_vel = -8
        elif event.key == K_s:
            paddle1_vel = 8

    #keyup handler
    def keyup(event):
        global paddle1_vel, paddle2_vel
        
        if event.key in (K_a, K_s):
            paddle1_vel = 0
        elif event.key in (K_UP, K_DOWN):
            paddle2_vel = 0

    init()


    #game loop
    while True:

        draw(window)

        for event in pygame.event.get():

            if event.type == KEYDOWN:
                keydown(event)
            elif event.type == KEYUP:
                keyup(event)
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
        fps.tick(60)

#after checking the account existance desktop is run 
def desktop2():
    #setting the geometry and title of the gui
    desktop = tk.Tk()
    desktop.title("Desktop")
    desktop.geometry("289x433")

    #canvas is used to set the positions of the buttons 
    canvas1 = tk.Canvas(desktop,height = 433,width = 289)
    canvas1.pack()

    #after clicking this calculator is run
    button1 = tk.Button(desktop,width=10,text="Calculator",command=calci,bg = "#BFC9CA",borderwidth=8,height=2)
    canvas1.create_window(50,50,window = button1)

    #after clicking this assistant is run
    button2 = tk.Button(desktop,width=10,height=2,text="Notes",bg = "#2E86C1",borderwidth=8,command=note)
    canvas1.create_window(145,50,window = button2)

    #after clicking this tictactoe is run
    button3 = tk.Button(desktop,width=10,height=2,text="TicTacToe",command=tictactoe,bg = "#B7950B",borderwidth=8)
    canvas1.create_window(240,50,window = button3)

    #after clicking this encyclopedia is run
    button4 = tk.Button(desktop,width=10,height=2,text="Encyclopedia",command=dik,bg = "#979A9A",borderwidth=8)
    canvas1.create_window(50,120,window = button4)

    #after clicking this translator is run
    button5 = tk.Button(desktop,width=10,height=2,text="Translator",command=transposter,bg = "#D98880",borderwidth=8)
    canvas1.create_window(145,120,window = button5)

    #after clicking this autocorrect is run
    button6 = tk.Button(desktop,width=10,height=2,text="AutoCorrect",command =gram,bg = "#17A589",borderwidth=8)
    canvas1.create_window(240,120,window = button6)

    #after clicing this calendar is run
    button7 = tk.Button(desktop,width=10,height=2,text="Calendar",command=cale,bg = "#F4F6F7",borderwidth=8)
    canvas1.create_window(50,190,window = button7)

    #after clicking this url shortener is run
    button8 = tk.Button(desktop,width=10,height=2,text="UrlShortener",command=shorten,bg = "#F7DC6F",borderwidth=8)
    canvas1.create_window(145,190,window = button8)

    #after clicking this table tennis game is runyts
    button9 = tk.Button(desktop,width=10,height=2,text="Downloader",command=yts,bg = "#A93226",borderwidth=8)
    canvas1.create_window(240,190,window = button9)

    #after clicking this youtube downloader is run
    button10 = tk.Button(desktop,width=10,height=2,text="TTGame",bg = "#76D7C4",borderwidth=8,command=ttgame)
    canvas1.create_window(50,260,window = button10)

    #after clicking this Google is run on your pc
    button11 = tk.Button(desktop,width=10,height=2,text="Google",bg = "#5CCA40",borderwidth=8,command=gg)
    canvas1.create_window(145,260,window = button11)

    #after clicking this youtube run
    button12 = tk.Button(desktop,width=10,height=2,text="Youtube",bg = "#BD6868",borderwidth=8,command=yt)
    canvas1.create_window(240,260,window = button12)

    #after clicking this a joke box is opened
    button12 = tk.Button(desktop,width=10,height=2,text="Jokes",bg = "#D926C5",borderwidth=8,command=joking)
    canvas1.create_window(50,330,window = button12)

    #after clicking this a badwords eraser is deleted is opened
    button12 = tk.Button(desktop,width=10,height=2,text="God Words",bg = "#617C58",borderwidth=8,command=god)
    canvas1.create_window(145,330,window = button12)


    #this loops the dektop gui
    desktop.mainloop()

def database(user,passcode):
    #connection our python code to the database
    conn=sqlite3.connect('Main.db')
    cur=conn.cursor()

    #creating table in which we are storing data
    cur.execute('''
        CREATE TABLE IF NOT EXISTS data(
            username TEXT,
            password VARCHAR
        )
    ''')

    #the values which we have got through constructoris now put into a variable
    hello=user
    hi=passcode

    #selecting  the data and checking if it already exists
    value=cur.execute('SELECT *FROM data where username=?',(hello,))
    row=value.fetchone()

    if row is None:
        #if there is no coomon username in db then enter 
        cur.execute('INSERT INTO data(username,password) VALUES(?,?)',(hello,hi))

    else:
        #else show error message box
        messagebox.showerror("User Error","This Username Already Exists")
    conn.commit()
    

    
#login function is created to check whether username or password is same and exists
def login(operator,code):
    #connecting the database
    conn=sqlite3.connect('Main.db')
    cur=conn.cursor()

    #Assigning variables to the input username and password
    user_login=operator
    pass_login=code
    
    #Selection is used to check whether username and password are in the databse and are password is assigned for the same username
    truecase=cur.execute('SELECT *FROM data where username=? AND password=?',(user_login,pass_login))
    
    #fetching the data selected
    rows=truecase.fetchone()

    #if the username and password doesnot exists
    if rows is None:
        messagebox.showerror("Login Issue","This Username and Password Does not Exists")

    #run the desktop function if username and password exists
    else:
        desktop2()

    #close the database after use
    conn.commit()
    cur.close()

#this function creates an account in database
def signup():

    #setting the geometry and title of the gui
    signup=tk.Tk()
    signup.geometry("289x433")
    signup.title("SignUp")

    #it is a gui in a gui
    frame_signup=tk.LabelFrame(signup,text="Signup",padx=40,pady=160)
    frame_signup.pack(padx=4,pady=4)

    #For Entering the username, Used to store data in the database
    username=tk.Label(frame_signup,text="Username:")
    username.grid(row=0,column=0)
    entry_username=tk.Entry(frame_signup, borderwidth=3,width=20)
    entry_username.grid(row=0,column=1)

    #For Entering the password, Used to store data in the database
    password=tk.Label(frame_signup,text="Password:")
    password.grid(row=2,column=0)
    entry_password=tk.Entry(frame_signup, borderwidth=3,width=20,show="*")
    entry_password.grid(row=2,column=1)

    #For creating space
    extra_label=tk.Label(frame_signup,text="",width=10)
    extra_label.grid(row=3,column=0,columnspan=2)
    
    #For Signing up
    start_button=tk.Button(frame_signup,text="Create Account",borderwidth=3,width=28,command=lambda: database(entry_username.get(),entry_password.get()),bg = "#674ea7")
    start_button.grid(row=4,column=0,columnspan=2)

    #Main Loop
    signup.mainloop()

#this statement run the tkinter 
root=tk.Tk()

#setting the geometry and title of the main gui
root.geometry("289x433")
root.title("CodeHub")

#it is the gui in a gui
frame=tk.LabelFrame(root,text="SignIn",padx=40,pady=110)
frame.pack(padx=4,pady=4)

#it is ued to enter username
username=tk.Label(frame,text="Username:")
username.grid(row=0,column=0)
entry_username=tk.Entry(frame, borderwidth=3,width=20)
entry_username.grid(row=0,column=1)

#it is used to insert passowrd
password=tk.Label(frame,text="Password:")
password.grid(row=2,column=0)
password=tk.Entry(frame, borderwidth=3,width=20,show="*")
password.grid(row=2,column=1)

#some extra spaces
extra_label=tk.Label(frame,text="",width=10)
extra_label.grid(row=3,column=0,columnspan=2)

#this function runs the signup that detects that the usernme and password exists
start_button=tk.Button(frame,text="LogIn",borderwidth=3,width=28,command=lambda: login(entry_username.get(),password.get()),bg = "#674ea7")
start_button.grid(row=4,column=0,columnspan=2)

#some extra spaces
extra_label=tk.Label(frame,text="",width=10)
extra_label.grid(row=5,column=0,columnspan=2)
extra_label=tk.Label(frame,text="",width=10)
extra_label.grid(row=6,column=0,columnspan=2)
extra_label=tk.Label(frame,text="",width=10)
extra_label.grid(row=7,column=0,columnspan=2)

#this is a gui used to insert or create an account in the codehub
extra_label=tk.Label(frame,text="Don't Have An Account",width=20,padx=10)
extra_label.grid(row=7,column=0,columnspan=2)
sign_up=tk.Button(frame,text="Create One!!",borderwidth=3,width=28,command=signup,bg = "#674ea7")
sign_up.grid(row=8,column=0,columnspan=2)

#loop for running the main gui
root.mainloop()