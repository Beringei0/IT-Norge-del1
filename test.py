import platform
import socket
import os
import shutil
import subprocess
import inspect as i



hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
total, use, free = shutil.disk_usage("/")
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
s = str(Data)
sysOS = platform.platform()
user = os.getlogin()
free = free//(2**30)




dict = {
    "Host":hostname, 
    "sysOS":sysOS,
    "ip":ip,
    "User":user,
    "Free":free,
}

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

write()













