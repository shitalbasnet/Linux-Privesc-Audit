import subprocess

def run():
    print("\n[KERNEL INFORMATION]")

    print(subprocess.getoutput(
        "uname -a"
    ))
