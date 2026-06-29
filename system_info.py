import os
import platform
import subprocess

def run():
    print("="*50)
    print("SYSTEM INFORMATION")
    print("="*50)

    print("User :", os.getlogin())
    print("Kernel :", platform.release())

    os_info = subprocess.getoutput("cat /etc/os-release | grep PRETTY_NAME")
    print(os_info)
