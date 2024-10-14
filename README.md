###Tic-Tac-Toe with Sarsa Learning
In this repository, we train agents to play a 4x4 Tic-Tac-Toe game using Sarsa Learning.

###How It Works
The agents are trained by a teacher agent that knows the optimal strategy, but only follows this strategy with a given probability p. At each turn, the teacher either:

Chooses the optimal move (with probability p)
Chooses a random valid move (with probability 1 - p)
This random behavior allows the learning agents to occasionally win and learn from their successes.

To initialize the Q-values for the learning agent, I use Python's defaultdict with default values of 0, meaning that every state-action pair starts with a Q-value of 0.

###Code Structure
teacher.py
Implements the Teacher Agent, which knows the optimal policy for any given state. However, the teacher follows this policy only with a set probability.

agent.py
Implements the SARSA Learning Agents, which learn based on their interactions with the environment (the game board).

game.py
Contains the main Game class, which handles the game logic and state management. The primary game loop is found in the playGame() method.

###Running the Program
1. Train a New Agent with Teacher Guidance
To train a new RL agent with the help of a teacher agent, use the -t flag followed by the number of game iterations you want to train:

bash
Sao chép mã
python play.py -a q -t 5000
In this example, the agent will be trained for 5000 games. In my training, I used 200,000 games:

bash
Sao chép mã
python play.py -a q -t 200000
2. Load a Trained Agent and View Reward History
To load a pre-trained agent and view a plot of its cumulative reward history, run the following script:

bash
Sao chép mã
python plot_agent_reward.py -p q_agent.pkl
This will generate a plot showing how the agent's reward evolves over time.

###Result
The reward plot illustrates how the agent learns and improves its strategy as it plays more games.
![Figure_1](https://github.com/user-attachments/assets/a881cc5f-e0b2-4f39-83fc-6a86fb0d3f69)
