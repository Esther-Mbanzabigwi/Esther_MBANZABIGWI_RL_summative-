
from stable_baselines3 import DQN
from environment.custom_env import TherapyEnv

def train_dqn():
    env = TherapyEnv()
    model = DQN(
        "MlpPolicy", 
        env, 
        learning_rate=0.001, 
        buffer_size=10000, 
        learning_starts=1000,
        batch_size=64, 
        tau=1.0, 
        gamma=0.99,
        train_freq=1, 
        target_update_interval=500,
        exploration_fraction=0.1,
        exploration_final_eps=0.02,
        verbose=1
    )
    model.learn(total_timesteps=10000)
    model.save("dqn_model")

if __name__ == "__main__":
    train_dqn()
