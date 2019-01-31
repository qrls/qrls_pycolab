import random
from time import sleep
def AgentModel(Observation,actions,reward):
	sleep(0.05)
	action = random.choice(actions)
	return action