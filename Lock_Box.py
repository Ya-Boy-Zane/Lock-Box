from Manager import data_manager
import time
from Manager.system_manager  import find_pass as find
from Manager.system_manager import add_pass as add

from colorama import Fore

def cli():
    user = input(Fore.GREEN+">>>>").lower()
    return str(user)

#Sytem msgs- Dark green
#Script msgs - light green
#Failiures - Red
#Warnings  - yellow

print(Fore.LIGHTGREEN_EX+"WELCOME TO LOCK BOX")
print(Fore.LIGHTGREEN_EX+"\nOptions:")
print(Fore.LIGHTGREEN_EX+"\t1.Find saved password (f)")
print(Fore.LIGHTGREEN_EX+"\t2.Add new password(a)")
print(Fore.LIGHTGREEN_EX+"\t3.Change existing password(c)")
session = 0
while True:
    choice = cli()
    if choice == "f":
        print(Fore.LIGHTGREEN_EX+"Please mention the name of the site",Fore.LIGHTGREEN_EX+"(Press 's' to get list of saved sites)")
        inp = input(Fore.LIGHTGREEN_EX+"Site:").lower()
        if inp == "s":
            pass
        else:
            user,pas = find(inp)
            if user == None :
                pass
            else:
                 print(Fore.LIGHTGREEN_EX+"\nUser: "+Fore.MAGENTA+str(user)+Fore.GREEN+"\nPassword: "+Fore.MAGENTA+str(pas))
    elif choice == "a":
        print("-----------------------------------------")
        site = input("Name of site:")
        usr = input("Username:")
        pas = input("Password:")
        veri = input("Are you sure(y/n)?:").lower()
        if veri == "y":
                add(site,usr,pas)
                break
    elif choice == "c":
        pass
    else:
        print(Fore.YELLOW+"Invalid input: Unrecognized Option/Command")
        break

