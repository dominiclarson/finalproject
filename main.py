from gui import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 180.
    - Make the window non-resizable.
    """
    window = Tk()
    widgets = GUI(window)
    window.title('Lab 10')
    window.geometry('250x180')
    window.resizable(width=0, height=0)
    window.mainloop()
    

if __name__ == '__main__':
    main()
