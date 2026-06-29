import subprocess

def run():
    print("\n[CAPABILITY SCAN]")

    print(subprocess.getoutput(
        "getcap -r / 2>/dev/null"
    ))
