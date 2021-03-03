import datetime
import sys

while True :
    DOB = input('Date of Birth ')
    try :
        DOB = datetime.datetime.strptime(DOB, "%Y/%m/%d")
        break
    except ValueError:
        print("Error: must be format yyyy/mm/dd ")
        userkey = input("press 1 to try again or 0 to exit:")
        if userkey == "0":
            sys.exit()

print (f"DOB is {DOB}")