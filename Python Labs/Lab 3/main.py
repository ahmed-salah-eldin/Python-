import Register as Register
import Login as Login


def viewMainOptions():
    value = input("Choose on option:\n1)Register\n2)Login\n")
    if value.isdigit():
        if int(value) == 1:
            Register.registerUser()
            viewMainOptions()
        elif int(value) == 2:
            Login.loginUser()
            viewMainOptions()
        else:
            print("wrong number")
            viewMainOptions()
    else:
        print("wrong value")
        viewMainOptions()


viewMainOptions()
