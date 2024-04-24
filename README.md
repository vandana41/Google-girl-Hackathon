!!!!! NOC Optimization and Performance Analysis Tools !!!!!

This project comprises two main modules: a Performance Analysis tool that calculates average latency and bandwidth from monitoring transaction logs, and an RL-based NOC Optimization tool that uses reinforcement learning to optimize network on chip (NOC) configurations.

Features
Latency and Bandwidth Calculator: Computes average latency and bandwidth using transaction logs.
RL NOC Optimizer: Applies reinforcement learning to optimize NOC communication strategies.


Getting Started
Prerequisites
Ensure you have Python 3.7+ installed on your machine. The following additional packages are necessary:

1 numpy (for numerical operations)
2 tensorflow or pytorch (for implementing and running the RL model)


Installation
1 Clone the repository: git clone <repository-url>
2 Navigate to the project directory: cd <repository-name>
3 Install the required Python packages: pip install numpy tensorflow

Usage
1 To run the Latency and Bandwidth Calculator: python latency_bandwidth_calculator.py
2 To start the RL NOC Optimizer: python rl_noc_optimizer.py



!!! Algorithmic Approach !!!

Latency and Bandwidth Calculator
The calculator processes a stream of transactions from system monitors, identifying read and write operations to compute latency for each read operation and cumulative data transferred over the simulation period. The timestamp of the last operation is used to calculate total cycles, allowing for average bandwidth computation.

!!! RL NOC Optimizer !!!

Utilizes a reinforcement learning model, possibly a Deep Q-Network (DQN), to optimize decision-making in a simulated NOC environment. The agent learns from the state-action-reward mechanism through episodes, improving its policy based on the received rewards and observed next states.


Proof of Correctness :

Latency and Bandwidth Calculator
The correctness is ensured by maintaining a dictionary that maps data addresses to their first read timestamp, subsequently using this mapping to calculate latency when the corresponding data write occurs. The total data transferred and the highest timestamp encountered provide the necessary metrics for bandwidth calculation.

RL NOC Optimizer :

The model's correctness relies on the proper implementation of the RL framework, ensuring the agent effectively learns from incremental rewards and state transitions. This requires rigorous testing through various scenarios within the simulation environment.

Complexity Analysis :

Latency and Bandwidth Calculator
The computational complexity mainly involves iterating over the transaction entries, making the time complexity O(n) where n is the number of transactions. Space complexity revolves around the storage requirements for the read transactions dictionary, which is O(m) where m is the number of unique read addresses.

RL NOC Optimizer :

The complexity is largely dependent on the number of states and actions in the RL model, the complexity of the environment's state transition function, and the computational overhead of updating the model's weights during learning.

Contributing :

To contribute to this project, please fork the repository and submit a pull request with your suggested changes. All contributions are expected to adhere to the project's coding standards.

License : This project is licensed under the MIT License - see the LICENSE file for details.

Authors
[Vandana Kandpal ] - Initial work
