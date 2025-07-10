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
                           5. Press 5 to Exit
                           --> """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

    def signup(self):
        email = input("Enter Your Email: ")
        pwd = input("Enter your Password: ")
        self.username = email
        self.password = pwd
        print("!! You have Signned Up Successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please Signin first by Pressing 1 in the main menu")
        else:
            uname = input("Enter You Email: ")
            pwd = input("Enter Your Password: ")

            if self.username == uname and self.password == pwd:
                print("!! You have Signed In Successfull !!")
                self.loggin = True
            else:
                print("Please Enter the Correct Credientials....")

        print("\n")
        self.menu()


obj = chatbook()