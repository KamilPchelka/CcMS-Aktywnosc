class ManagerView:

    @staticmethod
    def display_manager_menu():
        print('1. Promote user to Mentor\n' +
              '2. Remove Mentor\n' +
              '3. Edit Mentor data\n' +
              '4. Display list of Mentors\n' +
              '5. Display list of students')

    @staticmethod
    def display_users(self, users):
        for k, v in enumerate(users):
            print(k+1 + '. ' + str(v))

    @staticmethod
    def get_promotion_input(self):
        return input('Enter login of the user which do you want to promote to Mentor: ')
