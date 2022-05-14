from gui import *

def main():
    """
    Method used to initialize GUI.
    :param window: Window of GUI.
    :param widgets: Widgets of GUI.
    """
    window = Tk()
    widgets = GUI(window)
    window.title('Final Project')
    window.geometry('250x350')
    window.resizable(False, True)
    window.mainloop()
    
    

if __name__ == '__main__':
    main()
