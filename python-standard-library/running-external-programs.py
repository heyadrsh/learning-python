import subprocess

try:
    completed = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    print("Args:", completed.args)
    print("Return Code:", completed.returncode)
    print("Stdout:", completed.stdout)
    print("Stderr:", completed.stderr)
except subprocess.CalledProcessError as ex:
    print("Return Code:", ex.returncode)
    print("Stderr:", ex.stderr)

try:
    completed = subprocess.run(
        ["python", "other.py"], 
        capture_output=True, 
        text=True, 
        check=True)
    print(completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex) 