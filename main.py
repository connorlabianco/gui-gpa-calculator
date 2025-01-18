'''
DEVELOPER: Connor La Bianco

Description:
This program calculates the GPA of students.
It does this using a GUI to allow students to input their courses, choosing between highschool and college, and then add their course information. At the top left lies an instructions button if the student does not know how to use the program. Highschool students may choose if their class is AP or not. Students may utilize add course button as many times as necessary for all their courses. Once finished adding courses, the student can click submit grades, and a messagebox will be displayed showing the student what their gpa is. For highschool students, this will include their unweighted and weighted gpa's.
Lastly, if student wishes to reset their grades, they may do so by hitting the reset button at the top. There is also a quit program button if the student is finished.
'''


# Imports
from tkinter import *
from calculator_GUI import Calculator_GUI

# Program
def main():
    '''Launches GUI'''
    window = Tk()
    gui = Calculator_GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()