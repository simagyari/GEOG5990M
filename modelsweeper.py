import subprocess
from distutils.util import strtobool

agent_range = range(10, 50, 10)
for item in agent_range:
    command = 'python model.py {} {} {}'.format(item, 100, 20)
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
