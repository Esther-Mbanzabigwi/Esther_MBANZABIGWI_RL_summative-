
from stable_baselines3 import PPO
from environment.custom_env import TherapyEnv

def train_ppo():
    env = TherapyEnv()
    model = PPO(
        "MlpPolicy", 
        env, 
        learning_rate=0.0003,
        n_steps=512,
        batch_size=64,
        gamma=0.95,
        gae_lambda=0.95,
        clip_range=0.2,
        ent_coef=0.01,
        vf_coef=0.5,
        max_grad_norm=0.5,
        verbose=1
    )
    model.learn(total_timesteps=10000)
    model.save("ppo_model")

if __name__ == "__main__":
    train_ppo()
