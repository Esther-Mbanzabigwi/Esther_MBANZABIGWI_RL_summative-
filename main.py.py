
from stable_baselines3 import DQN, PPO
from environment.custom_env import TherapyEnv

def evaluate_model(model, env, label):
    total_rewards = []
    for ep in range(10):
        obs = env.reset()[0]
        done = False
        ep_reward = 0
        steps = 0
        while not done and steps < 50:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, _, _ = env.step(action)
            ep_reward += reward
            steps += 1
        total_rewards.append(ep_reward)
    avg_reward = sum(total_rewards) / len(total_rewards)
    print(f"{label} - Average Reward over 10 episodes: {avg_reward}")

def main():
    env = TherapyEnv()
    dqn_model = DQN.load("dqn_model")
    ppo_model = PPO.load("ppo_model")

    evaluate_model(dqn_model, env, "DQN")
    evaluate_model(ppo_model, env, "PPO")

if __name__ == "__main__":
    main()
