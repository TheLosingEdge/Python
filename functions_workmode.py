import os

#Function that runs systeminfo and saves to a text file
def sys_info():
    return os.system("systeminfo > sysinfo.txt")

#Runs function
sys_info()
