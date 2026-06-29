import subprocess

def run():
    print("\n[CRON SCAN]")

    print(subprocess.getoutput("cat /etc/crontab"))
