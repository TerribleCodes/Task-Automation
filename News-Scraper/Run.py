import pyfiglet
import os
import Email


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
        if choice_1 == "q":
            exit()
        else:
            user_actions()
    elif user_input_1 == "yeet":
        os.system("shutdown /s /t 1")
    else:
        print("Invalid Input")
        user_actions()


user_actions()
