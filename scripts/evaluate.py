import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

df = pd.read_csv("results/experiment_logs.csv")
model = SentenceTransformer('all-MiniLM-L6-v2')

metrics = []
for index, row in df.iterrows():
    homo_rounds = str(row['homogeneous_transcript']).split("--- Round")
    hetero_rounds = str(row['heterogeneous_transcript']).split("--- Round")
    
    # Calculate basic semantic similarity between first and last agent outputs as a proxy for divergence
    homo_emb = model.encode([homo_rounds[1], homo_rounds[-1]])
    hetero_emb = model.encode([hetero_rounds[1], hetero_rounds[-1]])
    
    metrics.append({
        "topic_id": row['topic_id'],
        "homo_semantic_overlap": cosine_similarity([homo_emb[0]], [homo_emb[1]])[0][0],
        "hetero_semantic_overlap": cosine_similarity([hetero_emb[0]], [hetero_emb[1]])[0][0],
        "homo_rounds_detected": len(homo_rounds) - 1,
        "hetero_rounds_detected": len(hetero_rounds) - 1
    })

metrics_df = pd.DataFrame(metrics)
metrics_df.to_csv("results/metrics.csv", index=False)
print("Evaluation complete. Metrics saved to results/metrics.csv")