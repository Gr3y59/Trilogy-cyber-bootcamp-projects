# Administrator accounts list
import sys
import datetime
now = datetime.datetime.now().strftime("%c")
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

#takes user input for username and password and stores in userinfo variable and returns it
def getCreds():
    username = input("What is your user name?: ")
    print("----------------------------")
    userpassword = input("What is your password?: ")
    print("----------------------------")
    print("----------------------------")
    userinfo = {'username' : username}
    userinfo['password'] = userpassword
    return userinfo

#checks if creds are in adminlist if not program exits after 6 tries
def checkLogin(userinfo, adminList):
    incorrect = 0
    max_tries = 5
    if userinfo in adminList:
       print(":LOGGED IN SUCCESSFULLY:")
    if userinfo not in adminList:
        print(":FAILED LOGGIN 5 ATTEMPTS LEFT!:")
    while userinfo not in adminList:
        if userinfo not in adminList:
            #Creates UserAdminLogs.txt in current directory of the script is doesnt exist then logs the bad creds
            #in the file along with date and time
            Logs = open("UserAdminLogs.txt", "a")
            Logs.write("\nFailed Loggin Attempt at " + now + "\n------------------------" + "\nusername: " + userinfo['username'] + "\npassword: " + userinfo['password'] + "\n-------------------------------------")
            Logs.close()

        userinfo = getCreds()
        incorrect += 1
        trysleft = max_tries - incorrect
        if trysleft == 0:
            Logs = open("UserAdminLogs.txt", "a")
            Logs.write("\nFailed Loggin Attempt at " + now + "\n------------------------" + "\nusername: " + userinfo['username'] + "\npassword: " + userinfo['password'] + "\n-------------------------------------")
            Logs.close()
            sys.exit(1)
        if userinfo in adminList:
            print(":LOGGED IN SUCCESSFULLY:")


userinfo = getCreds()
checkedlogin = checkLogin(userinfo, adminList)












