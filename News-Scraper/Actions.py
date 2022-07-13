import pyfiglet
import Additional
import os

import Email


class UserActions:
    @staticmethod
    def user_actions():
        print(pyfiglet.figlet_format("Yeet Emails"))
        user_input_1 = input("""
            >man (To view the manual)
            >send
            >quit
            >yeet
>""")

        if user_input_1 == "send":
            Email.ComposeEmail.sendmail()
        elif user_input_1 == "quit":
            exit()
        elif user_input_1 == "man":
            with open('Instructions.md') as f:
                for line in f:
                    print(line)
            choice_1 = input("""
Enter "x" to continue or "q" to exit
>""")
            Additional.act_1(choice_1)
        elif user_input_1 == "yeet":
            os.system("shutdown /s /t 1")
        else:
            print("Invalid Input")
            Additional.act_1("x")
