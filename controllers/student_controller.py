from student import Student
from user_container import UserContainer
from student_view import StudentView


class StudentController:

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.user_container = UserContainer.get_instance

    def start():
        ...

    @classmethod
    def get_instance(cls):
        """
        Returns the singleton instance of Controller
        :return: None
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = StudentController()
        return cls.INSTANCE

    def show_student_grades(self, student_login):
        """
        Show grades for student with given student login
        """
        users = self.user_container.get_users_list()
        students = [pupil for pupil in users if isinstance(pupil, Student)]
        for pupil in students:
            if pupil.get_login() == student_login:
                grades_list = pupil.get_grades()
        else:
            raise ValueError('No student with this login!')
        StudentView.display_student_grades(grades_list)  # Todo in StudentView

    def submit_assignment(self, student_login, assignment_name):
        """
        Add new key to submissions with assignment_name
        """
        users = self.user_container.get_users_list()
        students = [pupil for pupil in users if isinstance(pupil, Student)]
        for pupil in students:
            if pupil.get_login() == student_login:
                pupil.submissions[assignment_name] = self.get_submission_input(assignment_name)
        else:
            raise ValueError('No student with this login!')
        StudentView.display_submission_result()  # Todo in StudentView

    @staticmethod
    def get_submission_input(assignment_name):
        submission = input('Assignment: {} Enter link with your submission: '.format(assignment_name))
        return submission
