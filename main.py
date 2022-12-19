import platform
import socket
import os
import shutil
import subprocess
#----------------Imported modules 

hostname = socket.gethostname()# gets hostname from pc
ip = socket.gethostbyname(hostname)# gets ip from pc 
total, use, free = shutil.disk_usage("/")# gets disk usage from pc 
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])# gets installed products from pc
s = str(Data)# converts data var to string 
sysOS = platform.platform()# gets installed OS
user = os.getlogin()# gets user 
free = free//(2**30)# converts to GB
#-------------------All variables 



dict = {
    "Host":hostname, 
    "sysOS":sysOS,
    "ip":ip,
    "User":user,
    "Free":free,
}
#-----------------All vars stored in dict 


def write():
 f = open("test.txt", "w")
 f.write("Host: "+str(dict["Host"])+"\n")
 f.write("sysOS: "+str(dict["sysOS"])+"\n")
 f.write("ip: "+str(dict["ip"])+"\n")
 f.write("User: "+str(dict["User"])+"\n")
 f.write("Free: "+str(dict["Free"])+"GB\n")
 try:

     for i in range(len(s)):
         f.write(("programmer: "+s.split("\\r\\r\\n")[6:][i])+"\n")
 except IndexError as e:
       print("Ferdig")
#----------------------------Function that writes to txt file 

write()













