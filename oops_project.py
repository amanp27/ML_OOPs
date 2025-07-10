class chatbook:

    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to the CHATBOOK !! How would you like to proceed.
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to Write a post
                           4. Press 4 to message a friend
                           5. Press 5to Exit
                           --> """)
        
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        else:
            exit()


obj = chatbook()