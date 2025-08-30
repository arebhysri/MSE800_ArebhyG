from course import Course
from student import Student

class Enrollment:
    def __init__(self, student: Student):
        self._student = student
        self._courses = []

    def enroll_course(self, course: Course):
        self._courses.append(course)

    def list_courses(self):
        return [course.get_course_info() for course in self._courses]

    def print_summary(self):
        print(f"Student: {self._student.get_name()}")
        print(f"Age: {self._student.get_age()}")
        print(f"Grade: {self._student.get_grade()}")
        print(f"Address: {self._student.get_address()}")
        print("Enrolled Courses:")
        for info in self.list_courses():
            print(f" - {info}")

if __name__ == "__main__":
    # Create student
    s = Student("Ali", 20, "City Road Auckland")

    # Create courses
    c1 = Course("Mathematics", "MATH101", 3)
    c2 = Course("Physics", "PHYS201", 4)

    # Enroll student in courses
    enrollment = Enrollment(s)
    enrollment.enroll_course(c1)
    enrollment.enroll_course(c2)

    # Print enrollment summary
    print("\nEnrollment Summary:")
    enrollment.print_summary()
