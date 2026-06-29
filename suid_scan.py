import subprocess

def run():
    print("\n[SUID SCAN]")

    result = subprocess.getoutput(
        "find / -perm -4000 -type f 2>/dev/null"
    )

    print(result)
