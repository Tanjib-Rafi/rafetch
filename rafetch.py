import distro
import platform
import subprocess
import os
import re
import random
import cv2
import socket
import psutil
import getpass
from cpuinfo  import get_cpu_info
from colorama import Fore, Back, Style


#get username
def getUser():
  return getpass.getuser()

#get the operating system
def getOS():
    os = distro.name() + ' ' + distro.version() + ' ' + platform.architecture()[0]
    if not None:
        os += ' '
    return os

#get host name
def getHost():
  return socket.gethostname()

#get pc model name
def getModel():
    m = subprocess.check_output("sudo dmidecode | grep -A3 '^System Information'", shell=True, universal_newlines=True)
    n=m.split('\n')[2]
    n1=n.split(' ')[2:]
    model=""
    for i in n1:
      model +=i + ' '
    return model

#get desktop environment
def getDE():
  return os.environ.get('DESKTOP_SESSION')

#get used and total memory size
def getRAM():
  ram = str(round(psutil.virtual_memory().used / (1024.0 **3),2))+" GB" + ' / ' +  str(round(psutil.virtual_memory().total / (1024.0 **3),2))+" GB"
  return ram

#get used and total disk space
def getDisk():
  partitions = psutil.disk_partitions()
  for partition in partitions:
      try:
          partition_usage = psutil.disk_usage(partition.mountpoint)
      except PermissionError:
          continue
      disk = str(round(partition_usage.used / (1024.0 **3),2))+" GB" + ' / ' + str(round(partition_usage.total / (1024.0 **3),2))+" GB"
      break
  return disk

#get kernel
def getKernel():
    kernel = platform.release()
    if kernel:
        return kernel
    return None

# get uptime
def getUptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_hours = uptime_seconds / 3600
        uptime_days = int(uptime_hours /24)
        uptime_minutes = (uptime_hours - int(uptime_hours)) * 60
        uptime_hours = int(uptime_hours)
        uptime_minutes = int(uptime_minutes)
        time = ''

        if uptime_days == 1:
            time = str(uptime_days) + ' day, '
        elif uptime_days == 0 :
          pass
        else:
            time = str(uptime_days) + ' days, '

        if uptime_hours <= 1:
            time += str(uptime_hours) + ' hour, '
        elif uptime_hours >= 24:
            hours = uptime_hours - 24
            time += str(hours) + ' hours, '
        else:
            time += str(uptime_hours) + ' hours, '

        if uptime_hours == 0:
            time += str(uptime_minutes) + ' min'
        else:
            time += str(uptime_minutes) + ' mins'

    return time


# get the number of dpkg,snap & flatpak packages
def getPackages():
    try:

      if os.path.exists("/bin/dpkg"):
        dpkgPackages = subprocess.check_output("echo $((`dpkg --list | wc -l` - 5))", shell=True, universal_newlines=True)
      if os.path.exists("/snap"):
        snapPackages = subprocess.check_output("echo $((`snap list | wc -l` - 1))", shell=True, universal_newlines=True)
      if os.path.exists("/bin/flatpak"):
        flatpakPackages = subprocess.check_output("echo $((`flatpak list | wc -l`))", shell=True, universal_newlines=True)


      dpkg = str(dpkgPackages.split('\n')[0])
      snap = str(snapPackages.split('\n')[0])
      flatpak = str(flatpakPackages.split('\n')[0])


      if dpkg!=0:
          info = dpkg + ' (dpkg)'
      if snap!=0:
          info += ', ' + snap + ' (snap)'
      if flatpak!='0':
          info += ', ' + flatpak + ' (flatpak)' 
        
      return info
        
    except:
        return None

#get window manager
def getWM():
    try:      
        output = subprocess.run(['wmctrl', '-m'], text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if output.stdout:
            name=output.stdout.split('\n')[0]
            wm=name.split(' ')[1]
        return wm
    except:
        return None

#get the shell
def getShell():
    path = os.readlink('/proc/%d/exe' % os.getppid())
    sh = re.search(r"/.+/(.+)" , path)
    return sh.group(1)

#get the terminal
def getTerminal():
    terminal = subprocess.check_output("echo $TERM", shell=True, universal_newlines=True)
    return terminal




if __name__ == "__main__":
    f = open("./output.txt", "w") 

    f.write(f"\u001b[36;1m {Fore.RED}{getUser()}{Fore.GREEN}@{Fore.YELLOW}{Fore.MAGENTA}{getHost()}{Fore.CYAN}\n")
    f.write(f"\u001b[36;1m ----------\n\n")

    f.write(f"\u001b[36;1m OS: {getOS()}\n")
    f.write(f"\u001b[35;1m Host: {getModel()}\n")
    f.write(f"\u001b[34;1m Kernel: {getKernel()}\n")
    f.write(f"\u001b[33;1m Packages: {getPackages()}\n")
    f.write(f"\u001b[33;1m DE: {getDE()}\n")
    f.write(f"\u001b[32;1m Shell: {getShell()}\n")
    f.write(f"\u001b[31;1m Terminal: {getTerminal()}")
    f.write(f"\u001b[30;1m WM: {getWM()}\n")
    f.write(f"\033[92m Disk: {getDisk()}\n")
    f.write(f"\u001b[37;1m RAM: {getRAM()}\n")
    f.write(f"\u001b[36;1m Uptime: {getUptime()}\n")
    f.close()


img="img/superman.png"
img1="img/batman.png"
img2="img/spiderman.png"
img3="img/pika2.png"
img4="img/captainamerica.png"
img5="img/spiderman2.png"
img6="img/ironmanp1.png"
img7="img/panda.png"
img8="img/poki1.png"
img9="img/poki3.png"
img10="img/joker.png"
img11="img/tom.png"
img12="img/tank.png"
img13="img/logo.png"
img14="img/racoon.png"
img15="img/black.png"
img16="img/hawk.png"
img17="img/dragon.png"
img18="img/cap.png"
img19="img/thor2.png"
img20="img/dead.png"
img21="img/aqua.png"
img22="img/hulk.png"
img23="img/thanos.png"


p2=cv2.imread((random.choice([img,img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14,img15,img16,img17,img18,img19,img20,img21,img22,img23])))


#removing black background color and make it transparent
tmp = cv2.cvtColor(p2, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(p2)
rgba = [b,g,r, alpha]
p3 = cv2.merge(rgba,4)

cv2.imwrite("tux.png",p3)
