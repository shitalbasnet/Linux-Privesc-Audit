import subprocess

def run():
    print("\n[SUDO SCAN]")

    print(subprocess.getoutput("sudo -l"))
