import os
import subprocess

# Get the absolute path of the directory to add
directory_to_add = os.path.abspath(r".\bin")
print(directory_to_add)

result = subprocess.run(f'setx /M PATH "%PATH%;{directory_to_add};"', shell=True)
print(f"Stdout: {result.stdout}")
print(f"Stderr: {result.stderr}")

