import subprocess


# Define sweeped parameter
agent_range = range(10, 50, 10)

# Loop through variables and run subprocesses with each
for item in agent_range:
    command = 'python model.py {} {} {} --multirun {}'.format(item, 100, 20, 1)
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)  # Nullifies output to enhance speed
