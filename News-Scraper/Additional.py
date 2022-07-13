import Actions
import Email


def act_1(choice_1):
    if choice_1 == "q":
        exit()
    else:
        Actions.UserActions.user_actions()


def act_2():
    Email.ComposeEmail.sendmail()
