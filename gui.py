from tkinter import *
import csv

class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window
        
        self.age = StringVar(window, '')
        self.name = StringVar(window, '')
        self.radio = StringVar(window, 'None selected')
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name, textvariable = self.name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=(5,20), side='right')
        self.frame_name.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.
        
        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age, textvariable = self.age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=(15,20), side='right')
        self.frame_age.pack(anchor='w', pady=10)   # anchor='w' helps to change the frame position from center to west.
        
        self.frame_radio = Frame(self.window)
        self.label_radio= Label(self.frame_radio, text='Status')
        self.r1_radio = Radiobutton(self.frame_radio, text='Student', variable=self.radio, value='Student')
        self.r2_radio = Radiobutton(self.frame_radio, text='Teacher', variable=self.radio, value='Teacher')
        self.r3_radio = Radiobutton(self.frame_radio, text='Both', variable=self.radio, value='Both')
        self.label_radio.pack(padx=5, side='left')
        self.r1_radio.pack(padx=0, side='left')
        self.r2_radio.pack(padx=0, side='left')
        self.r3_radio.pack(padx=0, side='left')
        self.frame_radio.pack(anchor='w', pady=10)
        
        self.frame_button=Frame(self.window)
        self.button = Button(self.frame_button, text='SAVE', command=self.clicked)
        self.button.pack(padx=0.5, anchor='s')
        self.frame_button.pack(fill="both", anchor='w', pady=10)


    def clicked(self):
        """
        - This method should only be called when the save button is clicked.
        - Retrieve the name, age, and status values.
        - The age must be doubled (e.g. if someone entered 5 for age, their age would be stored as 10).
        - Determine the person status based off the value of the radio button selected.

        - Open the records.csv file and append the new person's details.
        - I suggest first viewing the csv file's contents to understand how your data should be sent to it.

        - Clear the name and age values that were entered in the GUI.
        - Make sure you clear the status value (i.e, No status value should be selected).
        """
        with open('records.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            itemlist = [self.name.get(), int(self.age.get()) * 2, self.radio.get()]
            writer.writerow(itemlist)
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio.set(None)