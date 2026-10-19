import pandas as pd
import os
from src.debate_engine import run_debate

os.makedirs("results", exist_ok=True)

topics = [
    "A mechanism for room-temperature superconductivity in carbon-based lattices.",
    "A novel binding target for broad-spectrum antiviral nanobodies."
]

homogeneous_agents = {
    "Agent 1": "You are a helpful AI scientist.",
    "Agent 2": "You are a helpful AI scientist.",
    "Agent 3": "You are a helpful AI scientist."
}

heterogeneous_agents = {
    "Expert": "You are a domain-specific structural chemist. Focus on physical viability.",
    "Optimist": "You are a creative theorist. Propose bold, unconventional connections.",
    "Skeptic": "You are a harsh critic. Aggressively look for data leakage, physical impossibilities, or known failures."
}

results = []
for idx, topic in enumerate(topics):
    print(f"Running topic {idx+1}...")
    homo_log = run_debate(topic, homogeneous_agents)
    hetero_log = run_debate(topic, heterogeneous_agents)
    
    results.append({
        "topic_id": idx,
        "homogeneous_transcript": homo_log,
        "heterogeneous_transcript": hetero_log
    })

df = pd.DataFrame(results)
df.to_csv("results/experiment_logs.csv", index=False)
print("Experiment complete. Logs saved to results/experiment_logs.csv")