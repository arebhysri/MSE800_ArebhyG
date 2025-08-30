class Course:
    def __init__(self, course_name, course_code, credits):
        self.__course_name = course_name
        self.__course_code = course_code
        self._credits = credits

    # Getter and setter for course name
    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, value):
        self.__course_name = value

    # Getter and setter for course code
    def get_course_code(self):
        return self.__course_code

    def set_course_code(self, value):
        self.__course_code = value

    # Getter and setter for credits
    def get_credit(self):
        return self._credits

    def set_credit(self, value):
        if isinstance(value, int) and value > 0:
            self._credits = value
        else:
            print("Invalid credit. It must be a positive integer.")

    # Course info summary
    def get_course_info(self):
        return f"{self.__course_code}: {self.__course_name} ({self._credits} credits)"
