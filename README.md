# Agent-based Model

Author: [simagyari](https://github.com/simagyari)  
Version: 1.0.0

## Description

This software was made as a practical and assignment piece for **GEOG5990M Programming for Geographical Information Analysis: Core Skills**. The software implements an agent-based model, featuring an environment and agents interacting with it and with each other inside the allocated spatial and temporal constraints.  
Thus, the model can be likened to sheep, or any other animal, grazing a field. Agent information is taken from the [web](https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html) for the first 100 agents, then generated randomly between 0 and the maximum of web-based agent coordinates.

The agent actions are displayed on an animation and final results of the simulation are outputted to specific files, detailed in [What to expect while running the code](markdown-header-what-to-excpect-while-running-the-code).

## Software requirements

The code was run on a [Windows](https://www.microsoft.com/en-us/windows?r=1) 11 operating system, while [Python](https://www.python.org/) was operated through the [Anaconda](https://www.anaconda.com/) distribution. The versions of Python and the packages used are displayed below:

| **Software** | **Version** |
| :------- | :-----: |
| Python (packages below) | 3.9.7 |
| - matplotlib | 3.4.3 |
| - csv | 1.0 |
| - random | 3 |
| - argparse | 1.1 |
| - tk | 8.6.11 |
| - requests | 2.26.0 |
| - beautifulsoup4 | 4.10.0 |

## Installation

To install the model, download the source code from https://github.com/simagyari/GEOG5990M as a .zip file and unzip, or clone the repository to your local machine. The necessary files to download for the model to run are:
 - model.py
 - agentframework.py
 - agentstorage.py
 - in.txt

The code can be installed into your preferred folder, however, it is advised to be careful not to cause disturbance in the way other code runs by using these files from the same directory as them.

Once installed, the model is ready to run, provided that [Software Requirements](markdown-header-software-requirements) are satisfied ***AND*** an environment raster is provided as a nested list, called "in.txt", of numerical values in the same directory as model.py.

## Contents of the software

| **File** | **Description** |
| :--- | :---------- |
| agentframework.py | Contains the Agent class and its methods, provides the functionality of agents. |
| agentstorage.py | Contains methods for handling and outputting storage information of agents. |
| model.py | Contains the main functionality needed to run the agent-based model. |
| tests_agentframework.py | Contains unittest functions to test the agentframework methods. |
| in.txt | Contains the environment for the agents to move in. |

## Running the model

The model can be run from the Command Prompt or Powershell on Windows, Terminal on MacOS and Linux distibutions. The code to initialise the model is the following:

```
python model.py --agents [] --iterations [] --neighbourhood []
```
with the square brackets showing the place to insert the integers needed as inputs. The default values of the parameters are:
 - agents: 10
 - iterations: 100
 - neighbourhood: 20

### What to expect while running the code
Once running the above script from the CMD/Powershell/Terminal, a [Tkinter](https://docs.python.org/3/library/tkinter.html) window will pop up with a drop-down menu named Model in the upper right corner. From the menu, choose the, only, "Run model" option to start the simulation.  
The running model will output an animation of the agents cycling through every time step, then stopping at the last. Final agent positions and storages will be printed to the console and outputted into "out.txt" automatically created in the same folder as model.py.  
Once the animation has ended, you can close the Tkinter window.

## Testing

Testing of the agentframework methods were conducted using the [unittest](https://docs.python.org/3/library/unittest.html) library of Python. The library facilitates testing different units of the code independently. In this case, all functions were tested to give the appropriate results when fed with appropriate parameters, with some of them tested for errors raised on feeding it with the wrong data. The test file is included in the repository, names "tests_agentframework.py". It contains the full code with informative comments on the testing and the exact processes undertaken.

## Profiling

The computer used for profiling had the following specifications:

| **Hardware** | **Specification** |
| :------- | :------------ |
| Processor | AMD Ryzen 7 4800H 2.90 GHz |
| RAM | 32 GB |
| OS | Windows 11 Pro x64 version 21H2 |

The code has been profiled for speed using [cProfile](https://docs.python.org/3/library/profile.html). Through multiple attempts, runtime averaged around 60 seconds in the tkinter mainloop.

Memory profiling was carried out using [memory-profiler](https://pypi.org/project/memory-profiler/). Multiple runs showed that a consistent maximum memory usage of 150 MiB can be observed.

## Known issues

There is only one known issue with the code, and that is an occasional problem with the neighbourhood size. Since it is an integer, and the distance measurements between agents are returned as floating point numbers, which have a slight error due to imperfect storage, agents on the boundary neighbourhood distance can sometimes fall out of sharing. This problem has a low chance of occurring.

## Future development ideas

In the future, there are several optimisation options that can take place, such as:

1. Interface changes - the interface can accommodate input boxes and buttons to more comfortably control input values.
2. Speed optimisation - as much of the code is written in pure Python, there is probably space for performance improvement, even though some work has been done following the profiling on this.
3. Output optimisation - the agentstorage functions could be able to output the time and initial parameters of the runs, giving more information and better distinguishing between different model runs.

#### Thank you for reading through this README file, I hope you will find this program useful.
