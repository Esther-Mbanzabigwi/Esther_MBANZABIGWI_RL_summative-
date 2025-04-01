# Esther_MBANZABIGWI_RL_summative-

# 🤖 Therapy RL Agent – Guided Session Navigation

This project simulates an AI-powered therapy assistant navigating a custom 5x5 grid environment to recommend personalized mental health interventions. It compares two reinforcement learning techniques: **Deep Q-Network (DQN)** and **Proximal Policy Optimization (PPO)** using a non-generic, culturally contextual mission-based environment.

## 🌍 Environment Overview
The grid represents a therapeutic journey with labeled cells like:

- 🩵 Journaling
- 💨 Breathing Exercises
- 💬 Chatbot Support
- 🧠 CBT Modules
- 🚨 Crisis Handling

The agent’s goal is to reach the **Crisis** cell from a random start using optimal actions.

## 🧠 Models Implemented
| Model | Type | Highlights |
|-------|------|------------|
| `DQN` | Value-Based | Uses Q-values, ε-greedy, replay buffer, target network |
| `PPO` | Policy-Based | Actor-Critic, clipped objective, entropy regularization |

## 🎯 Action Space
The agent can take 4 discrete actions:  
`[0: Up, 1: Down, 2: Left, 3: Right]`

## 🏁 Reward Function

```math
R(s, a) =
  +10 if agent reaches goal
  -1  per step
  -5  if bumping into boundaries
```

## 📈 Performance Summary

| Metric                     | DQN        | PPO        |
|----------------------------|------------|------------|
| Avg Reward (Train)         | ~3.2       | ~5.8       |
| Success Rate (Unseen)      | 60%        | 90%        |
| Convergence Episode        | 9–10       | 6–7        |
| Avg Steps to Goal          | ~14        | ~9         |

## 🖼️ Environment Visualization

![Therapy Agent Simulation](therapy_agent_simulation.gif)

## 📁 Project Structure

```
project_root/
├── environment/
│   └── custom_env.py
├── training/
│   ├── dqn_training.py
│   └── ppo_training.py
├── rendering_active.py
├── models/
│   ├── dqn/
│   └── ppo/
├── Final_RL_Summative_With_Headings.ipynb
├── Esther_ML_Report_With_Tables_Final.docx
└── README.md
```

## 🙌 Author
**Esther Mbanzabigwi**  
Machine Learning Techniques II – African Leadership University  
“Built for real-world change. Powered by faith.”
