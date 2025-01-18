class Student:
    def __init__(self, student_type):
        """
        Initializes a Student object with a specified student type.
        This is the parametized constructor
        """
        self.student_type = student_type  # 0 for college, 1 for high school #Attribute 1
        self.courses = []  # List to store courses #ATTRIBUTE 2
        self.unweighted_gpa = float(0) #ATTRIBUTE 3
        self.weighted_gpa = float(0) #ATTRIBUTE 4

    def __init__(self, student_type = 0):
        """
        Default constructor that defaults to college student if no student type is used when creating object
        """
        self.student_type = student_type
        self.courses = []  # List to store courses
        self.unweighted_gpa = float(0)
        self.weighted_gpa = float(0)

    # Setter methods for student_type
    def set_courses(self, courses):
        self.courses = courses

    def set_student_type(self, student_type):
        self.student_type = student_type

    def set_unweighted_gpa(self, unweighted_gpa):
        self.unweighted_gpa = unweighted_gpa

    def set_weighted_gpa(self, weighted_gpa):
        self.weighted_gpa = weighted_gpa

    # Getter methods for courses
    def get_courses(self):
        return self.courses

    def get_student_type(self):
        return self.student_type

    def get_unweighted_gpa(self):
        return self.unweighted_gpa

    def get_weighted_gpa(self):
        return self.weighted_gpa

    def __str__(self):
        """
        Returns a string including the type of student and course list.
        """
        if self.student_type == 1 :
            return f"Student Type: {'High School'}\nCourses: {self.courses}"
        else:
            return f"Student Type: {'College'}\nCourses: {self.courses}"
    
    def add_course(self, course_name, grade, credits_or_semesters, ap=False):
        """
        Adds a course to the student's list of courses with its grade, credits (or semesters), and AP status.
        """
        self.courses.append({
            "course_name": course_name,
            "grade": grade,
            "credits_or_semesters": credits_or_semesters,
            "ap": ap
        })

    def grade_to_points(self, grade, weighted=False):
        """
        Converts a letter grade to GPA points. Optionally applies a weighted scale for AP courses.
        """
        grade_points = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        
        # Apply weighted scale for AP courses if student is in high school
        if self.student_type == 1 and weighted:  # High school students with AP courses
            grade_points = {
                "A": 5.0,
                "B": 4.0,
                "C": 3.0,
                "D": 2.0,
                "F": 0.0
            }
        
        return grade_points.get(grade.upper(), 0.0)  # Default to 0.0 if grade is invalid

    def calculate_gpa(self):
        """
        Calculates the unweighted and weighted GPA for the student based on their courses.
        """
        total_points = 0
        total_credits = 0
        total_weighted_points = 0

        for course in self.courses:
            grade = course["grade"]
            credits_or_semesters = course["credits_or_semesters"]
            
            # Skip the course if credits_or_semesters is empty
            if not credits_or_semesters:  # If it's empty or None, skip this course
                continue
            
            try:
                credits = float(credits_or_semesters)  # Convert to float
            except ValueError:
                continue  # Skip this course if credits_or_semesters is invalid
            
            # Convert grade to points
            grade_points = self.grade_to_points(grade)
            
            # Add points to total
            total_points += grade_points * credits
            total_credits += credits
            
            # If AP, use weighted GPA (5-point scale)
            if course.get("ap"):
                weighted_points = self.grade_to_points(grade, weighted=True)
                total_weighted_points += weighted_points * credits
            else:
                total_weighted_points += grade_points * credits
        
        # Calculate GPAs
        if total_credits == 0: # Avoid division by zero if no valid courses are entered
            self.set_unweighted_gpa(0)
            self.set_weighted_gpa(0)  
        else:
            self.set_unweighted_gpa(total_points / total_credits)
            self.set_weighted_gpa(total_weighted_points / total_credits)
        return self.get_unweighted_gpa(), self.get_weighted_gpa()
