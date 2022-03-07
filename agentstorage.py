# Sums stored food of every agent in the list
def all_storage_writer(agents: list, outfile: str) -> None:
    all_storage = 0
    for agent in agents:
        all_storage += agent.store
    print('Storage is', all_storage)  # Prints current run's storage on terminal
    # Appends storage to storage.txt file
    with open(outfile, 'a') as f:
        f.write('Combined storage of all agents: ' + str(all_storage) + '\n')
    print('Total amount stored by all agents recorded in "storage.txt"')

# Writes the individual storage of each agent at the end of simulation
def agent_storage_writer(agents: int, outfile: str) -> None:
    agent_storage = []
    for agent in agents:
        agent_storage.append(agent.store)
    print('Storage of agents:\n', agent_storage)
    with open(outfile, 'a') as f:
        f.write('Individual storage of agents: ' + str(agent_storage)[1:-1] + '\n')
    print('Amount of food stored by each agent recorded in "storage.txt"')