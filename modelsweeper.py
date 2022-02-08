import subprocess

agent_range = range(10, 100, 10)
for item in agent_range:
    command = 'python model.py {} {} {}'.format(item, 100, 20)
    subprocess.run(command)
