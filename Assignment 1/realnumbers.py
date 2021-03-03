import math

def get_num():
    userdata = input("Enter an number, or 'q' to quit: ")
    if userdata == 'q':
        return None
    try:
        user_num = float(userdata)

        print("The value of ",userdata, "on applying floor() function is:", math.floor(user_num))
        print("The value of ",userdata, "on applying ceil() function is:", math.ceil(user_num))
        print("The value of ",userdata, "on applying round() function is:", round(user_num))

        return user_num
    except ValueError:
        print("Sorry, I need a number to continue.")
        return(get_num())

user_number = get_num()