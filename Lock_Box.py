from Manager import system_manager
import time
from colorama import Fore
import subprocess

def cli():
    user = input(Fore.GREEN+">>>>"+Fore.LIGHTCYAN_EX).lower()
    return user                   
def option(choice):
    #Finding password

    if choice == "find":
        print(Fore.LIGHTGREEN_EX+"Please mention the name of the site",Fore.LIGHTGREEN_EX+"(Use the 'saved' command to get a list of saved sites)")
        inp = input(Fore.LIGHTGREEN_EX+"Identifier:"+Fore.LIGHTCYAN_EX)
        if inp == "saved":
            sites = system_manager.sites("all",None)
        else:
            user,pas = system_manager.find_pass(inp)
            if user == None :
                print(Fore.YELLOW+"Cannot find data,please check spellings and try again")
            else:
                 print(Fore.BLUE+"Data found")
                 time.sleep(1)
                 print()
                 print(Fore.LIGHTBLACK_EX+"-----------------------------------------")
                 print(Fore.LIGHTGREEN_EX+"User: "+Fore.MAGENTA+str(user)+Fore.GREEN+"\nPassword: "+Fore.MAGENTA+str(pas))
                 print(Fore.LIGHTBLACK_EX+"-----------------------------------------")
                 print()
    #Adding password
    elif choice == "add":
        print(Fore.GREEN+"\nPlease make sure to use correct"+Fore.LIGHTGREEN_EX+" spellings and capitalization for the Identifier name, "+Fore.GREEN+"it will be used to identify your data in the data base.")
        print("-----------------------------------------")
        site = input(Fore.LIGHTGREEN_EX+"Website/App/Identifier:"+Fore.WHITE)
        usr = input(Fore.GREEN+"Username:"+Fore.WHITE)
        pas = input(Fore.GREEN+"Password:"+Fore.WHITE)
        print(Fore.GREEN+"-----------------------------------------")
        veri = input("Are you sure(y/n)?:").lower()
        if veri == "y":
                system_manager.add_pass(site,usr,pas)
                system_manager.sites('add',site)
                print(Fore.BLUE+"Password succesfully added to database")
        elif veri == "n":
            pass
        else:
            pass
    #changing password
    elif choice == "change":
        print(Fore.GREEN+"Please remember to enter the name of the password Identifier correctly.")
        inp = input("website/App/Identifier:"+Fore.WHITE)
        if system_manager.sites('find',inp):
            print(Fore.BLUE+"Site exsists, fetching data.")
            time.sleep(1.5)
            print(Fore.GREEN+"-----------------------------------------")
            usr = input(Fore.GREEN+"New Username:"+Fore.WHITE)
            pas = input(Fore.GREEN+"New Password:"+Fore.WHITE)
            print(Fore.GREEN+"-----------------------------------------")
            veri = input(Fore.GREEN+"Are you sure(y/n)?:").lower()
            if veri == "y":
                system_manager.add_pass(inp,usr,pas)
                time.sleep(1)
                print(Fore.BLUE+"Successfully changed existing data.")
            else:
                pass
        else:
            print(Fore.YELLOW+"Site doesnt exsist(please check spellings/capitalization and try again.)")

    elif choice == "saved":
        system_manager.sites('all',None)
    else:
        print(Fore.YELLOW+"Invalid input: Unrecognized Option/Command")

txt_art = Fore.MAGENTA+'''


██╗      █████╗  █████╗ ██╗  ██╗  ██████╗  █████╗ ██╗  ██╗
██║     ██╔══██╗██╔══██╗██║ ██╔╝  ██╔══██╗██╔══██╗╚██╗██╔╝
██║     ██║  ██║██║  ╚═╝█████═╝   ██████╦╝██║  ██║ ╚███╔╝
██║     ██║  ██║██║  ██╗██╔═██╗   ██╔══██╗██║  ██║ ██╔██╗
███████╗╚█████╔╝╚█████╔╝██║ ╚██╗  ██████╦╝╚█████╔╝██╔╝╚██╗
╚══════╝ ╚════╝  ╚════╝ ╚═╝  ╚═╝  ╚═════╝  ╚════╝ ╚═╝  ╚═╝

'''
print(txt_art)
print(Fore.GREEN+"NOTE:Please read the text file called"+Fore.WHITE+' Manual '+Fore.GREEN+"in the main directory of the program for more information about Lock box.")
print(Fore.GREEN+"-------------------------------------------------------------------------------")
print(Fore.LIGHTGREEN_EX+"System Commands:")
print(Fore.CYAN+"\t1.exit - Exit full program")
print(Fore.GREEN+"-------------------------------------------------------------------------------")
print(Fore.LIGHTGREEN_EX+"Program Commands:")
print(Fore.LIGHTCYAN_EX+"\t1.find - Find saved data(passwords)")
print("\t2.add - Add new data(password)")
print("\t3.change - Change existing data(passwords)")
print("\t4.saved - Get a list of all the names of the sites saved")
print(Fore.GREEN+"-------------------------------------------------------------------------------")
while True:
    choice = cli()
    if choice =='exit':
        break
    else:
        option(choice)

