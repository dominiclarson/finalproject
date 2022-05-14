from tkinter import *
import csv


class GUI:
    """
    Class representing details for a GUI object.
    """
    def __init__(self, window):
        """
        Constructor to create initial state of a GUI object.
        :param window: Window of GUI.
        :param age: Age value input by user.
        :param name: Name value input by user.
        :param radio: Button pressed by user.
        :param search: Search variable input by user.
        """
        self.window = window
        
        self.age = StringVar(window, '')
        self.name = StringVar(window, '')
        self.radio = StringVar(window, 'None selected')
        self.search = StringVar(window, '')
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name, textvariable=self.name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=(5, 20), side='right')
        self.frame_name.pack(anchor='w', pady=10)
        
        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age, textvariable=self.age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=(15, 20), side='right')
        self.frame_age.pack(anchor='w', pady=10)
        
        self.frame_radio = Frame(self.window)
        self.label_radio = Label(self.frame_radio, text='Status')
        self.r1_radio = Radiobutton(self.frame_radio, text='Student', variable=self.radio, value='Student')
        self.r2_radio = Radiobutton(self.frame_radio, text='Teacher', variable=self.radio, value='Teacher')
        self.r3_radio = Radiobutton(self.frame_radio, text='Both', variable=self.radio, value='Both')
        self.label_radio.pack(padx=5, side='left')
        self.r1_radio.pack(padx=0, side='left')
        self.r2_radio.pack(padx=0, side='left')
        self.r3_radio.pack(padx=0, side='left')
        self.frame_radio.pack(anchor='w', pady=10)
        
        self.frame_button = Frame(self.window)
        self.button = Button(self.frame_button, text='SAVE', command=self.clicked)
        self.button.pack(padx=0.5, anchor='n')
        self.frame_button.pack(fill="both", anchor='w', pady=5)
        
        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='', fg='red')
        self.frame_error.pack(anchor='n', pady=0)
        self.label_error.pack(side='left', pady=0)
        
        self.frame_search = Frame(self.window)
        self.label_search = Label(self.frame_search, text='Search for name:')
        self.entry_search = Entry(self.frame_search, textvariable=self.search)
        self.label_search.pack(padx=5, side='left')
        self.entry_search.pack(padx=(5, 5), side='right')
        self.frame_search.pack(anchor='w', pady=5)
        
        self.frame_button2 = Frame(self.window)
        self.button2 = Button(self.frame_button2, text='FIND', command=self.find)
        self.button2.pack(padx=0.5, anchor='n')
        self.frame_button2.pack(fill="both", anchor='w', pady=5)
        
        self.frame_results1 = Frame(self.window)
        self.label_results1 = Label(self.frame_results1, text='Name,Age,Status', fg='#0080ff', bg='white')
        self.frame_results1.pack(anchor='w', pady=0)
        self.label_results1.pack(side='left', pady=0)
        self.frame_results2 = Frame(self.window)
        self.label_results2 = Label(self.frame_results2, text='', fg='#0080ff')
        self.frame_results2.pack(anchor='w', pady=0)
        self.label_results2.pack(side='left', pady=0)

    def clicked(self):
        """
        Method called when save button is clicked and inputs entries from user into CSV file.
        :param age: Age value input by user.
        :param name: Name value input by user.
        :param radio: Button pressed by user.
        """
        if self.name.get() != '' and self.age.get() != '' and self.radio.get() != 'None selected':
            try:
                if int(self.age.get()) > 0:
                    with open('records.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        itemlist = [self.name.get(), int(self.age.get()), self.radio.get()]
                        writer.writerow(itemlist)
                else:
                    self.label_error.config(text='Age must be greater than 0')
            except:
                self.label_error.config(text='Age must be an integer')
        else:
            if self.name.get() == '' == self.age.get():
                self.label_error.config(text='Name and Age missing')
            if self.name.get() == '':
                self.label_error.config(text='Name missing')
            if self.age.get() == '':
                self.label_error.config(text='Age missing')
            if self.radio.get() == 'None selected':
                self.label_error.config(text='Status missing')
        
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio.set('None selected')

    def find(self):
        """
        Method used to find name items in a CSV file.
        :param listo: List of indexes where searched names were found.
        :param names: List of names in column 0 of the CSV file.
        :param fulltext: Full string to be displayed in the GUI.
        :param lines: All lines from CSV file.
        """
        with open('records.csv', mode='r') as file:
            listo = []
            names = []
            fulltext = ''
            lines = file.readlines()
            for x in range(len(lines)):
                lines[x] = lines[x].strip()
            for x in lines:
                y = x.split(',')
                names.append(y[0].lower())
            i = 0
            for x in names:
                if (self.search.get()).strip().lower() == x:
                    listo.append(i)
                i += 1
            for x in listo:
                fulltext += lines[x] + '\n'
            self.label_results2.config(text=fulltext)

    def __str__(self):
        """
        Method used to return the program status.
        :return: Program status.
        """
        return f"Name entry = {self.name.get()}, Age entry = {self.age.get()}, Radio button = {self.radio.get()}"
