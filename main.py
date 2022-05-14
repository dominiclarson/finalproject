from gui import *

#add search method
def main():
    window = Tk()
    widgets = GUI(window)
    window.title('Final Project')
    window.geometry('250x350')
    window.resizable(False, True)
    window.mainloop()
    

if __name__ == '__main__':
    main()
