"""
This module defines the Student class and demonstrates its functionality.
It includes methods for managing grades, calculating averages, and generating reports.
"""
class Student:
    """
    Represents a student with an ID, name, grades, and other attributes.
    Provides methods to manage grades and calculate averages.
    """
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = None
    def add_grade(self,grade):
        """
        Adds a grade to the student's list of grades.

        Args:
            grade (int): The grade to add.
        """
        self.grades.append(grade)
    def calc_average(self):
        """
        Calculates the average of the student's grades.

        Returns:
            float: The average grade, or 0 if there are no grades.
        """
        if not self.grades:
            return 0
        return sum(self.grades/ len(self.grades ))
    def check_honor(self):
        """
        Checks if the student's average grade is above 90.
        If so, sets the honor attribute to 'yep'.
        """
        if self.calc_average()>90:
            self.honor = "Yes"
        else:
            self.honor = "No"
    def delete_grade(self, index):
        """
        Deletes a grade from the student's list of grades by index.

        Args:
            index (int): The index of the grade to delete.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("index is out of range")
    def report(self):
        """
        Prints a report of the student's details, including ID, name,
        number of grades, and average grade.
        """
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        average = self.calc_average()
        print(f"Average Grade: {average:.2f}")
        print(f"Honor Roll: {self.honor}")
def start_run():
    """
    Demonstrates the functionality of the Student class by creating
    a student, adding grades, calculating averages, and printing a report.
    """
    student = Student("x01", "Sebastian Arguello")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.check_honor()
    student.delete_grade(5)
    student.report()
start_run()
