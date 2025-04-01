
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TherapyEnv(gym.Env):
    def __init__(self):
        super(TherapyEnv, self).__init__()
        self.grid_size = 5
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=self.grid_size - 1, shape=(2,), dtype=np.int32)
        self.goal_pos = np.array([4, 3])
        self.state = None

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.array([0, 0])
        return self.state, {}

    def step(self, action):
        x, y = self.state
        if action == 0: x = max(x - 1, 0)
        elif action == 1: x = min(x + 1, self.grid_size - 1)
        elif action == 2: y = max(y - 1, 0)
        elif action == 3: y = min(y + 1, self.grid_size - 1)
        self.state = np.array([x, y])
        reward = -1
        done = np.array_equal(self.state, self.goal_pos)
        if done:
            reward = 10
        return self.state, reward, done, False, {}

    def render(self):
        print(f"Agent at {self.state}")
