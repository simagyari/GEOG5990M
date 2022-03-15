import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agentframework
import agentstorage
import csv
import random
import argparse
import tkinter
import requests
import bs4


# Quitter function from tkinter loop
# From: https://stackoverflow.com/a/55206851
def quit_me() -> None:
    """Quit and destroy the tkinter mainloop on closing the model GUI window."""
    print('Quitting model runner!')
    root.quit()
    root.destroy()


# Updates agents one by one
def update(frame_number) -> None:
    """
    Update agent position and behaviour.

    Parameters
    ----------
    frame_number : int
        Set automatically to equal number of model iterations, only used in animation.

    Returns
    -------
    None

    """
    fig.clear()  # clears scatter points from earlier iteration
    random.shuffle(agents)  # shuffle agents to eliminate position-based advantages
    for a in range(num_of_agents):
        agents[a].eat()
    for a in range(num_of_agents):
        agents[a].move()
    for a in range(num_of_agents):
        agents[a].share_with_neighbours(neighbourhood)
    for a in range(num_of_agents):
        agents[a].share_eater()
    for a in range(num_of_agents):
        agents[a].sick()
    # Plot agents on a scatterplot recursively adding points onto the environment raster (only on single model run)
    plt.imshow(environment)
    for b in range(num_of_agents):
        plt.scatter(agents[b].x, agents[b].y)


# Create and display animation, write outputs
def run() -> None:
    """Run the model animation and record output."""
    # Defining animation part with stopping at num_of_iterations and no looping
    animation = FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    # Only draw result when there is no parameter sweeping
    canvas.draw()

    # Write environment to outfile
    env_writer('out.txt')

    # Print overall and one-by-one agent storage, record in storage.txt
    agentstorage.all_storage_writer(agents, 'storage.txt')
    agentstorage.agent_storage_writer(agents, 'storage.txt')

    # Print agents
    agent_printer(agents)


# Read environment file to nested list
def env_reader(infile: str) -> list:
    """
    Read environment list from infile.

    Parameters
    ----------
    infile : str
        Name of the file containing the environment list.

    Returns
    -------
    list
        Nested (2D) list of the environment.
    """
    with open(infile, 'r') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  # QUOTE_NONNUMERIC changes everything to float
        # For every row of the list, append every row element to an environment row, then append environment row to environment
        environment = [[value for value in row] for row in reader]
    return environment


# Make agents based on num_of_agents
def agent_maker(num_of_agents: int, environment: list, ys: list, xs: list) -> list:
    """
    Create list of agents used for simulation.

    Parameters
    ----------
    num_of_agents : int
        The desired number of agents, defaults to length of web agent list.
    environment : list
        Nested(2D) list of environment.
    ys : list
        List of y coordinates retrieved from the web.
    xs : list
        List of x coordinates retrieved from the web.

    Returns
    -------
    list
        List of agentframework.Agent objects.

    """
    # Create empty agents list
    agents = []
    # For every agent, test if there is a coordinate pair from the web for it (not out of bound)
    for i in range(num_of_agents):
        if i < len(ys):
            y = ys[i]
            x = xs[i]
            agents.append(agentframework.Agent(i, environment, agents, y, x))
        # If there is no coordinate pair (out of bounds), one is assigned randomly
        else:
            y = random.randint(0, max(ys))
            x = random.randint(0, max(xs))
            agents.append(agentframework.Agent(i, environment, agents, y, x))
    return agents


# Get agent starting coordinates from the web
def web_scraper(url: str) -> tuple:
    """
    Scrape the web for agent coordinates.

    Parameters
    ----------
    url : str
        The URL of the agent coordinates data on the web.

    Returns
    -------
    tuple
        Tuple of lists ([y coordinates], [x coordinates]).

    """
    # Fetch the url and download the text the html site contains
    r = requests.get(url)
    content = r.text
    # Parse html text to make it selectable
    soup = bs4.BeautifulSoup(content, 'html.parser')
    # Find coordinate table
    table = soup.find(id='yxz')
    # Retrieve list of html tags containing x and y values
    ys_html = soup.find_all(attrs={'class': 'y'})
    xs_html = soup.find_all(attrs={'class': 'x'})
    # Extract and convert to integer the numbers from the tags
    ys_basic = [int(y.text) for y in ys_html]
    xs_basic = [int(x.text) for x in xs_html]
    # Scale the numbers to fill the environment list
    ys = [y * round(len(environment) / max(ys_basic)) for y in ys_basic]
    xs = [x * round(len(environment[0]) / max(xs_basic)) for x in xs_basic]
    return ys, xs


# Writes environment file to out.txt
def env_writer(outfile: str) -> None:
    """
    Write environment list to text file after simulation.

    Parameters
    ----------
    outfile : str
        Name of the output textfile.

    Returns
    -------
    None

    """
    # Write environment out at the end to a file
    with open(outfile, 'w') as f:
        writer = csv.writer(f)
        for line in environment:
            writer.writerow(line)


# 3. Overwrite __str__ method of agents to print location and storage
def agent_printer(agents: list) -> None:
    """
    Print agent properties.

    Parameters
    ----------
    agents : list
        List of agentframework.Agent objects.

    Returns
    -------
    None

    """
    for agent in agents:
        print(agent)


# Create figure for animated plotting
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)  # Does not scale automatically

# Read environment list
environment = env_reader('in.txt')

# Scrape web for agent coordinate information
ys, xs = web_scraper('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')

# # Create command-line functionality (needs positional arguments from command line to run)
# parser = argparse.ArgumentParser(description='Simulate random moving agents grazing a field and sharing food')
# # Add arguments
# parser.add_argument('agents', help='Number of agents (integer)', type=int)
# parser.add_argument('iterations', help='Number of iterations (integer)', type=int)
# parser.add_argument('neighbourhood', help='Radius of agent communication zone (integer)', type=int)
# parser.add_argument('--multirun', help='Specifies if the model is run as a subprocess or not (integer, defult: 0)',
#                     type=int, required=False, default=0)

# Create command-line functionality (needs positional arguments from command line to run)
parser = argparse.ArgumentParser(description='Simulate random moving agents grazing a field and sharing food')
# Add arguments
parser.add_argument('--agents', help='Number of agents (integer)', type=int, required=False, default=len(ys))
parser.add_argument('--iterations', help='Number of iterations (integer)', type=int, required=False, default=100)
parser.add_argument('--neighbourhood', help='Radius of agent communication zone (integer)', type=int, required=False, default=20)
parser.add_argument('--multirun', help='Specifies if the model is run as a subprocess or not (integer, defult: 0)',
                    type=int, required=False, default=0)

# Declare number of agents and iterations, along with neighbourhood size (all from argparse cmd)
num_of_agents = parser.parse_args().agents
num_of_iterations = parser.parse_args().iterations
neighbourhood = parser.parse_args().neighbourhood
multirun = parser.parse_args().multirun


# Append to agents list
agents = agent_maker(num_of_agents, environment, ys, xs)

# Create GUI canvas
root = tkinter.Tk()
root.protocol('WM_DELETE_WINDOW', quit_me)  # exists program when window closed
root.wm_title('Model')
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)  # Plot fig on canvas
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create menu with Run functionality
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label='Model', menu=model_menu)  # Model button
model_menu.add_command(label='Run model', command=run)  # Run button in the drop-down list of Model

# Initialise main loop
root.mainloop()
