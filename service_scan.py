import subprocess

def run():
    print("\n[SYSTEMD SERVICES]")

    print(subprocess.getoutput(
        "systemctl list-unit-files"
    ))
