import subprocess
import os

script_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.py')

script_path = os.path.abspath(script_path)

subprocess.run(['python', script_path], check=True)
