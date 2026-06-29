import subprocess

def run():
    print("\n[PERMISSION SCAN]")

    result = subprocess.getoutput(
        "find / -type f -perm -002 2>/dev/null"
    )

    print(result)
