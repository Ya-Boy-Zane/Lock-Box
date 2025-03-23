import sys
import os
module_dir = os.path.dirname(os.path.abspath(__file__))
if module_dir not in sys.path:
    sys.path.append(module_dir)
import data_manager as dat
import os
import json
from colorama import Fore
import time

#Path to storage
storage = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__,".."))),"Storage")
data = os.path.join(storage,"data.json")
site_file = os.path.join(storage,"sites.txt")

#Storage
def store(site,user,pas):
    try:
        inp = {str(site):{str(user):str(pas)}}
        with open(data,'r') as d:
            passes = json.load(d)
            passes.update(inp)
        with open(data,'w') as op:
            json.dump(passes,op)
    except FileNotFoundError:
        print("DATA FILE WAS NOT FOUND")
    except Exception as e:
        print(f"UNKNOWN ERROR : {e}")

#Add Password
def add_pass(name_of_site,user,pas):
    enc_pass = dat.encrypt(pas)
    store(name_of_site,user,enc_pass)

#Find Password
def find_pass(name_of_site):
    try:
        with open(data,'r') as of:
            passes = json.load(of)
            spec_data = passes.get(name_of_site)
        if spec_data == None:
            user,pas = None,None
            print(Fore.YELLOW+"Error:Site not found")
            return user,pas
        else:
            for i in spec_data.keys():
                user = i
            for i in spec_data.values():
                pas = i
            pas = dat.decrypt(pas)
            return user,pas
    except FileNotFoundError:
        print(Fore.YELLOW+"Error:File not found")
    except Exception as e:
        print(Fore.YELLOW+f"Unknown Error: {e}")

def sites(tsk,site):
    found = False
    match tsk:
        case "find":
            with open(site_file,'r') as f:
                sites = f.readlines()
                if any(line.strip()==site for line in sites):
                    found = True
                else:
                    found = False
                return found
        case "add":
            with open(site_file,'a+') as a:
                sites  = a.readlines()

                if site in sites:
                        pass
                else:
                        a.write(f"\n{site}")
        case "all":
            with open(site_file,'r') as r:
                sites  = r.readlines()
                if not sites:
                    print(Fore.YELLOW+"You Do not have any saved data")
                else:
                    counter = 0
                    print(Fore.GREEN+"------------------")
                    for line in sites:
                        if counter <= 0:
                            counter = counter+1
                        else:
                            print(Fore.GREEN+str(counter)+"."+Fore.MAGENTA+line)
                            counter = counter+1
                    print(Fore.GREEN+"------------------")

