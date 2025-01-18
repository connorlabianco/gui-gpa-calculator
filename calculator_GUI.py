from tkinter import *
from tkinter import messagebox
from student import Student

class Calculator_GUI:

    def __init__(self, window=None):
        if window is None:
            raise ValueError("Must pass valid Tkinter window parameter in order to use GUI functionality")
        self.window = window

    def __init__(self, window):
        '''Parametized constructor for the gui'''
        self.window = window
        self.window.title("GPA Calculator")
        self.window.geometry("600x600")

        # Variables
        self.COLLEGE = 0 #ATTRIBUTE 1  # should not have accessors or mutators since it is a constant
        self.HIGHSCHOOL = 1 #ATTRIBUTE 2 # should not have accessors or mutators since it is a constant
        self.student_type_var = IntVar(value=self.COLLEGE)  # Defaults selection as College Student
        self.entries = []  # attribute 3
        self.entry_position = 4  # Start at row 4 for entries

        # Instructions Button (Row 0, Column 0)
        self.instructions_button = Button(window, text="Instructions", command=self.show_instructions)
        self.instructions_button.grid(row=0, column=0, padx=5, pady=10)

        # Reset Button (Row 0, Column 1)
        self.reset_button = Button(window, text="Reset", command=self.reset_entries)
        self.reset_button.grid(row=0, column=2)

        # Quit Program Button (Row 0, Column 2)
        self.quit_program_button = Button(window, text="Quit Program", command=self.quit_program)
        self.quit_program_button.grid(row=0, column=3)


        # Student type setup 
        self.student_type_label = Label(window, text="Select your student type:")
        self.student_type_label.grid(row=1, column=0, padx=5, pady=10)

        self.college_student_rb = Radiobutton(window, text="College Student", variable=self.student_type_var, value=self.COLLEGE, command=self.student_type_changed)
        self.college_student_rb.grid(row=2, column=0)

        self.highschool_student_rb = Radiobutton(window, text="High School Student", variable=self.student_type_var, value=self.HIGHSCHOOL, command=self.student_type_changed)
        self.highschool_student_rb.grid(row=2, column=1)

        # Course entry setup (Shifted down by one row)
        self.course_label = Label(window, text="Course Name")
        self.course_label.grid(row=3, column=0)

        self.grade_label = Label(window, text="Grade")
        self.grade_label.grid(row=3, column=1)

        self.credits_semester_label = Label(window, text="# of Credits")
        self.credits_semester_label.grid(row=3, column=2)

        # Add Course Button (Shifted down by one row)
        self.add_course_button = Button(window, text="Add Course", command=self.add_entry)
        self.add_course_button.grid(row=2, column=2, padx = 25, pady=10)

        # Submit Grades Button (Shifted down by one row)
        self.submit_button = Button(window, text="Submit Grades", command=self.submit_grades)
        self.submit_button.grid(row=2, column=3, padx=10, pady=10)

        # Initialize Student (defaults to College Student)
        self.student = Student()

    #Setters
    def set_window(self, window):
        self.window = window
    
    def set_student(self, student):
        self.student = student

    def set_entries(self, entries):
        self.entries = entries
    
    def set_entry_position(self, entry_position):
        self.entry_position = entry_position

    #Getters
    def get_window(self):
        return self.window

    def get_student(self):
        return self.student

    def get_entries(self):
        return self.entries

    def get_entry_position(self):
        return self.entry_position

    def __str__(self):
        return (f"GPA: {unweighted_gpa:.2f}, Weighted GPA: {weighted_gpa:.2f}")

    def show_instructions(self):
        """Displays the instructions in a messagebox."""
        instructions = """Welcome to GPA Calculator!

First, please select the type of student you are. Click either "College Student" or "High School Student".

Then, hit the "Add Course" button (you can do this anytime if you would like to add another course to your calculation).

Make sure you add all valid course information to calculate your GPA. 

If you would like to remove a specific class from calculation, leave # of semesters or # of credits blank.

When sufficient information is entered, click the "Submit Grades" button.

You will then get a popup (like this one) that allows you to see your GPA. If you are in high school, this will include your weighted GPA as well.

If you'd like to reset your grades, simply hit the "Reset" button at the top, and watch it all dissappear.

Once done, hit the "Quit Program" button at the top"""

        messagebox.showinfo("Instructions", instructions)

    def reset_entries(self):
        for entry in self.entries:
            if self.student_type_var.get() == self.HIGHSCHOOL:
                entry[0].destroy()
                entry[1].destroy()
                entry[3].destroy()
                entry[4].destroy()
            else:
                entry[0].destroy()
                entry[1].destroy()
                entry[3].destroy()
        self.set_entries([])
        messagebox.showinfo("Reset Successful!", "All of your inputs have been reset!")

    def quit_program(self):
        self.window.destroy()

    def student_type_changed(self):
        """Updates the student type and adjusts the UI accordingly."""
        if self.student_type_var.get() == self.COLLEGE: 
            self.credits_semester_label.config(text="# of Credits")
            self.remove_ap_checkbox()
            self.set_student(Student(self.COLLEGE))
        elif self.student_type_var.get() == self.HIGHSCHOOL:
            self.credits_semester_label.config(text="# of Semesters")
            self.add_ap_checkbox()
            self.set_student(Student(self.HIGHSCHOOL))

    def add_ap_checkbox(self):
        """Adds the AP checkbox to each entry if the student is in high school."""
        for entry in self.entries:
            if entry[4] is None:  # If there is currently no ap checkbox
                ap_var = IntVar()  # creates IntVar for ap courses
                ap_checkbox = Checkbutton(self.window, text="AP Class", variable=ap_var)
                ap_checkbox.grid(row=entry[0].grid_info()['row'], column=3, pady=5)
                entry[4] = ap_checkbox  # Stores the AP checkbox
                entry[5] = ap_var  # IntVar for the AP checkbox that determines whether it is checked or not

    def remove_ap_checkbox(self):
        """Removes the AP checkbox from each entry if the student is in college."""
        for entry in self.entries:
            if entry[4] is not None:  # If the AP checkbox exists
                entry[4].grid_forget()  # Remove the checkbox from the window
                entry[4] = None  # Set the checkbox to None
                entry[5] = None  # Remove the IntVar

    def add_entry(self):
        """Adds a new row for entering course details."""
        # Create a new row for the course entry
        course_entry = Entry(self.window)
        course_entry.grid(row=self.get_entry_position(), column=0, pady=5)

        # Grade Dropdown (Listbox)
        grade_var = StringVar(self.window)
        grade_var.set("Select")  # Default value
        grade_dropdown = OptionMenu(self.window, grade_var, "A", "B", "C", "D", "F")
        grade_dropdown.grid(row=self.get_entry_position(), column=1, pady=5)

        # Credits/Semesters Entry
        credits_semesters_entry = Entry(self.window)
        credits_semesters_entry.grid(row=self.get_entry_position(), column=2, pady=5)

        # AP Course Checkbox (Only for High School Students)
        ap_checkbox = None
        ap_var = None
        if self.student_type_var.get() == self.HIGHSCHOOL: 
            ap_var = IntVar()  # Create a unique IntVar for this course
            ap_checkbox = Checkbutton(self.window, text="AP Class", variable=ap_var)
            ap_checkbox.grid(row=self.get_entry_position(), column=3, pady=5)
        else:
            ap_var = None  # No AP checkbox for college students

        # Track entries , includes the AP checkbox if it exists, and uses this information for later
        self.entries.append([course_entry, grade_dropdown, grade_var, credits_semesters_entry, ap_checkbox, ap_var])

        # Increment row position for the next course
        self.set_entry_position(self.get_entry_position() + 1)

    def submit_grades(self):
        """Submits the grades and calculates the GPA."""
        # Clear the previous courses from the student object to reset for the new calculation
        self.student.courses = []  # Reset the courses list

        # Checks every entry and collects the course info
        for entry in self.entries:
            course_name = entry[0].get()  # Get the course name
            grade = entry[2].get()  # Get the grade
            credits_or_semesters = entry[3].get()  # Get the credits or semesters
            if entry[5]:
                ap_status = entry[5].get()  # Get the AP status if entry[4] exists
            else:
                ap_status = False  # Set to False if entry[4] does not exist


            # Skip this entry if any field is empty
            if not grade or not credits_or_semesters:
                continue

            # Add course to the student object
            self.student.add_course(course_name, grade, credits_or_semesters, ap=ap_status)

        # Calculate GPA
        unweighted_gpa, weighted_gpa = self.student.calculate_gpa()

        # Optionally display the GPA in a message box
        if self.student.student_type == self.HIGHSCHOOL:
            messagebox.showinfo("GPA Calculation", f"GPA: {unweighted_gpa:.2f}\nWeighted GPA: {weighted_gpa:.2f}")
        else:
            messagebox.showinfo("GPA Calculation", f"GPA: {unweighted_gpa:.2f}")
