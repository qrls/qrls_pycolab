import random
import numpy as np
from time import sleep
def AgentModel(Observation,actions,reward):
	sleep(0.05)
	#action = random.choice(actions)
	Observation_size = Observation.size()
	action_size = len(actions)
	qtable = np.zeros((Observation_size, action_size))
	return action