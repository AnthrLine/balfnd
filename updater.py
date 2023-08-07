import subprocess
import os

awake_gunicorn = ["gunicorn3", "--workers=1", "main:app", "--daemon"]

def completeupdate():
    os.system("sudo pkill gunicorn3")
    print("KILLED GUNICORN")
    awake = subprocess.run(awake_gunicorn)
    print("GUNICORN ON")
    print(awake.returncode)
